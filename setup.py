# -*- coding: utf-8 -*-
"""`sphinx_libcellml_theme` on `Github`_.

.. _github: https://github.com/hsorby/SphinxLibCellMLTheme

"""
import os
import re
import codecs

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name="sphinx_libcellml_theme",
    version=find_version("src", "sphinx_libcellml_theme", "__init__.py"),
    url="https://github.com/hsorby/SphinxLibCellMLTheme.",
    license="Apache 2.0",
    author="libCellML Contributors",
    author_email="authors@libcellml.com",
    description="A simple Sphinx theme for libCellML.",
    long_description=open("README.rst").read(),
    zip_safe=False,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'sphinx.html_themes': [
            'libcellml-theme = sphinx_libcellml_theme',
        ]
    },
    package_data={"sphinx_libcellml_theme": [
        "theme.conf",
        "*.html",
        "includes/*.html",
        "static/*.css",
        "static/*.js",
        "static/*.jpg",
        "static/fonts/*.*"
    ]},
    include_package_data=True,
    install_requires=open("requirements.txt").read().splitlines(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
