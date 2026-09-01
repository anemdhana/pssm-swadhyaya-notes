# pssm-swadhyaya-notes

Static notes for PSSM swadhyaya. GitHub Pages serves the **repository root**.

## Site layout

```text
swasa_maha_vidya/
  index.html
  day-01.html … day-11.html, bonus.html   # full teaching notes
  qna/
    index.html
    day-01.html … bonus.html              # Q&A
  css/site.css

21-Day-Meditation-with-Music-PMMA/
  index.html
  day-01.html … day-21.html
  css/site.css

patriji_teachings/
  index.html
  difficult-family-members.html
  css/site.css

person-transformation-journey/
  index.html
  vishwa-raiyani-life-changing-experience.html
  css/site.css
```

## Live URLs

- Notes: https://anemdhana.github.io/pssm-swadhyaya-notes/swasa_maha_vidya/day-01.html
- Q&A: https://anemdhana.github.io/pssm-swadhyaya-notes/swasa_maha_vidya/qna/day-01.html
- PMMA 21-day: https://anemdhana.github.io/pssm-swadhyaya-notes/21-Day-Meditation-with-Music-PMMA/day-01.html
- Patriji: https://anemdhana.github.io/pssm-swadhyaya-notes/patriji_teachings/difficult-family-members.html
- Transformation journeys: https://anemdhana.github.io/pssm-swadhyaya-notes/person-transformation-journey/vishwa-raiyani-life-changing-experience.html

Pages source: **Deploy from a branch** → `main` → `/ (root)`.

## Rebuild

```text
python scripts/build_swasa_static_site.py
python scripts/build_pmma_21day_static_site.py
```

Notes source: `C:\Users\dhana\Downloads\Swasa_Maha_Vidya_All_Days_1-12_Full_Enhanced`  
Q&A source: `C:\Users\dhana\Downloads\Swasa_Maha_Vidya_All_Days_Expanded_QA_Blogger`  
PMMA source: `C:\Users\dhana\Downloads\21-Day-Meditation-with-Music-PMMA\21-day-meditation`
