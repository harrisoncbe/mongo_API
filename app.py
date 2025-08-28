from flask import Flask, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB connection string from Render environment variable
MONGO_URI = os.environ.get("MONGO_URI")

# connect to MongoDB
client = MongoClient(MONGO_URI)
db = client["TestDB"]   # 👈 change "testdb" to your database name
collection = db["users"]  # 👈 change "testcollection" to your collection name


@app.route("/")
def home():
    return jsonify({"message": "MongoDB API is running!"})


@app.route("/records", methods=["GET"])
def get_records():
    records = list(collection.find({}, {"_id": 0}))  # fetch all docs, hide _id
    return jsonify(records)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
