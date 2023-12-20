import sys, os

sys.path.append(os.path.abspath(".."))

extensions = [
    "sphinxcontrib.phpdomain",
    "myst_parser",
]

myst_enable_extensions = ["colon_fence"]

source_suffix = ".md"
master_doc = "index"

exclude_patterns = ["_build", "logging.md"]

html_theme = "default"
