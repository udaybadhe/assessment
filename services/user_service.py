# services/user_service.py
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()

# MongoDB configuration
mongo_uri = os.getenv("MONGODB_URI")
database_name = os.getenv("DATABASE_NAME")

# Connect to MongoDB
client = MongoClient(mongo_uri)
db = client[database_name]
collection = db.users

def get_all_users():
    users = list(collection.find({}))
    for user in users:
        user["_id"] = str(user["_id"])  # Convert ObjectId to string
    return users

def get_user(id):
    user = collection.find_one({"_id": ObjectId(id)})
    if user:
        user["_id"] = str(user["_id"])  # Convert ObjectId to string
        return user
    return None

def create_user(data):
    user = {
        "name": data["name"],
        "email": data["email"],
        "password": data["password"]
    }
    result = collection.insert_one(user)
    return str(result.inserted_id)

def update_user(id, data):
    updated_user = {}

    if "name" in data:
        updated_user["name"] = data["name"]
    if "email" in data:
        updated_user["email"] = data["email"]
    if "password" in data:
        updated_user["password"] = data["password"]

    if not updated_user:
        return False

    result = collection.update_one({"_id": ObjectId(id)}, {"$set": updated_user})
    return result.modified_count > 0

def delete_user(id):
    result = collection.delete_one({"_id": ObjectId(id)})
    return result.deleted_count > 0
