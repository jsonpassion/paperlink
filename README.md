# Paper Galaxy Template

> Turn any collection of research papers into an interactive 3D galaxy visualization.

<p align="center">
  <img src="https://img.shields.io/badge/Three.js-black?logo=three.js" alt="Three.js">
  <img src="https://img.shields.io/badge/Zero_Dependencies-green" alt="Zero Dependencies">
  <img src="https://img.shields.io/badge/Single_HTML-blue" alt="Single HTML">
  <img src="https://img.shields.io/github/license/jsonpassion/papergoat-galaxy-template" alt="MIT License">
</p>

<p align="center">
  <a href="https://jsonpassion.github.io/papergoat-galaxy/">Live Demo (PaperGoat Galaxy)</a> ·
  <a href="https://jsonpassion.github.io/papergoat-apple/">Live Demo (Apple ML)</a>
</p>

---

## Features

- **3D Interactive Globe** — Papers as glowing nodes on a sphere, edges as curved lineage arcs
- **Click & Explore** — Click any node for details, Shift+Click for multi-select
- **Filter & Search** — Filter by category, year, score; full-text search
- **Dark / Light Mode** — Automatic system preference detection
- **Bilingual (EN/KR)** — Built-in i18n with one-click toggle
- **Responsive** — Desktop, tablet, and mobile optimized
- **Single HTML** — No server, no build tools required for basic usage
- **GitHub Pages Ready** — Deploy in 2 minutes

---

## Quick Start

### Option A: Fork & Deploy (2 min)

1. **Fork this repository** — Click the "Fork" button above
2. **Enable GitHub Pages** — Go to Settings > Pages > Source: `main` / `root`
3. **Done!** — Your galaxy is live at `https://<your-username>.github.io/papergoat-galaxy-template/`

The template ships with 20 sample papers. Edit `papers.json` to add your own.

### Option B: Local Development

```bash
# Clone
git clone https://github.com/jsonpassion/papergoat-galaxy-template.git
cd papergoat-galaxy-template

# Copy sample data
cp papers.sample.json papers.json

# Open in browser (any local server works)
python -m http.server 8000
# → http://localhost:8000
```

---

## Customizing Your Data

### Step 1: Edit `papers.json`

Each paper needs these fields:

```json
{
  "id": "unique-id",
  "rank": 1,
  "alias": "Short Name",
  "title": "Full Paper Title",
  "url": "https://arxiv.org/abs/...",
  "year": 2024,
  "score": 95,
  "categories": ["LLM", "Scaling"],
  "cluster": "llm",
  "reason": "Why this paper matters (shown in detail panel)",
  "has_review": false,
  "one_liner": "",
  "key_discoveries": [],
  "review_url": "",
  "reason_en": "English version of reason"
}
```

### Step 2: Define Edges (Paper Lineage)

Edges show relationships between papers:

```json
{
  "edges": [
    {"source": "paper-A", "target": "paper-B", "type": "lineage"}
  ]
}
```

### Step 3: Customize Clusters

Clusters define the color-coded categories. Customize them in the `clusters` section:

```json
{
  "clusters": {
    "llm":        {"label": "LLM",          "color": "#3b82f6", "icon": "🧠"},
    "vision":     {"label": "Vision",       "color": "#10b981", "icon": "👁️"},
    "generation": {"label": "Generation",   "color": "#f59e0b", "icon": "🎨"}
  }
}
```

### Step 4: Build for Production (Optional)

To inline data into a single HTML file for deployment:

```bash
python build.py
# → dist/index.html (single file, no external data fetch)
```

Options:
```bash
python build.py --input my_custom_data.json
python build.py --output build/index.html
```

---

## Scoring Rubric

Papers are sized proportionally to their `score` (80–100 range). The default scoring criteria:

| Weight | Criterion | Description |
|--------|-----------|-------------|
| 25% | Paradigm Shift | Did it open a new research direction? |
| 25% | Adoption | Real-world industry usage |
| 20% | Citation | Downstream research impact |
| 15% | Novelty | Technical originality |
| 15% | Timeliness | Current relevance |

---

## Project Structure

```
papergoat-galaxy-template/
├── index.html              ← Visualization engine (Three.js)
├── papers.json             ← Your paper data (gitignored in production)
├── papers.sample.json      ← Sample data with 20 mock papers
├── build.py                ← Inline papers.json into HTML for deployment
├── dist/
│   └── index.html          ← Production build (after running build.py)
├── LICENSE                 ← MIT
└── README.md
```

---

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `ESC` | Reset selection & filters |
| `Shift + Click` | Multi-select nodes |
| `Scroll` | Zoom in/out |
| `Drag` | Rotate globe |

---

## Live Examples

These sites are built with the same engine:

- **[PaperGoat Galaxy](https://jsonpassion.github.io/papergoat-galaxy/)** — Top 151 AI papers, curated & ranked
- **[PaperGoat Apple](https://jsonpassion.github.io/papergoat-apple/)** — Top 100 Apple ML research papers

---

## License

MIT License. See [LICENSE](LICENSE) for details.

Built by [Jason Lee](https://www.linkedin.com/in/json-lee) as part of the [PaperGoat](https://papergoat.beehiiv.com/) project.

If you find this useful, a star would be appreciated!
