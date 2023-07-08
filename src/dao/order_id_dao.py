from typing import Dict, List

from pymongo.collection import Collection
from src.dto.order_dtos.order_dto import OrderDto
from src.errors.errors import UserAlreadyExistsException

from src.db.init_db import InitDb
from settings import DATABASE_NAME


class OrderIdDao:

    def __init__(self) -> None:
        self.client = InitDb().connectDb()
        self.collection = self.setCollection()

    def setCollection(self) -> Collection:
        db = self.client[DATABASE_NAME]
        return db['order_ids']

    def getOrderId(self) -> int:
        if self.isEmpty():
            self.insertFirstOrderId()

        current_order_id = self.collection.find_one_and_update(
            {'_id': 'order_id'}, {'$inc': {'seq': 1}})

        return current_order_id['seq']

    def isEmpty(self) -> bool:
        return self.collection.count_documents == 0

    def insertFirstOrderId(self):
        self.collection.insert_one({'_id': 'order_id', 'seq': 1})
