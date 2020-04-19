import pickledb

DB_NAME = 'summoners.db'

def add(key, value):
    db = pickledb.load(DB_NAME, True)
    db.set(key, value)

def get(key):
    db = pickledb.load(DB_NAME, False)
    value = db.get(key)
    return value

def get_keys():
    db = pickledb.load(DB_NAME, False)
    keys = list(db.getall())
    return keys

def rm(key):
    db = pickledb.load(DB_NAME, True)
    db.rem(key)
