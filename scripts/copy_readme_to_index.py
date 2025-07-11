from pathlib import Path
import mkdocs_gen_files

root = Path(__file__).parent.parent
docs = root / "docs"
readme_src = root / "README.md"

if readme_src.exists():
    with mkdocs_gen_files.open(docs / "index.md", "w") as f:
        f.write(readme_src.read_text())
