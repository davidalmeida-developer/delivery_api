import os
from bson import ObjectId
from flask import Flask


app = Flask('app')

DATABASE_URI_BEGIN = os.getenv('DATABASE_URI_BEGIN' ,'mongodb+srv://')
DATABASE_URI_END = os.getenv('DATABASE_URI_END','@mycluster.dtgxplp.mongodb.net/')
DATABASE_USER=os.getenv('DATABASE_USER','user')
DATABASE_PASSWORD=os.getenv('DATABASE_PASSWORD','mysecretpassword')
DATABASE_NAME=os.getenv('DATABASE_NAME', 'delivery')


def serialize(obj):
    if isinstance(obj, ObjectId):
        return str(obj)