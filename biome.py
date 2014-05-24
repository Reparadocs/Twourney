import constants, random

class EnvType():
  SAND = 0
  FOREST = 1
  MOUNTAIN = 2
  WATER = 3
  SWAMP = 4
  NumBiomes = 5

class Cell(object):
  x = -1
  y = -1
  env = -1
  description = ""

  def getDescription(self,env):
    return {
      0: u"You are in sand",
      1: u"You are in forest",
      2: u"You are in mountain",
      3: u"You are in water",
      4: u"You are in swamp",
    }[env]

  def __str__(self):
    return str(self.env)

  def __repr__(self):
    return str(self.env)

  def __init__(self, x, y, env):
    self.x = x
    self.y = y
    self.env = env
    self.description = self.getDescription(env)

biome_map = [[-1]*constants.MAP_SIZE_Y for i in range(constants.MAP_SIZE_X)]
def fillSurroundingTiles(i,j,e):
  if (i-1) >= 0:
    if biome_map[i-1][j] == -1:
      biome_map[i-1][j] = e
  if (i+1) < len(biome_map):
    if biome_map[i+1][j] == -1:
      biome_map[i+1][j] = e
  if (j-1) >= 0:
    if biome_map[i][j-1] == -1:
      biome_map[i][j-1] = e
  if (j+1) < len(biome_map[0]):
    if biome_map[i][j+1] == -1:
      biome_map[i][j+1] = e

def setupMap():
  global biome_map
  map_area = constants.MAP_SIZE_Y * constants.MAP_SIZE_X
  num_biomes = random.randint(int(map_area*0.1), int(map_area*0.15))
  for k in range(num_biomes):
    px = random.randint(0,constants.MAP_SIZE_X-1)
    py = random.randint(0,constants.MAP_SIZE_X-1)
    biome_map[px][py] = random.randint(0,EnvType.NumBiomes-1)

  while True:
    map_incomplete=False
    for i in range(constants.MAP_SIZE_X):
      for j in range(constants.MAP_SIZE_Y):
        e = biome_map[i][j]
        if e == -1:
          map_incomplete = True
        else:
          fillSurroundingTiles(i,j,e) 
    if not map_incomplete:
      break

def cellMap(seed=None):
  cell_map = [[None]*constants.MAP_SIZE_Y for i in range(constants.MAP_SIZE_X)]
  if seed is not None:
    random.seed(seed)
  setupMap()
  for i in range(constants.MAP_SIZE_X):
    for j in range(constants.MAP_SIZE_Y):
      cell_map[i][j] = Cell(i,j,biome_map[i][j])
  return cell_map

