# -*- coding: utf-8 -*-
"""Build GitHub Pages site: full notes + Q&A in swasa_maha_vidya/qna/."""
from __future__ import annotations

import re
from pathlib import Path

NOTES_SRC = Path(r"C:\Users\dhana\Downloads\Swasa_Maha_Vidya_All_Days_1-12_Full_Enhanced")
QA_SRC = Path(
    r"C:\Users\dhana\GitHub\pssm-spiritual-text-work\blogger-posts\DrNewtonKondaveti"
)
OUT = Path(__file__).resolve().parents[1] / "swasa_maha_vidya"
QNA_OUT = OUT / "qna"

PAGES = [
    {
        "notes_src": "Swasa_Maha_Vidya_Day1_Sections.html",
        "qa_src": "Swasa_Maha_Vidya_Day1_QA_Blogger.html",
        "out": "day-01.html",
        "label": "1",
        "hub_title": "Day 1",
        "hub_sub": "సూక్ష్మం లో మోక్షం",
    },
    {
        "notes_src": "Swasa_Maha_Vidya_Day2_Sections.html",
        "qa_src": "Swasa_Maha_Vidya_Day2_QA_Blogger.html",
        "out": "day-02.html",
        "label": "2",
        "hub_title": "Day 2",
        "hub_sub": "శ్వాస – ఆయుష్ప్రమాణం",
    },
    {
        "notes_src": "Swasa_Maha_Vidya_Day3_Sections.html",
        "qa_src": "Swasa_Maha_Vidya_Day3_QA_Blogger.html",
        "out": "day-03.html",
        "label": "3",
        "hub_title": "Day 3",
        "hub_sub": "సూక్ష్మీకరణ",
    },
    {
        "notes_src": "Swasa_Maha_Vidya_Day4_Sections.html",
        "qa_src": "Swasa_Maha_Vidya_Day4_QA_Blogger.html",
        "out": "day-04.html",
        "label": "4",
        "hub_title": "Day 4",
        "hub_sub": "శ్వాసే వాక్కు",
    },
    {
        "notes_src": "Swasa_Maha_Vidya_Day5_Sections.html",
        "qa_src": "Swasa_Maha_Vidya_Day5_QA_Blogger.html",
        "out": "day-05.html",
        "label": "5",
        "hub_title": "Day 5",
        "hub_sub": "పంచ మహా ప్రాణాలు",
    },
    {
        "notes_src": "Swasa_Maha_Vidya_Day6_Sections.html",
        "qa_src": "Swasa_Maha_Vidya_Day6_QA_Blogger.html",
        "out": "day-06.html",
        "label": "6",
        "hub_title": "Day 6",
        "hub_sub": "శ్వాస భాష",
    },
    {
        "notes_src": "Swasa_Maha_Vidya_Day7_Sections.html",
        "qa_src": "Swasa_Maha_Vidya_Day7_QA_Blogger.html",
        "out": "day-07.html",
        "label": "7",
        "hub_title": "Day 7",
        "hub_sub": "పంచ తత్వాలు",
    },
    {
        "notes_src": "Swasa_Maha_Vidya_Day8_Sections.html",
        "qa_src": "Swasa_Maha_Vidya_Day8_QA_Blogger.html",
        "out": "day-08.html",
        "label": "8",
        "hub_title": "Day 8",
        "hub_sub": "Art of Dying",
    },
    {
        "notes_src": "Swasa_Maha_Vidya_Day9_Sections.html",
        "qa_src": "Swasa_Maha_Vidya_Day9_QA_Blogger.html",
        "out": "day-09.html",
        "label": "9",
        "hub_title": "Day 9",
        "hub_sub": "Science of Manifestation",
    },
    {
        "notes_src": "Swasa_Maha_Vidya_Day10_Sections.html",
        "qa_src": "Swasa_Maha_Vidya_Day10_QA_Blogger.html",
        "out": "day-10.html",
        "label": "10",
        "hub_title": "Day 10",
        "hub_sub": "అశ్వినీ దేవతలు",
    },
    {
        "notes_src": "Swasa_Maha_Vidya_Day11_Sections.html",
        "qa_src": "Swasa_Maha_Vidya_Day11_QA_Blogger.html",
        "out": "day-11.html",
        "label": "11",
        "hub_title": "Day 11",
        "hub_sub": "Characteristics of the Breath",
    },
    {
        "notes_src": "Swasa_Maha_Vidya_Bonus_Sections.html",
        "qa_src": "Swasa_Maha_Vidya_Day12_Bonus_QA_Blogger.html",
        "out": "bonus.html",
        "label": "B",
        "hub_title": "Bonus",
        "hub_sub": "సారాంశం & మార్గదర్శనం",
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


def day_strip(prefix: str, current_out: str) -> str:
    pills = []
    for p in PAGES:
        cls = ' class="is-current"' if p["out"] == current_out else ""
        pills.append(f'      <a href="{prefix}{p["out"]}"{cls}>{p["label"]}</a>')
    return "\n".join(pills)


def chrome(kind: str, current_out: str) -> str:
    if kind == "notes":
        brand = "index.html"
        notes_link = "index.html"
        qna_link = f"qna/{current_out}"
        strip = day_strip("", current_out)
    else:
        brand = "../index.html"
        notes_link = f"../{current_out}"
        qna_link = "index.html"
        strip = day_strip("", current_out)
    return f"""    <header class="site-header">
      <a class="site-brand" href="{brand}">శ్వాస మహావిద్య
        <span>Dr. Newton Kondaveti</span>
      </a>
      <nav>
        <a href="{notes_link}">బోధన</a>
        <a href="{qna_link}">ప్రశ్నోత్తరాలు</a>
      </nav>
    </header>
    <nav class="day-strip" aria-label="Days">
{strip}
    </nav>
"""


def pager(_kind: str, idx: int) -> str:
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


def wrap(kind: str, title: str, inner: str, idx: int) -> str:
    css = "css/site.css" if kind == "notes" else "../css/site.css"
    current = PAGES[idx]["out"]
    return f"""<!DOCTYPE html>
<html lang="te">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="stylesheet" href="{css}">
</head>
<body>
  <div class="site-wrap">
{chrome(kind, current)}
    <article class="post-card">
{inner}
    </article>
{pager(kind, idx)}
    <footer class="site-footer">శ్వాస మహావిద్య · Dr. Newton Kondaveti · Vikarabad</footer>
  </div>
</body>
</html>
"""


def _hub_page(title_h1: str, lede: str, items: list[str], css: str, brand: str, extra_nav: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="te">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>శ్వాస మహావిద్య · Dr. Newton Kondaveti</title>
  <link rel="stylesheet" href="{css}">
</head>
<body>
  <div class="site-wrap">
    <header class="site-header">
      <a class="site-brand" href="{brand}">శ్వాస మహావిద్య
        <span>Dr. Newton Kondaveti</span>
      </a>
      <nav>
        {extra_nav}
      </nav>
    </header>
    <div class="hub-card">
      <h1>{title_h1}</h1>
      <p class="lede">{lede}</p>
      <ul class="day-list">
{chr(10).join(items)}
      </ul>
    </div>
    <footer class="site-footer">Static pages for GitHub Pages</footer>
  </div>
</body>
</html>
"""


def write_indexes() -> None:
    notes_items = [
        f'      <li><a href="{p["out"]}"><strong>{p["hub_title"]}</strong><em>{p["hub_sub"]}</em></a></li>'
        for p in PAGES
    ]
    qna_items = [
        f'      <li><a href="qna/{p["out"]}"><strong>{p["hub_title"]}</strong><em>{p["hub_sub"]}</em></a></li>'
        for p in PAGES
    ]
    home = f"""<!DOCTYPE html>
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
        <a href="index.html">బోధన</a>
        <a href="qna/index.html">ప్రశ్నోత్తరాలు</a>
      </nav>
    </header>
    <div class="hub-card">
      <h1>బోధన</h1>
      <p class="lede">జ్ఞానోదయం · Swasa Maha Vidya. పూర్తి ఉపన్యాస సారాంశం.</p>
      <ul class="day-list">
{chr(10).join(notes_items)}
      </ul>
      <h1 class="hub-second">ప్రశ్నోత్తరాలు</h1>
      <p class="lede">అదే బోధన ప్రశ్నోత్తరాల రూపంలో.</p>
      <ul class="day-list">
{chr(10).join(qna_items)}
      </ul>
    </div>
    <footer class="site-footer">Static pages for GitHub Pages</footer>
  </div>
</body>
</html>
"""
    (OUT / "index.html").write_text(home, encoding="utf-8")

    qna_list = [
        f'      <li><a href="{p["out"]}"><strong>{p["hub_title"]}</strong><em>{p["hub_sub"]}</em></a></li>'
        for p in PAGES
    ]
    (QNA_OUT / "index.html").write_text(
        _hub_page(
            "ప్రశ్నోత్తరాలు",
            "జ్ఞానోదయం · Swasa Maha Vidya. డా. న్యూటన్ కొండవేటి బోధన ఆధారంగా.",
            qna_list,
            "../css/site.css",
            "../index.html",
            '<a href="../index.html">బోధన</a>\n        <a href="index.html">ప్రశ్నోత్తరాలు</a>',
        ),
        encoding="utf-8",
    )


def write_qna_pages() -> None:
    QNA_OUT.mkdir(parents=True, exist_ok=True)
    for i, page in enumerate(PAGES):
        qa_text = (QA_SRC / page["qa_src"]).read_text(encoding="utf-8")
        qa_html = wrap("qna", extract_title(qa_text), extract_article_inner(qa_text), i)
        (QNA_OUT / page["out"]).write_text(qa_html, encoding="utf-8")
        print(f"Wrote qna/{page['out']}")
    write_indexes()
    print("Wrote indexes")


def write_notes_pages() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "css").mkdir(exist_ok=True)
    for i, page in enumerate(PAGES):
        notes_text = (NOTES_SRC / page["notes_src"]).read_text(encoding="utf-8")
        notes_html = wrap("notes", extract_title(notes_text), extract_article_inner(notes_text), i)
        (OUT / page["out"]).write_text(notes_html, encoding="utf-8")
        print(f"Wrote notes/{page['out']}")


def main(qna_only: bool = False) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "css").mkdir(exist_ok=True)
    if not qna_only:
        write_notes_pages()
    write_qna_pages()


if __name__ == "__main__":
    import sys

    main(qna_only="--qna-only" in sys.argv)
