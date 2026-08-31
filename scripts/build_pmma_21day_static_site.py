# -*- coding: utf-8 -*-
"""Build GitHub Pages site for 21-Day Meditation with Music (PMMA)."""
from __future__ import annotations

import html as html_lib
import re
from pathlib import Path

SRC = Path(r"C:\Users\dhana\Downloads\21-Day-Meditation-with-Music-PMMA\21-day-meditation")
OUT = Path(__file__).resolve().parents[1] / "21-Day-Meditation-with-Music-PMMA"

HUB_SUBS = [
    "Introduction to Sound & Breath",
    "Pythagoras & the Harmony of Sound",
    "Aristotle on Sound",
    "Tesla & Resonance",
    "What is Nada Yoga?",
    "Breath + Sound (Pranava)",
    "Integration – Simple Daily Practice",
    "Root Chakra (Muladhara) – 396 Hz",
    "Sacral Chakra (Svadhisthana) – 417 Hz",
    "Solar Plexus (Manipura) – 528 Hz",
    "Heart Chakra (Anahata) – 639 Hz",
    "Throat Chakra (Vishuddha) – 741 Hz",
    "Third Eye (Ajna) – 852 Hz",
    "Crown Chakra (Sahasrara) – 963 Hz",
    "The 72,000 Nadis",
    "How Frequency Uplifts the Energy Body",
    "Combining Classical Music + Frequency Work",
    "Inner Listening (Anāhata Nāda)",
    "Full Chakra Journey",
    "Personal Resonance",
    "Integration & Closing",
]

WEEKS = [
    (1, 7, "Week 1 — Foundations"),
    (8, 14, "Week 2 — Chakras & Frequencies"),
    (15, 21, "Week 3 — Nadis & Advanced Practice"),
]

PAGES = [
    {
        "src": f"day{n:02d}.html",
        "out": f"day-{n:02d}.html",
        "label": str(n),
        "hub_title": f"Day {n}",
        "hub_sub": HUB_SUBS[n - 1],
        "day": n,
    }
    for n in range(1, 22)
]


def extract_title(text: str, fallback: str) -> str:
    m = re.search(r"<title>(.*?)</title>", text, re.S)
    return m.group(1).strip() if m else fallback


def extract_h1(text: str, fallback: str) -> str:
    m = re.search(r"<h1>(.*?)</h1>", text, re.S)
    if not m:
        return fallback
    return re.sub(r"<[^>]+>", "", m.group(1)).strip()


def extract_sections(text: str) -> str:
    m = re.search(r"<body>(.*?)</body>", text, re.S)
    if not m:
        raise ValueError("No body found")
    body = m.group(1)
    start = body.find("<h2>")
    end = body.find('<div class="nav">')
    if start < 0 or end < 0:
        raise ValueError("Could not find day sections")
    return body[start:end].strip()


def article_inner(src_html: str, page: dict) -> str:
    h1 = extract_h1(src_html, page["hub_sub"])
    sections = extract_sections(src_html)
    return f"""    <div class="author-row">
      <img src="images/pmma-logo.png" alt="Pyramid Music Meditation Academy">
      <div class="author-info">
        <strong>Pyramid Music Meditation Academy</strong>
        <span>PMMA · Dhyanam Sharanam Gachchami</span>
      </div>
    </div>
    <p class="eyebrow">21-Day Meditation with Music • Day {page["label"]}</p>
    <h1>{html_lib.escape(h1)}</h1>

{sections}

    <div class="closing">
      Pyramid Music Meditation Academy (PMMA) · 21-Day Meditation with Music Programme
    </div>"""


def day_strip(current_out: str) -> str:
    pills = []
    for p in PAGES:
        cls = ' class="is-current"' if p["out"] == current_out else ""
        pills.append(f'      <a href="{p["out"]}"{cls}>{p["label"]}</a>')
    return "\n".join(pills)


