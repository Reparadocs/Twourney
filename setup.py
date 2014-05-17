from storm.locals import *

db = create_database("sqlite:db")
store = Store(db)
store.execute("CREATE TABLE users "
              "(id INTEGER PRIMARY KEY, handle VARCHAR UNIQUE, posX INTEGER, posY INTEGER)")

