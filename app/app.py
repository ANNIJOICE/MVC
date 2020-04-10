from flask import Flask,request
from flask_pymongo import PyMongo
from app.config import config
app = Flask(__name__, template_folder="views")
app.config['MONGO_DBNAME'] = config['MONGO_DBNAME']
app.config['MONGO_URI'] = config['MONGO_URI']
mongo = PyMongo(app)