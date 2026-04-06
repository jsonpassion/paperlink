"""Inline papers.json into index.html for deployment.

Usage:
    python build.py
    python build.py --input my_papers.json
    python build.py --output dist/index.html

The script embeds papers.json as window.__PG_DATA__ inside the HTML,
so GitHub Pages serves a single file with no external data fetch.
"""

import argparse
import json
import re
from pathlib import Path

START_MARKER = "<!-- @PG_INLINE_DATA_START -->"
END_MARKER = "<!-- @PG_INLINE_DATA_END -->"


def build(src_json: Path, src_html: Path, out_html: Path):
    if not src_html.exists():
        raise FileNotFoundError(f"Missing: {src_html}")
    if not src_json.exists():
        raise FileNotFoundError(f"Missing: {src_json}")

    html = src_html.read_text()
    data = json.loads(src_json.read_text())

    data_json = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    data_json = data_json.replace("</script>", "<\\/script>")

    new_block = (
        f"{START_MARKER}\n"
        f'<script id="__pg_inline_data__">window.__PG_DATA__={data_json};</script>\n'
        f"{END_MARKER}"
    )

    pattern = re.compile(
        re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER),
        re.DOTALL,
    )
    if not pattern.search(html):
        raise RuntimeError(f"Inline markers not found in {src_html}.")

    html_out = pattern.sub(new_block, html)
    out_html.parent.mkdir(parents=True, exist_ok=True)
    out_html.write_text(html_out)

    size_kb = len(html_out) / 1024
    data_kb = len(data_json) / 1024
    print(
        f"Built {out_html}  "
        f"({size_kb:.1f} KB total, {data_kb:.1f} KB inlined data, "
        f"{len(data.get('papers', []))} papers, {len(data.get('edges', []))} edges)"
    )


def main():
    parser = argparse.ArgumentParser(description="Inline papers.json into index.html")
    parser.add_argument("--input", default="papers.json", help="Path to papers JSON (default: papers.json)")
    parser.add_argument("--output", default="dist/index.html", help="Output HTML path (default: dist/index.html)")
    args = parser.parse_args()

    root = Path(__file__).parent
    build(
        src_json=Path(args.input) if Path(args.input).is_absolute() else root / args.input,
        src_html=root / "index.html",
        out_html=Path(args.output) if Path(args.output).is_absolute() else root / args.output,
    )


if __name__ == "__main__":
    main()
