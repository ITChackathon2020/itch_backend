import os
import ssl
import pymongo
from bson.objectid import ObjectId


client = pymongo.MongoClient(
    os.getenv("MONGO_DB_URI"), ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
itch_db = client.itch1
users = itch_db["users"]
