# pssm-swadhyaya-notes

Static notes for PSSM swadhyaya. HTML is meant to be viewed on GitHub Pages, not as raw files on github.com.

## Site layout

```text
swasa_maha_vidya/
  index.html
  day-01.html … day-11.html
  bonus.html
  css/site.css
```

## Live URL (after Pages is enabled)

- https://anemdhana.github.io/pssm-swadhyaya-notes/
- https://anemdhana.github.io/pssm-swadhyaya-notes/day-01.html

## Enable GitHub Pages (once)

1. Repo **Settings → Pages**
2. Source: **GitHub Actions**
3. Push to `main`, or run the **Deploy GitHub Pages** workflow

## Rebuild from Blogger HTML

```text
python scripts/build_swasa_static_site.py
```

Source folder: `C:\Users\dhana\Downloads\Swasa_Maha_Vidya_All_Days_Expanded_QA_Blogger`
