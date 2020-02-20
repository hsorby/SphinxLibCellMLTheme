LibCellML Sphinx Theme
======================

.. image:: https://badge.fury.io/py/sphinx_libcellml_theme.svg
    :target: http://badge.fury.io/py/sphinx_libcellml_theme
    :alt: Badge not found

.. contents::


`libCellML theme <https://github.com/hsorby/SphinxLibCellMLTheme>`_ is a simple `Sphinx <http://sphinx-doc.org/>`_ theme.

Installation
-------------

Via package
~~~~~~~~~~~~

1. Installing from PyPI::

    $ pip install sphinx_libcellml_theme

2. Edit the Sphinx configuration file ``conf.py`` ::

    # At the top.
    import sphinx_libcellml_theme

    # ...

    html_theme = "sphinx_libcellml_theme"

    html_theme_path = [sphinx_libcellml_theme.get_html_theme_path()]


Via git or download
~~~~~~~~~~~~~~~~~~~~

1. Copy ``sphinx_libcellml_theme/sphinx_libcellml_theme`` from repository into your documentation at ``_templates`` folder.

2. Edit the Sphinx configuration file ``conf.py`` ::

    # ...

    html_theme = "sphinx_libcellml_theme"

    html_theme_path = ["_templates"]


License
--------

The code is licensed under the `Apache License <https://github.com/hsorby/SphinxLibCellMLTheme/blob/master/LICENSE>`_
while documents are licensed under the `CC-BY License <https://creativecommons.org/licenses/by/4.0/>`_.
