import datetime
import os
import sys

import sphinx_rtd_theme  # noqa: F401

import snadra

snadra_root = os.path.dirname(snadra.__file__)
sys.path.insert(0, snadra_root)

SRC_PATH = os.path.dirname(snadra_root)


project = "snadra"
author = "ShaharNaveh"
copyright = f"2020-{datetime.datetime.now().year}, {author}"
version = snadra.__version__
release = version

exclude_patterns = []

extensions = [
    "autoapi.extension",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints",
    "sphinx_rtd_theme",
]

intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}

templates_path = ["_templates"]


html_theme = "sphinx_rtd_theme"
html_sidebars = {
    "**": [
        "about.html",
        "searchbox.html",
        "localtoc.html",
        "relations.html",
    ]
}

_html_theme_options_toc = {
    "collapse_navigation": True,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
}

_html_theme_options_misc = {
    "display_version": True,
    "prev_next_buttons_location": "bottom",
    "style_nav_header_background": "#2980B9",
    # "vcs_pageview_mode": "" # Can be {blob, view}
}

html_theme_options = {}
html_theme_options.update(_html_theme_options_toc)
html_theme_options.update(_html_theme_options_misc)

html_static_path = ["_static"]

html_show_sourcelink = False

# autoapi.extension
autoapi_type = "python"
autoapi_dirs = [SRC_PATH]
autoapi_member_order = "groupwise"
autoapi_keep_files = True
autoapi_template_dir = "_templates/_autoapi_templates"

# sphinx.ext.autosummary
autosummary_generate = True

# sphinx.ext.autodoc
autodoc_typehints = "description"
autoclass_content = "both"
autodoc_member_order = "groupwise"
autodoc_inherit_docstrings = True

# sphinx_autodoc_typehints
set_type_checking_flag = True
typehints_fully_qualified = True
