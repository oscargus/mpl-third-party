import datetime

project = "mpl-third-party"
author = "matplotlib developers"

project = "Matplotlib third-party packages"
copyright = (
     f"2012 - {datetime.datetime.now().year} The Matplotlib development team"
 )

source_suffix = ['.rst']

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "mpl_sphinx_theme"
html_static_path = ["./_static"]
html_theme_options = {
    "logo": {
        "link": "https://matplotlib.org/stable",
        "image_light": "images/logo2.svg",
        "image_dark": "images/logo_dark.svg",
    },
    "navbar_links": "internal",
    "page_sidebar_items": "page-toc.html",
}

html_css_files = [
    "custom.css",
]

html_sidebars = {
    '**': ['localtoc.html']
}
