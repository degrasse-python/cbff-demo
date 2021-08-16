# Import Cloudbees SDK
from rox.server.rox_server import Rox
from rox.server.flags.rox_flag import RoxFlag
from rox.core.entities.rox_string import RoxString
from rox.core.entities.rox_int import RoxInt
from rox.core.entities.rox_double import RoxDouble

ROLLOUT_ENV_KEY ="60fef08497b721ffee72cea8"

# Create Roxflags in the Flags container class
class Flags:
  def __init__(self):
    #Define the feature flags
    self.enableCustomersKPI = RoxFlag(False)
    # list of all dashboard options - here we give the engn team the option to revert
    self.enableLineGraph = RoxString('is-newversion', ['is-revert', 'is-newversion'])
    self.enableRevenueKPI =  RoxFlag(False)
    # enableLineGraph =  Rox.Flag(False),
    self.enableNewTaskButton =  RoxFlag(False)
    