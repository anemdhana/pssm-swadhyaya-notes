# pssm-swadhyaya-notes

Static notes for PSSM swadhyaya. GitHub Pages serves the **repository root**.

**Live site:** https://anemdhana.github.io/pssm-swadhyaya-notes/

## Layout

```text
index.html                          # site hub
css/site.css                        # global theme (single stylesheet)

DrNewton/swasa_maha_vidya/
  index.html, day-01…11, bonus.html
  qna/ …

Session-Schedules/21-Day-Meditation-with-Music-PMMA/
  index.html, day-01…21

BrahmarshiPatriji/
BrahmarshiPremnath/
Transformation-Journeys/
Book-Reading-Notes/
Ramtha/
```

## Notable URLs

- Hub: https://anemdhana.github.io/pssm-swadhyaya-notes/
- Swasa notes: …/DrNewton/swasa_maha_vidya/day-01.html
- Swasa Q&A: …/DrNewton/swasa_maha_vidya/qna/day-01.html
- PMMA 21-day: …/Session-Schedules/21-Day-Meditation-with-Music-PMMA/day-01.html

Pages source: **Deploy from a branch** → `main` → `/ (root)`.

## Rebuild (local)

```text
python scripts/build_swasa_static_site.py
python scripts/build_pmma_21day_static_site.py
```

Build scripts write under the folder names above and link to the global `css/site.css`.
