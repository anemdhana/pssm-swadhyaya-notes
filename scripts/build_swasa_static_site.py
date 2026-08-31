# -*- coding: utf-8 -*-
"""Build GitHub Pages site from expanded Blogger Q&A HTML."""
from __future__ import annotations

import re
from pathlib import Path

SRC = Path(r"C:\Users\dhana\Downloads\Swasa_Maha_Vidya_All_Days_Expanded_QA_Blogger")
OUT = Path(__file__).resolve().parents[1] / "swasa_maha_vidya"

PAGES = [
    {
        "src": "Swasa_Maha_Vidya_Day1_QA_Blogger.html",
        "out": "day-01.html",
        "label": "1",
        "hub_title": "Day 1",
        "hub_sub": "సూక్ష్మంలో మోక్షం",
    },
    {
        "src": "Swasa_Maha_Vidya_Day2_QA_Blogger.html",
        "out": "day-02.html",
        "label": "2",
        "hub_title": "Day 2",
        "hub_sub": "శ్వాస ఆయుష్ప్రమాణం",
    },
    {
        "src": "Swasa_Maha_Vidya_Day3_QA_Blogger.html",
        "out": "day-03.html",
        "label": "3",
        "hub_title": "Day 3",
        "hub_sub": "సూక్ష్మీకరణ",
    },
    {
        "src": "Swasa_Maha_Vidya_Day4_QA_Blogger.html",
        "out": "day-04.html",
        "label": "4",
        "hub_title": "Day 4",
        "hub_sub": "శ్వాసే వాక్కు",
    },
    {
        "src": "Swasa_Maha_Vidya_Day5_QA_Blogger.html",
        "out": "day-05.html",
        "label": "5",
        "hub_title": "Day 5",
        "hub_sub": "పంచ మహా ప్రాణాలు",
    },
    {
        "src": "Swasa_Maha_Vidya_Day6_QA_Blogger.html",
        "out": "day-06.html",
        "label": "6",
        "hub_title": "Day 6",
        "hub_sub": "శ్వాస భాష",
    },
    {
        "src": "Swasa_Maha_Vidya_Day7_QA_Blogger.html",
        "out": "day-07.html",
        "label": "7",
        "hub_title": "Day 7",
        "hub_sub": "పంచ తత్వాలు",
    },
    {
        "src": "Swasa_Maha_Vidya_Day8_QA_Blogger.html",
        "out": "day-08.html",
        "label": "8",
        "hub_title": "Day 8",
        "hub_sub": "Art of Dying",
    },
    {
        "src": "Swasa_Maha_Vidya_Day9_QA_Blogger.html",
        "out": "day-09.html",
        "label": "9",
        "hub_title": "Day 9",
        "hub_sub": "Science of Manifestation",
    },
    {
        "src": "Swasa_Maha_Vidya_Day10_QA_Blogger.html",
        "out": "day-10.html",
        "label": "10",
        "hub_title": "Day 10",
        "hub_sub": "అశ్వినీ దేవతలు",
    },
    {
        "src": "Swasa_Maha_Vidya_Day11_QA_Blogger.html",
        "out": "day-11.html",
        "label": "11",
        "hub_title": "Day 11",
        "hub_sub": "Characteristics of the Breath",
    },
    {
        "src": "Swasa_Maha_Vidya_Bonus_QA_Blogger.html",
        "out": "bonus.html",
        "label": "B",
        "hub_title": "Bonus",
        "hub_sub": "యోగం–వియోగం",
    },
]


def extract_title(text: str) -> str:
    m = re.search(r"<title>(.*?)</title>", text, re.S)
    return m.group(1).strip() if m else "శ్వాస మహావిద్య"


def extract_article_inner(text: str) -> str:
    m = re.search(r'<article class="post-card">(.*?)</article>', text, re.S)
    if not m:
        raise ValueError("No article found")
    return m.group(1).strip()


def chrome(current_out: str) -> str:
    pills = []
    for p in PAGES:
        cls = ' class="is-current"' if p["out"] == current_out else ""
        pills.append(f'      <a href="{p["out"]}"{cls}>{p["label"]}</a>')
    return f"""    <header class="site-header">
      <a class="site-brand" href="index.html">శ్వాస మహావిద్య
        <span>Dr. Newton Kondaveti</span>
      </a>
      <nav>
        <a href="index.html">All days</a>
      </nav>
    </header>
    <nav class="day-strip" aria-label="Days">
{chr(10).join(pills)}
    </nav>
"""


def pager(idx: int) -> str:
    prev_html = '<span>← Previous</span>'
    next_html = '<span>Next →</span>'
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
<html lang="te">
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
    <footer class="site-footer">శ్వాస మహావిద్య · Dr. Newton Kondaveti · Vikarabad</footer>
  </div>
</body>
</html>
"""


def write_teacher_index() -> None:
    items = []
    for p in PAGES:
        items.append(
            f'      <li><a href="{p["out"]}"><strong>{p["hub_title"]}</strong><em>{p["hub_sub"]}</em></a></li>'
        )
    html = f"""<!DOCTYPE html>
<html lang="te">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>శ్వాస మహావిద్య · Dr. Newton Kondaveti</title>
  <link rel="stylesheet" href="css/site.css">
</head>
<body>
  <div class="site-wrap">
    <header class="site-header">
      <a class="site-brand" href="index.html">శ్వాస మహావిద్య
        <span>Dr. Newton Kondaveti</span>
      </a>
      <nav>
        <a href="index.html">All days</a>
      </nav>
    </header>
    <div class="hub-card">
      <h1>ప్రశ్నోత్తరాలు</h1>
      <p class="lede">జ్ఞానోదయం · Swasa Maha Vidya. డా. న్యూటన్ కొండవేటి బోధన ఆధారంగా. Vikarabad, Telangana, Bharath Desh.</p>
      <ul class="day-list">
{chr(10).join(items)}
      </ul>
    </div>
    <footer class="site-footer">Static pages for GitHub Pages</footer>
  </div>
</body>
</html>
"""
    (OUT / "index.html").write_text(html, encoding="utf-8")


def write_nojekyll() -> None:
    (OUT / ".nojekyll").write_text("", encoding="utf-8")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "css").mkdir(exist_ok=True)
    for i, page in enumerate(PAGES):
        src = SRC / page["src"]
        text = src.read_text(encoding="utf-8")
        html = wrap(extract_title(text), extract_article_inner(text), i)
        dest = OUT / page["out"]
        dest.write_text(html, encoding="utf-8")
        print(f"Wrote {dest.relative_to(OUT.parent)}")
    write_teacher_index()
    write_nojekyll()
    print("Wrote indexes")


if __name__ == "__main__":
    main()
