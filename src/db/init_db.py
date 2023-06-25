from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from settings import DATABASE_USER, DATABASE_PASSWORD, DATABASE_URI_BEGIN, DATABASE_URI_END, DATABASE_NAME

class InitDb:
    def __init__(self) -> None:
        self.user = DATABASE_USER
        self.password = DATABASE_PASSWORD
        self.uri_begin = DATABASE_URI_BEGIN
        self.uri_end = DATABASE_URI_END
        self.db_name = DATABASE_NAME

    def connectDb(self):
        try:
            uri = f'{self.uri_begin}{self.user}{self.separator()}{self.password}{self.uri_end}' 
            client = MongoClient(uri, server_api=ServerApi('1'))
            client.admin.command('ping')
            return client
        except Exception as e:
            print(e)

    def separator(self) -> str:
        if self.user and self.password:
            return ':'
        return ''