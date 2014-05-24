from storm.locals import *
import random, constants

store = None

def setup(stormStore, seed=None):
  global store
  store = stormStore
  if seed is not None:
    random.seed(seed)

class User(object):
  __storm_table__ = "users"
  id = Int(primary=True)
  handle = Unicode()
  posX = Int()
  posY = Int()

  def __init__(self, handle, x=None, y=None):
    if x is None or y is None:
      x = random.randint(0,constants.MAP_SIZE_X-1)
      y = random.randint(0,constants.MAP_SIZE_Y-1)
    self.handle = handle
    self.posX = x
    self.posY = y
