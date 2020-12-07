# Configuration file for the Sphinx documentation builder.
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
# https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# https://recommonmark.readthedocs.io/en/latest/index.html#autostructify
# https://recommonmark.readthedocs.io/en/latest/auto_structify.html
# This enables additional features of recommonmark syntax
import recommonmark
from recommonmark.transform import AutoStructify

# -- Project information -----------------------------------------------------

project = 'hledger'
author = 'Simon Michael'
copyright = '2007-2020, Simon Michael & contributors'

# version of the reference manuals (the rest of the docs aren't really versioned)
# version = '1.14'
# release = '1.14'
# version = 'latest (master)'
# release = 'latest (master)'

manuals = [
    'hledger',
    'hledger-ui',
    'hledger-web',
    'journal',
    'csv',
    'timeclock',
    'timedot',
    # old manuals
    'hledger-api',
    'manual',
]

# all hledger versions we might want to show docs for (since 1.0)
release_versions = [
    '1.20',
    '1.19',
    '1.18',
    '1.17',
    '1.16',
    '1.15',
    '1.14',
    '1.13',
    '1.12',
    '1.11',
    '1.10',
    '1.9',
    '1.5',
    '1.4',
    '1.3',
    '1.2',
    '1.1',
    '1.0',
]

version_dates = {
    '1.20': '2020-12-07',
    '1.19': '2020-09-01',
    '1.18': '2020-06-07',
    '1.17': '2020-03-01',
    '1.16': '2019-12-01',
    '1.15': '2019-09-01',
    '1.14': '2019-03-01',
    '1.13': '2019-02-01',
    '1.12': '2018-12-02',
    '1.11': '2018-09-30',
    '1.10': '2018-06-30',
    '1.9' : '2018-03-31',
    '1.5' : '2017-12-31',
    '1.4' : '2017-09-30',
    '1.3' : '2017-06-30',
    '1.2' : '2017-03-31',
    '1.1' : '2016-12-31',
    '1.0' : '2016-10-26',
}

# only these versions will be shown in the version selector
# may want to comment out all of these when previewing docs locally
show_release_versions = [
    # all versions shown on the download page (overkill):
    '1.20', # 
    '1.19', # 
    '1.18', # 
    '1.17', # 
    '1.16', # 
    '1.15', # arch, gentoo
    '1.14', # void
    '1.13',
    '1.12', # debian sid, fedora 31, fedora 32, fedora rawhide
    '1.11',
    '1.10', # debian buster, debian bullseye, ubuntu disco, fedora 30, openbsd wip
    '1.9',  # sandstorm
    '1.5',  # ubuntu cosmic, fedora 29
    '1.2',  # ubuntu bionic
    '1.0',  # debian stretch
]

# these non-shown versions will be excluded from site building, below
hide_release_versions = []
for v in release_versions:
    if v not in show_release_versions:
        hide_release_versions.append(v)

current_release_version = release_versions[0]
# dev_version = current_release_version + '.99 (dev)'

# -- Some definitions for theme templates ---------------------------------------------------

# https://docs.readthedocs.io/en/stable/development/design/theme-context.html
# Before calling sphinx-build to render your docs, Read the Docs
# injects some extra context in the templates by using the
# html_context Sphinx setting in the conf.py file. In case you want to
# access to this data from your theme, you can use it like this:
# {% if readthedocs.v1.vcs.type == 'github' %}
#     <a href="https://github.com/{{ readthedocs.v1.vcs.user }}/{{ readthedocs.v1.vcs.repo }}
#     /blob/{{ readthedocs.v1.vcs.version }}{{ readthedocs.v1.vcs.conf_py_path }}{{ pagename }}.rst">
#     Show on GitHub</a>
# {% endif %}
# see also http://www.sphinx-doc.org/en/master/templating.html#global-variables
# Don't store functions here, it causes all files to be rebuilt
html_context = {

    # "edit on github" links.
    "display_github": True,        # Integrate GitHub
    "github_user": "simonmichael", # Username
    "github_repo": "hledger_site", # Repo name
    "github_version": "master",    # Version
    "conf_py_path": "/",           # Path in the checkout to the docs root
    'theme_vcs_pageview_mode': 'edit',
    "manuals": manuals,
    'versions': show_release_versions,
    'version_dates': version_dates,
    'current_release_version': current_release_version,
    # 'dev_version': dev_version,
    # custom edit links for certain pages (the manuals). Cf _templates/breadcrumbs.html
    "special_edit_paths": {
        "journal"     : "hledger/edit/master/hledger-lib/hledger_journal.m4.md",
        "csv"         : "hledger/edit/master/hledger-lib/hledger_csv.m4.md",
        "timeclock"   : "hledger/edit/master/hledger-lib/hledger_timeclock.m4.md",
        "timedot"     : "hledger/edit/master/hledger-lib/hledger_timedot.m4.md",
        "hledger"     : "hledger/edit/master/hledger/hledger.m4.md",
        "hledger-ui"  : "hledger/edit/master/hledger-ui/hledger-ui.m4.md",
        "hledger-web" : "hledger/edit/master/hledger-web/hledger-web.m4.md",
    },

}

