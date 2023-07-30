# app.py
from flask import Flask, jsonify, request
from services.user_service import get_all_users, get_user, create_user, update_user, delete_user

app = Flask(__name__)

@app.route("/users", methods=["GET"])
def get_all_users_route():
    users = get_all_users()
    return jsonify(users)

@app.route("/users/<string:id>", methods=["GET"])
def get_user_route(id):
    user = get_user(id)
    if user:
        return jsonify(user)
    return jsonify({"message": "User not found"}), 404

@app.route("/users", methods=["POST"])
def create_user_route():
    data = request.get_json()
    user_id = create_user(data)
    if user_id:
        return jsonify({"message": "User created successfully", "inserted_id": user_id}), 201
    return jsonify({"message": "Invalid data provided"}), 400

@app.route("/users/<string:id>", methods=["PUT"])
def update_user_route(id):
    data = request.get_json()
    updated = update_user(id, data)
    if updated:
        return jsonify({"message": "User updated successfully"}), 200
    return jsonify({"message": "User not found or no valid fields provided for update"}), 404

@app.route("/users/<string:id>", methods=["DELETE"])
def delete_user_route(id):
    deleted = delete_user(id)
    if deleted:
        return jsonify({"message": "User deleted successfully"}), 200
    return jsonify({"message": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
