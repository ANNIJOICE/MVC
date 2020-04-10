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

    def getIntents(self):
        intents = mongo.db.flowers.find({'isDeleted': 'false'})
        return intents
    def getEntity(self):
        entity = mongo.db.entity.find({"isDeleted": 'false'})
        return entity

authmodel=AuthModel()