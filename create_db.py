from pymongo import MongoClient

import sys
sys.path.append('.')
from config import AdminConfig

client = MongoClient(AdminConfig.MONGO_URI)
db = client.stocks
db.command("createUser", AdminConfig.MONGO_USERNAME, pwd=AdminConfig.MONGO_PASSWORD, roles=["readWrite"])
conn = db.stocks
conn.insert_one({'id': 1})
