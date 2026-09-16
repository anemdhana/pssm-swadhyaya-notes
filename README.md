# pssm-swadhyaya-notes

Static notes for PSSM swadhyaya. GitHub Pages serves the **repository root**.

**Live site:** https://anemdhana.github.io/pssm-swadhyaya-notes/

## Layout

```text
index.html                          # site hub
css/site.css                        # global theme (single stylesheet)

Master-Speeches/
  DrNewton/Swasa Maha Vidya/        # teaching + qna/
  Brahmarshi Patriji/
  Brahmarshi Premnath/

Session-Schedules/
  21-Day-Meditation-with-Music-PMMA/

Transformation-Journeys/

Book-Reading-Notes/
  Soul's Journey/
  Ramtha/

collections/
  ahimsa-dhyana-mahasabha/
```

## Collections

### 1. National Ahimsa Dhyana Mahasabha
**జాతీయ అహింసా ధ్యాన మహాసభలు**

- Dates: 1-5 October
- Venue: Nampally Exhibition Grounds, Hyderabad
- Facebook: https://www.facebook.com/profile.php?id=61586315486621

Folder: `collections/ahimsa-dhyana-mahasabha/`

| Page | Language | Description |
|------|----------|-------------|
| [index.html](collections/ahimsa-dhyana-mahasabha/index.html) | Landing | Language chooser |
| ahimsa-dhyana-mahasabha-instagram.html | Telugu | Instagram-style Q&A story (Full Screen supported) |
| ahimsa-dhyana-mahasabha-instagram-en.html | English | Instagram-style Q&A story (Full Screen supported) |

Place `jadms.jpg` (event logo) in the collection folder for avatars.

## Notable URLs

- Hub: https://anemdhana.github.io/pssm-swadhyaya-notes/
- Swasa: .../Master-Speeches/DrNewton/Swasa%20Maha%20Vidya/day-01.html
- Swasa Q&A: .../Master-Speeches/DrNewton/Swasa%20Maha%20Vidya/qna/day-01.html
- PMMA 21-day: .../Session-Schedules/21-Day-Meditation-with-Music-PMMA/day-01.html

Pages source: **Deploy from a branch** -> `main` -> `/ (root)`.

On deploy, the workflow rewrites every HTML `stylesheet` link to the global `css/site.css` based on folder depth (works after reorganizations).

## Rebuild (local)

```text
python scripts/build_swasa_static_site.py
python scripts/build_pmma_21day_static_site.py
```

Update `OUT` paths in those scripts if folder names change again.
