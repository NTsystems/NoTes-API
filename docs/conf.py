# -*- coding: utf-8 -*-
import os
import sys
import sphinx_rtd_theme

sys.path.append(os.path.abspath('./../'))

# Sphinx extensions
extensions = ['sphinx.ext.autodoc']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'NoTes'
copyright = u'2015, NTsystems'

# The full version, including alpha/beta/rc tags.
release = '1.0.0'
version = release

# Ignored directories
exclude_patterns = ['_build']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Theme to use for HTML & HTML Help pages
html_theme = 'sphinx_rtd_theme'

# Theme path
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Static files path
html_static_path = ['_static']

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# Output file base name for HTML help builder.
htmlhelp_basename = 'NoTesAPIServicedoc'
