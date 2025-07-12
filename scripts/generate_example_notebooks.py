from pathlib import Path
import mkdocs_gen_files

nav = mkdocs_gen_files.Nav()
root = Path(__file__).parent.parent
docs = root / "docs"
EXAMPLE_NOTEBOOKS = "example_notebooks"
example_notebooks = docs / EXAMPLE_NOTEBOOKS

for path in sorted(example_notebooks.glob("*.ipynb")):
    name = path.stem.title()
    rel_path = path.relative_to(example_notebooks)
    nav[(name, )] = rel_path.as_posix()

with mkdocs_gen_files.open(f"{EXAMPLE_NOTEBOOKS}/SUMMARY.md", "w") as nav_file:  
    nav_file.writelines(nav.build_literate_nav())
