import sys, os

sys.path.append(os.path.abspath('..'))

extensions = [
    'sphinxcontrib.phpdomain',
]

source_suffix = '.rst'

master_doc = 'index'

exclude_patterns = ['_build']

pygments_style = 'sphinx'

html_theme = 'default'
