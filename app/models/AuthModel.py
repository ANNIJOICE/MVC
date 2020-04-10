from ..app import mongo
from flask import request,json
import hashlib
import pprint
from flask_pymongo import ObjectId
from datetime import datetime
from app.helpers.Utility import toDictionaryArray

class AuthModel():
    def __init__(self):
        pass

    def getUser(self):
     #    users = mongo.db.users.find({'_id': _id})
     #    x = []
     #    for user in users:
     #        x.append(user)
        return "user"


authmodel=AuthModel()