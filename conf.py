#!/usr/bin/env python3
"""Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
"""
# pylint: disable=invalid-name,redefined-builtin
import zerovm_sphinx_theme

author = 'Xander Harris'
autoyaml_root = "."
autoyaml_doc_delimiter = "###"
autoyaml_comment = "#"
autoyaml_level = 10
autoyaml_safe_loader = True
copyright = '2024, Xander Harris'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    '.venv/*',
    '.tmp/*',
    '.pytest_cache/*',
    'resources/templates/NOTES.txt',
]

extensions = [
    'myst_parser',
    'sphinx_design',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.autoyaml',
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_logo = '_static/img/hr-logo.svg'
# html_favicon = '_static/img/hr-logo.svg'
html_static_path = ['_static']
html_theme = 'zerovm'
html_theme_path = [zerovm_sphinx_theme.theme_path]
myst_dmath_double_inline=True
myst_enable_extensions = [
    "amsmath",
    "attrs_block",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
myst_title_to_header = True
project = 'Generic Helm Chart'
rst_epilog = """
.. sectionauthor:: Xander Harris <xandertheharris@gmail.com>
"""
release = '0.0.1'
show_authors=True
source_suffix = {
    '.md': 'markdown',
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
}
templates_path = ['_templates']
