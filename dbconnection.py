#!flask/bin/python
from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://127.0.0.1:27017")  # host uri
db = client.mymongodb  # Select the database
data_collection = db.entity  # Select the collection name
initial_data = [data for data in data_collection.find()]

if (len(initial_data)) == 0:
    data_collection.insert({
            "tag": "flower",
            "value": ["rose", "lilly","lotus","jasmine"],
            "isDeleted": "false"
          })
    data_collection.insert({
            "tag": "number",
            "value": ["one", "two","three","four"],
            "isDeleted": "false"
          })
    data_collection.insert({
            "tag": "travel",
            "value": ["flight", "train", "bus"],
            "isDeleted": "false"
          })
    data_collection.insert({
            "tag": "pickLocation",
            "value": ["chennai"],
            "isDeleted": "false"
          })
    data_collection.insert({
            "tag": "dropLocation",
            "value": ["paris", "maldives"],
            "isDeleted": "false"
          })

if __name__ == '__main__':
    app.run(debug=True)

          