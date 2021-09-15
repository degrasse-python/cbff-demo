#!/usr/bin/env python
"""
Copyright (c) 2021
"""

import os
import sys
import csv

from rox.server.rox_server import Rox

from core.flags import (Flags,
                            ROLLOUT_ENV_KEY)
# from app.models import Orders

flags = Flags()
  
def main():

  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
  try:
    from django.core.management import execute_from_command_line
  except ImportError as exc:
    raise ImportError(
        "Couldn't import Django. Are you sure it's installed and "
        "available on your PYTHONPATH environment variable? Did you "
        "forget to activate a virtual environment?"
        ) from exc

  # Setup Feature Management SDK
  try:
    # Register the flags container
    Rox.register('Production', flags)
    print("Feature Management Flags Registered")
    # Setup the environment key
    cancel_event = Rox.setup(ROLLOUT_ENV_KEY, flags.options).result()
    print("Feature Management Setup - Starting Server")
    execute_from_command_line(sys.argv)
  except Exception as e:
    print('%s (%s)' % (e, type(e)))
    try:
      Rox.shutdown()
    except Exception as e:
      print('%s (%s)' % (e, type(e)))

      # execute server init  
      execute_from_command_line(sys.argv)

if __name__ == '__main__':
  main()


