from general_settings import *
from tests_settings import *
from users_settings import *
from debug_toolbar_settings import *

try:
    from local_settings import *
except ImportError:
    pass
