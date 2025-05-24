from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["warn_db"]
warns = db["warns"]

def get_warn_count(chat_id, user_id):
    data = warns.find_one({"chat_id": chat_id, "user_id": user_id})
    return data["count"] if data else 0

def increase_warn(chat_id, user_id):
    data = warns.find_one({"chat_id": chat_id, "user_id": user_id})
    if data:
        warns.update_one({"_id": data["_id"]}, {"$inc": {"count": 1}})
    else:
        warns.insert_one({"chat_id": chat_id, "user_id": user_id, "count": 1})
    return get_warn_count(chat_id, user_id)

def reset_warn(chat_id, user_id):
    warns.delete_one({"chat_id": chat_id, "user_id": user_id})