# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021

"""

import os

from django.core.wsgi import get_wsgi_application
from rox.server.rox_server import Rox

from .flags import (Flags,
                    ROLLOUT_ENV_KEY)

# setup env
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
# get wsgi
application = get_wsgi_application()


