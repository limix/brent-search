from __future__ import unicode_literals

import re
from importlib import import_module
from os import getenv
from os.path import dirname, join, realpath
from time import strftime

import sphinx_rtd_theme

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser


def get_metadata():
    config = ConfigParser()
    config.read('setup.cfg')
    return dict(config.items('metadata'))


def get_init_metadata(expr):
    metadata = get_metadata()
    prjname = metadata['packages'][0]
    data = open(join(prjname, "__init__.py")).read()
    return re.search(expr, data).group(1)


def get_version(metadata):
    return get_init_metadata(re.compile(r"__version__ *= *\"(.*)\""))


def get_author(metadata):
    return get_init_metadata(re.compile(r"__author__ *= *\"(.*)\""))


def get_name(metadata):
    return get_init_metadata(re.compile(r"__name__ *= *\"(.*)\""))


if getenv("READTHEDOCS", "False") == "True":

    prjname = getenv("READTHEDOCS_PROJECT", "unknown")
    pkgname = prjname.replace("-", "_")
    pkg = import_module(pkgname)

    project = pkg.__name__
    version = pkg.__version__
    author = pkg.__author__
else:
    project = metadata['name']
    version = metadata['version']
    author = metadata['author']

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]
napoleon_google_docstring = True
master_doc = 'index'
copyright = '%s, %s' % (strftime("%Y"), author)
release = version
language = "en"
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'conf.py']
pygments_style = 'sphinx'
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
intersphinx_mapping = {
    'python': ('http://docs.python.org/', None),
    'numpy': ('http://docs.scipy.org/doc/numpy/', None)
}
