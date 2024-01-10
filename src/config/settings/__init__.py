import os

from split_settings.tools import include

MODE_SETTINGS = os.environ.get('MODE_SETTINGS', 'development')

if MODE_SETTINGS == 'production':
    from .production import *
else:
    from .development import *

include(
    'base.py',
    MODE_SETTINGS + '.py',
    'logging.py',
)
