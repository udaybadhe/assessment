from pymongo import MongoClient
from bson.objectid import ObjectId
import hashlib

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = self._hash_password(password)  # Hash the password during initialization

    def _hash_password(self, password):
        # Hash the password using SHA-256
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

    def verify_password(self, password):
        # Verify if the provided password matches the stored hashed password
        return self.password == self._hash_password(password)

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password
        }

    @staticmethod
    def from_dict(data):
        return User(
            name=data["name"],
            email=data["email"],
            password=data["password"]
        )
    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password
        }

    @staticmethod
    def from_dict(data):
        return User(
            name=data["name"],
            email=data["email"],
            password=data["password"]
        )
