# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021

"""

import os

from django.core.asgi import get_asgi_application
from rox.server.rox_server import Rox

from .flags import (Flags,
                            ROLLOUT_ENV_KEY)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_asgi_application()

if Flags:
  flags = Flags()
  # Register the flags container
  Rox.register(flags)
  # Setup the environment key
  cancel_event = Rox.setup(ROLLOUT_ENV_KEY).result()
  print('enableCustomersKPI is {}'.format(flags.enableCustomersKPI.is_enabled()))

else:
  pass