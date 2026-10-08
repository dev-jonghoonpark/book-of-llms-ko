"""content.md를 template.html에 넣어 index.html을 만든다. (python3 build.py)"""
from pathlib import Path

root = Path(__file__).parent
md = (root / "content.md").read_text()
assert "</script" not in md.lower()
html = (root / "template.html").read_text()
html = html.replace("SNAPSHOT_DATE", "2026-10-09").replace("__CONTENT__", md)
(root / "index.html").write_text(html)
print("index.html", len(html))
