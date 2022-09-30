# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sec Lope De Vega Project'
copyright = '2022, Sec Lope De Vega Project'
author = 'Alberto Dominguez'
release = '0.5'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']

locale_dirs = ['locale/'] 
gettext_compact = False   

exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_theme_options = {
    'logo': 'slv_logo.png',
    'logo_name': 'true',
    'font_family': "'Caslon','Georgia'",
    'code_font_size':'medium',   
    'font_size': 'x-large',
    'head_font_family': "'Caslon','Garamond', 'Georgia'", 
    'sidebar_link':'#b38600',
}
html_static_path = ['_static']
html_css_files = [
    'css-style.css',
]
