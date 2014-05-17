biome_map = [['0']*10 for i in range(10)]

environments = {"Sand":'s',
                "Forest":'f', 
                "Mountain":'m', 
                "Water":'w',
                "Swamp": 'd'}

mside = len(biome_map)

import sys
def printMap():
  for i in range(mside):
    for j in range(mside):
      sys.stdout.write(biome_map[i][j])
    print ""

def stringMap():
  strmap = ""
  for i in range(mside):
    for j in range(mside):
      strmap = strmap + biome_map[i][j]
    strmap = strmap + "\n"
  return strmap

def fillSurroundingTiles(i,j,e):
  if (i-1) >= 0:
    if biome_map[i-1][j] == '0':
      biome_map[i-1][j] = e
  if (i+1) < mside:
    if biome_map[i+1][j] == '0':
      biome_map[i+1][j] = e
  if (j-1) >= 0:
    if biome_map[i][j-1] == '0':
      biome_map[i][j-1] = e
  if (j+1) < mside:
    if biome_map[i][j+1] == '0':
      biome_map[i][j+1] = e

import random
def main():
  num_biomes = random.randint(mside/2, int(mside*0.75))
  for k in range(num_biomes):
    x = random.randint(0,mside-1)
    y = random.randint(0,mside-1)
    env = environments.keys()[random.randint(0,len(environments.keys())-1)]
    biome_map[x][y] = environments[env]

  while True:
    map_incomplete=False
    for i in range(mside):
      for j in range(mside):
        e = biome_map[i][j]
        if e == '0':
          map_incomplete = True
        else:
          fillSurroundingTiles(i,j,e) 
    if not map_incomplete:
      break

