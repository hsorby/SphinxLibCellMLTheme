import os

__version__ = "0.1.0"


def get_html_theme_path():
    """Return list of HTML theme paths."""
    theme_path = os.path.abspath(os.path.dirname(__file__))
    return [theme_path]


def setup(app):
    app.add_html_theme('libcellml-theme', os.path.join(get_html_theme_path()[0], 'libcellml-theme'))