# -- General configuration ---------------------------------------------------

master_doc = 'sitemap'

smartquotes = False

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # https://recommonmark.readthedocs.io
    'recommonmark',
    # https://github.com/ryanfox/sphinx-markdown-tables
    # https://python-markdown.github.io/extensions/tables
    # https://michelf.ca/projects/php-markdown/extra/#table
    'sphinx_markdown_tables',
    # https://pypi.org/project/sphinx-rtd-theme/
    'sphinx_rtd_theme',
]

# needs_extensions = {
#     'recommonmark': '1.1',
#     'sphinx_markdown_tables': '2.2',
# }

# http://www.sphinx-doc.org/en/master/usage/markdown.html#configuration
# https://spec.commonmark.org
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
#    '.txt': 'markdown',
}

# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-suppress_warnings
# doesn't help, see setup below
suppress_warnings = [
    # 'ref.term',
    # 'ref.ref',
    # 'ref.numref',
    # 'ref.keyword',
    # 'ref.option',
    # 'ref.citation',
    # 'ref.footnote',
    # 'ref.doc',
    # 'ref.python',
    # 'misc.highlighting_failure',
]

# https://recommonmark.readthedocs.io/en/latest/index.html#linking-to-headings-in-other-files
# For linking to headings in other files you can use the autosectionlabel sphinx feature, e.g.
#extensions = [
#     # Auto-generate section labels.
#     'sphinx.ext.autosectionlabel',
#]
# # Prefix document path to section labels, otherwise autogenerated labels would look like 'heading'
# # rather than 'path/to/file:heading'
#autosectionlabel_prefix_document = True
# You would use it like:
#
# <!-- path/to/file_1.md -->
# # Title
# ## My Subtitle
#
# <!-- file_2.md -->
# [My Subtitle][]
# [My Subtitle]: <path/to/file_1:My Subtitle>

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    '_site',
    # exclude more things, for faster testing
    # '[A-Za-gi-z]*.md',
    # '[0-9]*',
    # '*.md',  
] + hide_release_versions   # exclude some old manuals


# A string of reStructuredText that will be included at the beginning of
# every source file that is read. This is a possible place to add
# substitutions that should be available in every file (another being rst_epilog). 
# rst_prolog = """
# .. |psf| replace:: Python Software Foundation
# """


# -- Options for HTML output -------------------------------------------------

html_extra_path = [
    # include the old manual's old html as static files
    # '_site/doc',
]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add stylesheets to HEAD
html_css_files = [
    # styles for the highslide image zoomer
    'js/highslide/highslide.css',
    # overrides for the sphinx theme
    'css/theme-overrides.css',
    # our old custom style overides
    # 'css/style.css',
]

# Add javascript files to HEAD. See also _template/layout.html.
html_js_files = [
    # bootstrap js, I think not used
    # 'js/bootstrap.min.js',
    # highslide image zoomer
    'js/highslide/highslide.js',
    # custom js, currently none
    # 'site.js',
]


# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"

