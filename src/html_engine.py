from pathlib import Path

from jinja2 import Environment, FileSystemLoader

TEMPLATE_PATH = "templates"
TPL_NAME = "nhl_standings.html"
INDEX_NAME = "index.html"
DOC_PATH = "docs"


def build(divisions: list[str]) -> None:
    jinja = Environment(loader=FileSystemLoader(Path(TEMPLATE_PATH)))
    content = jinja.get_template(TPL_NAME).render({"divisions": divisions})
    with open(Path(DOC_PATH) / Path(INDEX_NAME), "w") as output:
        output.write(content)
