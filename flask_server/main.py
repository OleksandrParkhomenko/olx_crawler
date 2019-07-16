import os
import json
from bson import json_util

from flask import request
from flask import Flask
from flask import jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/olx"
mongo = PyMongo(app)

@app.route('/', methods = ['GET'])
def parse_request():
    if request.method == 'GET':
        query = request.args
        __data = mongo.db.dogs_and_cats.find(query)
        data = [item for item in __data]
        
        return json.dumps(data, default=json_util.default), 200
