# RepairIt SEO Site

> Affiliate promotional site for Wondershare Repairit — AI-powered repair for corrupted videos, photos, documents and audio.

**Live site:** https://brightlane.github.io/itunerepair/

---

## What This Repo Does

A single Python build script (`build.py`) generates a complete file repair affiliate site into `dist/`. The workflow automatically cleans all old files from the repo, then deploys the new site.

```
build.py   ←  the only file you need to edit or commit
```

---

## Quick Start

### Repo needs:

```
itunerepair/
├── build.py
├── README.md
└── .github/
    └── workflows/
        └── deploy.yml
```

### Enable GitHub Pages

1. **Settings → Pages → Source: GitHub Actions**

### Run the workflow

**Actions → Build & Deploy RepairIt → Run workflow**

Old files deleted automatically. Site live at **https://brightlane.github.io/itunerepair/**

---

## What Gets Built

| Content | Count |
|---|---|
| Essential pages | 11 |
| Keyword-targeted pages | 167 |
| Blog posts | 12 |
| Total files | ~1,855 |
| Total size | ~50 MB |

### Essential Pages

| File | Description |
|---|---|
| `index.html` | Homepage — 8-repair-type hub, features, causes |
| `features.html` | Full feature list with comparison table |
| `how-it-works.html` | 3-step guide + Quick vs Advanced Repair |
| `faq.html` | 18 FAQs with FAQPage schema |
| `compare.html` | vs Stellar, Kernel, online tools |
| `blog.html` | Blog index — 12 full articles |
| `download.html` | Download CTA with system requirements |
| `keywords.html` | All 167 topics by category |
| `glossary.html` | 25 file repair terms defined |
| `privacy.html` | Privacy policy + affiliate disclosure |
| `404.html` | Branded 404 with auto-redirect |

### Blog Posts (in `blog/`)

1. How to Repair a Corrupted MP4 File
2. How to Repair Corrupted Photos (JPEG, RAW, PNG)
3. How to Repair a Corrupted Word Document
4. How to Repair a Corrupted Excel File
5. Repair Corrupted GoPro Video Files
6. Repair Corrupted Drone Video Footage
7. How to Repair a Corrupted PSD File
8. Fix Audio Files That Won't Play
9. How to Use AI Video Enhancer
10. How to Repair a Corrupted PDF
11. Best File Repair Software 2025 — Ranked
12. Fix Video Files Corrupted by Power Failure

### Keyword Categories (12)

`brand` · `video` · `photo` · `document` · `audio` · `cause` · `platform` · `compare` · `howto` · `global` · `business` · `ai`

---

## Config at the top of `build.py`

```python
AFFILIATE_URL = "https://www.linkconnector.com/ta.php?lc=007949095044004532&atid=itunerepairwebs"
SITE_DOMAIN   = "https://brightlane.github.io/itunerepair"
BASE_PATH     = "/itunerepair"
```

---

## Affiliate Disclosure

All links use `rel="nofollow sponsored"`. Disclosure in footer and privacy page.

Repairit is a product of Wondershare Technology Co., Ltd.