def chrome(current_out: str) -> str:
    return f"""    <header class="site-header">
      <a class="site-brand" href="index.html">
        <img src="images/pmma-logo.png" alt="Pyramid Music Meditation Academy">
        <span class="brand-text">21-Day Meditation with Music
        <span>Pyramid Music Meditation Academy</span></span>
      </a>
      <nav>
        <a href="index.html">Programme</a>
      </nav>
    </header>
    <nav class="day-strip" aria-label="Days">
{day_strip(current_out)}
    </nav>
"""


def pager(idx: int) -> str:
    prev_html = "<span>← Previous</span>"
    next_html = "<span>Next →</span>"
    if idx > 0:
        p = PAGES[idx - 1]
        prev_html = f'<a href="{p["out"]}">← {p["hub_title"]}</a>'
    if idx < len(PAGES) - 1:
        n = PAGES[idx + 1]
        next_html = f'<a href="{n["out"]}">{n["hub_title"]} →</a>'
    return f"""    <nav class="pager">
      {prev_html}
      {next_html}
    </nav>
"""


def wrap(title: str, inner: str, idx: int) -> str:
    current = PAGES[idx]["out"]
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="stylesheet" href="css/site.css">
</head>
<body>
  <div class="site-wrap">
{chrome(current)}
    <article class="post-card">
{inner}
    </article>
{pager(idx)}
    <footer class="site-footer">21-Day Meditation with Music · Pyramid Music Meditation Academy</footer>
  </div>
</body>
</html>
"""


def write_index() -> None:
    chunks: list[str] = []
    for start, end, label in WEEKS:
        chunks.append(f'      <p class="week-label">{html_lib.escape(label)}</p>')
        chunks.append("      <ul class=\"day-list\">")
        for p in PAGES:
            if start <= p["day"] <= end:
                chunks.append(
                    f'      <li><a href="{p["out"]}"><strong>{p["hub_title"]}</strong>'
                    f'<em>{html_lib.escape(p["hub_sub"])}</em></a></li>'
                )
        chunks.append("      </ul>")
    body = "\n".join(chunks)
    home = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>21-Day Meditation with Music · PMMA</title>
  <link rel="stylesheet" href="css/site.css">
</head>
<body>
  <div class="site-wrap">
    <header class="site-header">
      <a class="site-brand" href="index.html">
        <img src="images/pmma-logo.png" alt="Pyramid Music Meditation Academy">
        <span class="brand-text">21-Day Meditation with Music
        <span>Pyramid Music Meditation Academy</span></span>
      </a>
      <nav>
        <a href="index.html">Programme</a>
      </nav>
    </header>
    <div class="hub-card">
      <h1>Programme</h1>
      <p class="lede">From basics to advanced — Nada Yoga, frequencies, chakras and nadis. Each day has a short teaching, a practice, and suggested music or tones.</p>
      <p class="note"><strong>Note:</strong> Chakra frequencies listed are commonly used modern associations (Solfeggio-based). Traditional systems sometimes use different numbers. Music supports meditation and nervous-system regulation — it is not a medical treatment.</p>
{body}
    </div>
    <footer class="site-footer">Static pages for GitHub Pages</footer>
  </div>
</body>
</html>
"""
    (OUT / "index.html").write_text(home, encoding="utf-8")


def main() -> None:
    if not SRC.is_dir():
        raise SystemExit(f"Source folder not found: {SRC}")
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "css").mkdir(exist_ok=True)
    for i, page in enumerate(PAGES):
        src_path = SRC / page["src"]
        src_html = src_path.read_text(encoding="utf-8")
        title = extract_title(src_html, f"{page['hub_title']} | 21-Day Meditation with Music")
        inner = article_inner(src_html, page)
        (OUT / page["out"]).write_text(wrap(title, inner, i), encoding="utf-8")
        print(f"Wrote {page['out']}")
    write_index()
    print("Wrote index.html")


if __name__ == "__main__":
    main()
