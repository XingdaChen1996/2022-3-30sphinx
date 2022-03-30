'''基础配置
'''

from pathlib import Path
import sys
import ablog

if sys.platform == 'win32':
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

extensions = [
    "ablog",
    "myst_nb",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx_thebe",
    "sphinx_copybutton",
    "sphinx_comments",
    "sphinxcontrib.mermaid",
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.napoleon',
    # "sphinx.ext.todo",
    # "sphinxcontrib.bibtex",
    # "sphinx_togglebutton",
    # "sphinx.ext.viewcode",
    # "sphinx.ext.autodoc",
    # "sphinx.ext.doctest",
    # "sphinx_design",
    # "sphinx.ext.ifconfig",
    # "sphinx_automodapi.automodapi",
    # "sphinxext.opengraph",
]

myst_enable_extensions = [
    "colon_fence",
    "amsmath",
    "deflist",
    "dollarmath",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
    # "linkify",
]

# MyST NB 设置
nb_render_priority = {
    "html": (
        "application/vnd.jupyter.widget-view+json",
        "application/javascript",
        "text/html",
        "image/svg+xml",
        "image/png",
        "image/jpeg",
        "text/markdown",
        "text/latex",
        "text/plain",
    ),
    'gettext': ()
}

ROOT = Path(__file__).parent.absolute().as_posix()
# Add any paths that contain templates here, relative to this directory.
templates_path = [f'{ROOT}/_templates', ablog.get_html_templates_path()]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = [f'{ROOT}/_static']
html_css_files = ["default.css"]

# -- 国际化输出 ----------------------------------------------------------------
gettext_compact = False  # optional.
locale_dirs = [f'{ROOT}/locales/']

# -- 主题设置 -------------------------------------------------------------------

# 定制主侧栏
html_sidebars = {
    "*": [
        # 显示标志和网站标题。
        "sidebar-logo.html",
        #一个基于 bootstrap 的搜索栏（来自 PyData Sphinx Theme）
        "search-field.html",
        # 一个用于你的书基于 bootstrap 的导航菜单。
        "sbt-sidebar-nav.html",
        # 一个 可配置的 HTML 片段，用于添加到侧边栏（默认情况下，它被放置在底部）。
        "sbt-sidebar-footer.html",
    ],
    "posts/**": [
        "postcard.html",
        "recentposts.html",
        "tagcloud.html",
        "categories.html",
        "archives.html",
    ],
}

extra_navbar = """<div>
版权所有 © 2021 <a href="https://xinetzone.github.io/">xinetzone</a></div>
<div>由 <a href="https://ebp.jupyterbook.org/">EBP</a> 提供技术支持</div>
"""

html_theme_options = {
    # -- 如果你的文档只有一个页面，而且你不需要左边的导航栏，那么 ---------------
    # 你可以在 单页模式 下运行，
    # "single_page": False,  # 默认 `False`
    # -- 在导航栏添加一个按钮，链接到版本库的议题 ------------------------------
    # （与 `repository_url` 和 `repository_branch` 一起使用）
    "use_issues_button": True,  # 默认 `False`
    # -- 在导航栏添加一个按钮，以下载页面的源文件。
    "use_download_button": True,  # 默认 `True`
    # 你可以在每个页面添加一个按钮，允许用户直接编辑页面文本，
    # 并提交拉动请求以更新文档。
    "use_edit_page_button": True,
    # 在导航栏添加一个按钮来切换全屏的模式。
    "use_fullscreen_button": True,  # 默认 `True`
    # -- 在导航栏中添加一个链接到文档库的按钮。----------------------------------
    "use_repository_button": True,  # 默认 `False`
    # -- 包含从 Jupyter 笔记本建立页面的 Binder 启动按钮。 ---------------------
    # "launch_buttons": '', # 默认 `False`
    "home_page_in_toc": False,  # 是否将主页放在导航栏（顶部）
    # -- 只显示标识，不显示 `html_title`，如果它存在的话。-----
    # "logo_only": True,
    # -- 在导航栏中显示子目录，向下到这里列出的深度。 ----
    # "show_navbar_depth": 2,
    # -- 在侧边栏页脚添加额外的 HTML -------------------
    # （如果 `sbt-sidebar-footer.html `在 `html_sidebars` 中被使用）。
    "extra_navbar": extra_navbar,
    # -- 在每个页面的页脚添加额外的 HTML。---
    # "extra_footer": '',
    # （仅限开发人员）触发一些功能，使开发主题更容易。
    # "theme_dev_mode": False
    # 重命名页内目录名称
    "toc_title": "导航",
    "launch_buttons": {
        # https://mybinder.org/v2/gh/xinetzone/sphinx-demo/main
        "binderhub_url": "https://mybinder.org",
        # "jupyterhub_url": "https://datahub.berkeley.edu",  # For testing
        "colab_url": "https://colab.research.google.com/",
        # 你可以控制有人点击启动按钮时打开的界面。
        "notebook_interface": "jupyterlab",
        "thebe": True,  # Thebe 实时代码单元格
    },
}
# -- 自定义网站的标志 --------------
html_logo = f'{ROOT}/logo.jpg'
# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = f'{ROOT}/page-logo.jfif'

# -- 自定义网站的标题 --------------
# html_title = '动手学习 Python'

# ========== ABlog 配置 ============================================================
blog_path = "posts"
blog_post_pattern = "posts/*.md"
fontawesome_included = True
post_auto_image = 1
post_auto_excerpt = 2
bibtex_reference_style = "author_year"
# --    博客作者、语言和位置 -------------------------------------------------
# 语言代码名称的字典，映射到这些语言的完整显示名称和链接。
# 类似于 :confval:`blog_authors`，
# 字典的键应该在 `post` 指令中使用，以指代位置。默认是 `{}`。
blog_languages = {'zh': ('Chinese', None), 'en': ('English', None)}

# 在 blog_locations 中定义的默认位置的名称。
# blog_default_location = None

# -- 博客帖子相关 --------------------------------------------------------

# 帖子的日期格式。默认 ``'%b %d, %Y'``
#  ``datetime.date.strftime()`` 的参数
post_date_format = '%c'
post_date_format_short = '%b %d, %Y'

# todo_include_todos = True

# 如果你希望stderr和stdout中的每个输出都被合并成一个流，请使用以下配置。
# 避免将 jupter 执行报错的信息输出到 cmd
nb_merge_streams = True
execution_allow_errors = True
jupyter_execute_notebooks = "cache"

epub_show_urls = 'footnote'

# Napoleon 设置
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = True
napoleon_type_aliases = None
napoleon_attr_annotations = True
