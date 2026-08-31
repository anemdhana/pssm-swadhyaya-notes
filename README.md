# pssm-swadhyaya-notes

Static notes for PSSM swadhyaya. GitHub Pages serves the **repository root**, so day pages keep the `swasa_maha_vidya/` path in the URL.

## Site layout

```text
swasa_maha_vidya/
  index.html
  day-01.html … day-11.html
  bonus.html
  css/site.css
```

## Live URLs

- https://anemdhana.github.io/pssm-swadhyaya-notes/swasa_maha_vidya/
- https://anemdhana.github.io/pssm-swadhyaya-notes/swasa_maha_vidya/day-01.html

Pages source: **Deploy from a branch** → `main` → `/ (root)`. Do not set the published folder to `swasa_maha_vidya`, or the extra path segment will disappear.

## Rebuild from Blogger HTML

```text
python scripts/build_swasa_static_site.py
```

Source folder: `C:\Users\dhana\Downloads\Swasa_Maha_Vidya_All_Days_Expanded_QA_Blogger`
