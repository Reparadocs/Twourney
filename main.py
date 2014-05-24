from storm.locals import *
import biome, rpg, constants

database = create_database("sqlite:db")
store = Store(database)

cell_map = biome.cellMap(constants.SEED)
rpg.setup(store)


