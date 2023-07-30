# app.py
import os
from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv

# Load environment variables from .env file (optional)
load_dotenv()

# Create Flask application instance
app = Flask(__name__)

# MongoDB configuration
mongo_uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017")  # Use default URI if not provided
database_name = "assessment_db"  # Corrected database name

# Connect to MongoDB
client = MongoClient(mongo_uri)
db = client[database_name]
collection = db.users

# Routes for CRUD operations
@app.route("/users", methods=["GET"])
def get_all_users():
    users = list(collection.find({}, {"_id": 0}))
    return jsonify(users)

@app.route("/users/<string:id>", methods=["GET"])
def get_user(id):
    user = collection.find_one({"_id": ObjectId(id)}, {"_id": 0})
    if user:
        return jsonify(user)
    return jsonify({"message": "User not found"}), 404

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    user = {
        "name": data["name"],
        "email": data["email"],
        "password": data["password"]
    }
    result = collection.insert_one(user)
    return jsonify({"message": "User created successfully", "inserted_id": str(result.inserted_id)}), 201

@app.route("/users/<string:id>", methods=["PUT"])
def update_user(id):
    data = request.get_json()
    updated_user = {}

    if "name" in data:
        updated_user["name"] = data["name"]
    if "email" in data:
        updated_user["email"] = data["email"]
    if "password" in data:
        updated_user["password"] = data["password"]

    if not updated_user:
        return jsonify({"message": "No valid fields provided for update"}), 400

    result = collection.update_one({"_id": ObjectId(id)}, {"$set": updated_user})

    if result.modified_count > 0:
        return jsonify({"message": "User updated successfully"}), 200

    return jsonify({"message": "User not found"}), 404

@app.route("/users/<string:id>", methods=["DELETE"])
def delete_user(id):
    result = collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count > 0:
        return jsonify({"message": "User deleted successfully"}), 200
    return jsonify({"message": "User not found"}), 404

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
