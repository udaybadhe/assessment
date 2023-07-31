from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os
from models.user import User

load_dotenv()

mongo_uri = os.getenv("MONGODB_URI")
database_name = os.getenv("DATABASE_NAME")

client = MongoClient(mongo_uri)
db = client[database_name]
collection = db.users

def get_all_users():
    users = list(collection.find({}))
    for user in users:
        user["_id"] = str(user["_id"])
    return users

def get_user(id):
    user_data = collection.find_one({"_id": ObjectId(id)})
    if user_data:
        user = User.from_dict(user_data)
        return user
    return None

def create_user(data):
    user = User(data["name"], data["email"], data["password"])
    result = collection.insert_one(user.to_dict())
    return str(result.inserted_id)

def update_user(id, data):
    user = get_user(id)
    if not user:
        return False

    if "name" in data:
        user.name = data["name"]
    if "email" in data:
        user.email = data["email"]
    if "password" in data:
        user.password = data["password"]

    result = collection.update_one({"_id": ObjectId(id)}, {"$set": user.to_dict()})
    return result.modified_count > 0

def delete_user(id):
    result = collection.delete_one({"_id": ObjectId(id)})
    return result.deleted_count > 0
