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
    # Rox.fetch()
    # print("Fetch called to Feature Management dashboard")
     

  execute_from_command_line(sys.argv)


  # execute server init 
  
if __name__ == '__main__':
  main()


