from storm.locals import *
import biome

db = create_database("sqlite:db")
store = Store(db)
store.execute("CREATE TABLE users "
              "(id INTEGER PRIMARY KEY, handle VARCHAR UNIQUE, posX INTEGER, posY INTEGER)")
store.execute("CREATE TABLE tiles "
              "(id INTEGER PRIMARY KEY, x INTEGER, y INTEGER, env INTEGER, description VARCHAR)")
