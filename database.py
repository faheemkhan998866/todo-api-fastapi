from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["todo_database"]

todos_collection = db["todos"]
users_collection = db["users"]