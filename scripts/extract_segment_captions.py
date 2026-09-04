#!/usr/bin/env python3
"""
Extract precise timestamped captions for a YouTube video segment.

Video : Uu88QpHpXgE
Range : 54:32  →  1:44:07   (interpreted as MM:SS / HH:MM:SS)

Usage examples:
  python extract_segment_captions.py
  python extract_segment_captions.py --cookies-from-browser chrome
  python extract_segment_captions.py --cookies cookies.txt
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yt_dlp
except ImportError:
    print("Install yt-dlp first:  pip install -U yt-dlp")
    sys.exit(1)


VIDEO_ID = "Uu88QpHpXgE"
# User requested: --start 54:32:00 --end 01:44:07
# Interpreted as start=54m32s, end=1h44m07s
START_SECONDS = 54 * 60 + 32          # 3272
END_SECONDS   = 1 * 3600 + 44 * 60 + 7  # 6247


def hms(seconds: float) -> str:
    """Format seconds → HH:MM:SS,mmm"""
    ms = int(round((seconds % 1) * 1000))
    s = int(seconds) % 60
    m = (int(seconds) // 60) % 60
    h = int(seconds) // 3600
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def parse_vtt_or_srt(content: str) -> list[dict[str, Any]]:
    """Parse VTT or SRT into clean timed segments."""
    # Normalize line endings
    content = content.replace("\r\n", "\n").replace("\r", "\n")
    blocks = re.split(r"\n\s*\n", content.strip())
    segments = []

    for block in blocks:
        lines = [ln.strip() for ln in block.splitlines() if ln.strip()]
        if not lines:
            continue

        ts_line = None
        text_lines = []
        for ln in lines:
            if "-->" in ln:
                ts_line = ln
            elif ts_line is not None and not ln.isdigit():
                # skip pure index numbers
                text_lines.append(ln)

        if not ts_line or not text_lines:
            continue

        try:
            start_raw, end_raw = [t.strip() for t in ts_line.split("-->")]
            # Clean VTT style (may contain position info after timestamp)
            start_raw = start_raw.split()[0]
            end_raw = end_raw.split()[0]
            # Convert . to , for SRT consistency
            start = start_raw.replace(".", ",")
            end = end_raw.replace(".", ",")

            # Convert to seconds for filtering
            def to_sec(t: str) -> float:
                t = t.replace(",", ".")
                parts = t.split(":")
                if len(parts) == 3:
                    h, m, s = parts
                    return int(h) * 3600 + int(m) * 60 + float(s)
                elif len(parts) == 2:
                    m, s = parts
                    return int(m) * 60 + float(s)
                return float(t)

            start_s = to_sec(start)
            end_s = to_sec(end)

            text = re.sub(r"\s+", " ", " ".join(text_lines)).strip()
            # Remove common auto-caption artefacts
            text = re.sub(r"<[^>]+>", "", text)  # strip HTML-like tags

            if text:
                segments.append({
                    "start": start,
                    "end": end,
                    "start_seconds": round(start_s, 3),
                    "end_seconds": round(end_s, 3),
                    "text": text,
                })
        except Exception:
            continue

    return segments


def extract(video_id: str, start_s: float, end_s: float,
            cookies: Path | None = None,
            cookies_from_browser: str | None = None,
            out_dir: Path = Path("segment_captions")) -> None:

    out_dir.mkdir(parents=True, exist_ok=True)
    url = f"https://www.youtube.com/watch?v={video_id}"

    ydl_opts: dict[str, Any] = {
        "skip_download": True,
        "writesubtitles": True,
        "writeautomaticsub": True,
        "subtitleslangs": ["en", "en-US", "en-GB", "en-IN"],
        "subtitlesformat": "vtt",
        "ignoreerrors": False,
        "quiet": False,
        "no_warnings": False,
        "retries": 8,
        "extractor_retries": 5,
        "sleep_interval_requests": 1.5,
        "sleep_interval": 2,
        "max_sleep_interval": 8,
        "extractor_args": {
            "youtube": {
                "player_client": ["tv", "android", "web_safari"],
            }
        },
        # Download only the needed time window for efficiency (if supported)
        "download_ranges": lambda info, ydl: [{"start_time": start_s, "end_time": end_s}],
        "outtmpl": str(out_dir / f"{video_id}.%(ext)s"),
    }

    if cookies:
        ydl_opts["cookiefile"] = str(cookies)
    if cookies_from_browser:
        ydl_opts["cookiesfrombrowser"] = (cookies_from_browser,)

    print(f"Video  : {url}")
    print(f"Range  : {hms(start_s)}  →  {hms(end_s)}")
    print(f"Output : {out_dir.resolve()}")
    print("-" * 60)

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)

    # Find the downloaded subtitle file(s)
    vtt_files = list(out_dir.glob(f"{video_id}*.vtt")) + list(out_dir.glob(f"{video_id}*.srt"))
    if not vtt_files:
        # Sometimes yt-dlp writes with language code
        vtt_files = list(out_dir.glob("*.vtt")) + list(out_dir.glob("*.srt"))

    if not vtt_files:
        print("ERROR: No subtitle file was written.")
        print("Possible causes: no captions available, bot-check, or language mismatch.")
        print("Try again with:  --cookies-from-browser chrome")
        return

    all_segments: list[dict[str, Any]] = []
    for f in vtt_files:
        print(f"Parsing {f.name} …")
        content = f.read_text(encoding="utf-8", errors="replace")
        segs = parse_vtt_or_srt(content)
        all_segments.extend(segs)

    # Deduplicate & filter to the requested window (with small margin)
    seen = set()
    filtered = []
    for s in sorted(all_segments, key=lambda x: x["start_seconds"]):
        key = (s["start_seconds"], s["text"])
        if key in seen:
            continue
        seen.add(key)
        # Keep cues that overlap the requested range
        if s["end_seconds"] >= start_s - 2 and s["start_seconds"] <= end_s + 2:
            filtered.append(s)

    print(f"\nKept {len(filtered)} caption segments inside the time window.\n")

    # Write clean SRT
    srt_path = out_dir / f"{video_id}_segment_{int(start_s)}-{int(end_s)}.srt"
    with srt_path.open("w", encoding="utf-8") as fh:
        for i, s in enumerate(filtered, 1):
            fh.write(f"{i}\n")
            fh.write(f"{s['start']} --> {s['end']}\n")
            fh.write(f"{s['text']}\n\n")
    print(f"SRT written → {srt_path}")

    # Write JSON (precise, machine-readable)
    json_path = out_dir / f"{video_id}_segment_{int(start_s)}-{int(end_s)}.json"
    payload = {
        "video_id": video_id,
        "start_seconds": start_s,
        "end_seconds": end_s,
        "start_hms": hms(start_s),
        "end_hms": hms(end_s),
        "segment_count": len(filtered),
        "segments": filtered,
    }
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"JSON written → {json_path}")

    # Also a plain readable text with timestamps
    txt_path = out_dir / f"{video_id}_segment_{int(start_s)}-{int(end_s)}.txt"
    with txt_path.open("w", encoding="utf-8") as fh:
        fh.write(f"Video: https://www.youtube.com/watch?v={video_id}\n")
        fh.write(f"Segment: {hms(start_s)} → {hms(end_s)}\n")
        fh.write("=" * 60 + "\n\n")
        for s in filtered:
            fh.write(f"[{s['start']} → {s['end']}]\n{s['text']}\n\n")
    print(f"TXT written → {txt_path}")


def main() -> None:
    p = argparse.ArgumentParser(description="Extract timestamped captions for a YouTube segment")
    p.add_argument("--start", type=float, default=START_SECONDS,
                   help="Start time in seconds (default: 3272 = 54:32)")
    p.add_argument("--end", type=float, default=END_SECONDS,
                   help="End time in seconds (default: 6247 = 1:44:07)")
    p.add_argument("--cookies", type=Path, default=None)
    p.add_argument("--cookies-from-browser", default=None,
                   help="chrome / firefox / edge / brave …")
    p.add_argument("--out-dir", type=Path, default=Path("segment_captions"))
    args = p.parse_args()

    extract(
        VIDEO_ID,
        args.start,
        args.end,
        cookies=args.cookies,
        cookies_from_browser=args.cookies_from_browser,
        out_dir=args.out_dir,
    )


if __name__ == "__main__":
    main()
