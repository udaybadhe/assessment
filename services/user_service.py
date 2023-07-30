from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# MongoDB configuration
mongo_uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017")  # Use default URI if not provided
database_name = "assessment_db"  # Corrected database name

# Connect to MongoDB
client = MongoClient(mongo_uri)
db = client[database_name]
collection = db.users

def get_all_users():
    users = list(collection.find({}, {"_id": 0}))
    return users

def get_user(id):
    user = collection.find_one({"_id": ObjectId(id)}, {"_id": 0})
    return user

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
