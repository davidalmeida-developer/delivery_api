import os
import sys
from bson import ObjectId
from flask import Flask
import logging

app = Flask('app')

APP_NAME = os.getenv("APP_NAME", "delivery_api")
DEBUG = bool(os.getenv("DEBUG", "False"))

DATABASE_URI_BEGIN = os.getenv('DATABASE_URI_BEGIN', 'mongodb+srv://')
DATABASE_URI_END = os.getenv(
    'DATABASE_URI_END', '@mycluster.dtgxplp.mongodb.net/')
DATABASE_USER = os.getenv('DATABASE_USER', 'user')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'mysecretpassword')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'delivery')


def serialize(obj):
    if isinstance(obj, ObjectId):
        return str(obj)


logger = logging.getLogger('app')
if DEBUG:
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler(sys.stdout)

console_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")

console_handler.setFormatter(console_format)

logger.addHandler(console_handler)
