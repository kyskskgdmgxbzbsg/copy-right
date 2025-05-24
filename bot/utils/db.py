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
users = db["users"]

def add_user(user_id):
    if not users.find_one({"user_id": user_id}):
        users.insert_one({"user_id": user_id})

def get_all_users():
    return [u["user_id"] for u in users.find()]
filter_db = db["filter"]

def add_blacklist_word(chat_id, word):
    filter_db.update_one(
        {"chat_id": chat_id},
        {"$addToSet": {"blacklist": word.lower()}},
        upsert=True
    )

def add_whitelist_word(chat_id, word):
    filter_db.update_one(
        {"chat_id": chat_id},
        {"$addToSet": {"whitelist": word.lower()}},
        upsert=True
    )

def get_blacklist_words(chat_id):
    data = filter_db.find_one({"chat_id": chat_id})
    return data.get("blacklist", []) if data else []

def get_whitelist_words(chat_id):
    data = filter_db.find_one({"chat_id": chat_id})
    return data.get("whitelist", []) if data else []

def is_abusive(word, chat_id):
    word = word.lower()
    whitelist = get_whitelist_words(chat_id)
    if word in whitelist:
        return False
    blacklist = get_blacklist_words(chat_id)
    return word in blacklist