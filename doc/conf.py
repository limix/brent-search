import time


def _get_version():
    import brent_search

    return brent_search.__version__


def _get_name():
    import brent_search

    return brent_search.__name__


extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
]

napoleon_numpy_docstring = True
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
project = _get_name()
copyright = "2018, Danilo Horta"
author = "Danilo Horta"
version = _get_version()
release = version
today = time.strftime("%B %d, %Y")
language = "en"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "conf.py"]
pygments_style = "default"
todo_include_todos = False
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "logo_only": False,
    "display_version": True,
    "style_external_links": True,
}
highlight_language = "python3"
html_sidebars = {"**": ["relations.html", "searchbox.html"]}
htmlhelp_basename = "{}doc".format(project)
autodoc_default_flags = ["members"]
autosummary_generate = True