html_theme_options = {
    # https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html
    # 'canonical_url': '',
    # 'analytics_id': 'UA-XXXXXXX-1',
    # 'logo_only': False,
    'display_version': False,
    # 'prev_next_buttons_location': 'bottom',
    # 'style_external_links': False,
    'style_nav_header_background': '#343131',
    # Toc options
    'sticky_navigation': True,
    # 'includehidden': True,
    # 'titles_only': False,

    # https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html#how-the-table-of-contents-displays
    # Setting collapse_navigation to False and using a high value for navigation_depth on projects with many files and a deep file structure can cause long compilation times and can result in HTML files that are significantly larger in file size.
    'collapse_navigation': True,  # hides the + button on other top-level items
    'navigation_depth': 4,

}

# https://docs.readthedocs.io/en/stable/index.html
# https://sphinx-rtd-theme.readthedocs.io/en/latest/demo/demo.html  paragraph level markup
# https://sphinx-rtd-theme.readthedocs.io/en/latest/demo/lists_tables.html  lists & tables

# html_short_title = 'hledger'
# html_baseurl = '/index.html'
# html_logo = '_static/images/coins2-248.png'
html_last_updated_fmt = ''
html_show_sphinx = False


# -- Pygments highlighting tweaks ---------------------------------------

# define some custom pygments highlighters for literal blocks
# https://stackoverflow.com/questions/16469869/custom-syntax-highlighting-with-sphinx
# http://pygments.org/docs/lexerdevelopment
# http://pygments.org/docs/tokens/

from sphinx.highlighting import lexers
from pygments.lexer import RegexLexer
from pygments.token import *

datere = r'(\d\d\d\d[.-/])?\d\d?[.-/]\d\d?'

# journal format.
class JournalLexer(RegexLexer):
    tokens = {
        'root': [
            (datere+'(='+datere+')?', Keyword.Declaration),
            (r'.*\n', Text),
        ]
    }
lexers['journal'] = lexers['{.journal}'] = JournalLexer(startinline=True)

# transcript of a shell session. lines beginning with $ are commands
class ShellLexer(RegexLexer):
    tokens = {
        'root': [
            (r'^\$ [^#\n]*', Generic.Prompt),
            (r'.*\n', Text),
        ]
    }
lexers['shell'] = lexers['{.shell}'] = ShellLexer(startinline=True)

# silence warnings about these other kinds of literal block

for l in [
    'timeclock',
    'timedot',
    'csv',
    'rules',
    'haskell',
    'hledger',
    'example',
    # still in old manuals:
    '{.shells}',
    '{.bash}',
    '{.console}',
    '{.diff}',
  ]:
    class NullLexer(RegexLexer):
        name = l
        tokens = {
            'root': [
                (r'.*\n', Text),
            ] }
    lexers[l] = lexers['{.'+l+'}'] = NullLexer(startinline=True)
lexers['{.rules .display-table}'] = NullLexer(startinline=True)


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
# man_pages = [
#     ('hledger', 'hledger', u'a command-line accounting tool',
#      [author], 1)
# ]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- app setup hook ---------------------------------------

def setup(app):

    # Sphinx gives some bogus warnings about valid references (unless the
    # file extension is removed, but then the links would work only when
    # rendered by sphinx). Silence them all here, at the cost of also
    # hiding invalid ones. (suppress_warnings above doesn't do it.)
    # https://stackoverflow.com/questions/37359407/suppress-warnings-for-unfound-references-with-default-role-any-in-sphinx
    # WARNING, watch for other side effects
    def on_missing_reference(app, env, node, contnode):
        if node['reftype'] == 'any':
            return contnode
        else:
            return None
    app.connect('missing-reference', on_missing_reference)

    # Enable AutoStructify, an optional recommonmark component providing
    # various features, in particular evaluation of RST directives.
    # https://recommonmark.readthedocs.io/en/latest/index.html#autostructify
    # default_config = {
    #     'enable_auto_doc_ref': False,
    #     'auto_toc_maxdepth': 1,
    #     'auto_toc_tree_section': None,
    #     'enable_auto_toc_tree': True,
    #     'enable_eval_rst': True,
    #     'enable_math': True,
    #     'enable_inline_math': True,
    #     'commonmark_suffixes': ['.md'],
    #     'url_resolver': lambda x: x,
    #     'known_url_schemes': None,
    # }
    app.add_config_value('recommonmark_config', {
        'enable_math':        False,
        'enable_inline_math': False,
        'enable_eval_rst':    True,
    }, True)
    app.add_transform(AutoStructify)
