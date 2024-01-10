import os

from split_settings.tools import include

MODE_SETTINGS = os.environ.get('MODE_SETTINGS', 'development')

include(
    'base.py',
    MODE_SETTINGS + '.py',
    'logging.py',
)
