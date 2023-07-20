from pymongo.collection import Collection
from typing import Dict, List
from dao.ids_dao import IdsDao

from errors.errors import OrderIdNotFoundException
from dto.order_dtos.order_dto import OrderDto
from db.init_db import InitDb
from settings import DATABASE_NAME


class OrdersDao():

    def __init__(self) -> None:
        self.client = InitDb().connectDb()
        self.collection = self.setCollection()
        self.order_ids_dao = OrderIdsDao()

    def setCollection(self) -> Collection:
        db = self.client[DATABASE_NAME]
        return db['orders']

    def insertOrder(self, order: Dict) -> int:

        order['order_id'] = self.order_ids_dao.getId()
        order['status'] = 'pendente'

        self.collection.insert_one(order)

        return order["order_id"]

    def getAll(self, limit: int):
        return list(self.collection.find().limit(limit=limit))

    def getOrder(self, order_id: int):
        result = list(self.collection.find(filter={'order_id': order_id}))
        if len(result) > 0:
            return result[0]
        raise OrderIdNotFoundException()

    def updateOrder(self, order_id: int, order_dto: OrderDto) -> bool:
        result = self.collection.update_one(
            filter={'order_id': order_id}, update=order_dto.dict())

        if result.modified_count == 1:
            return True
        raise OrderIdNotFoundException()

    def deleteOrder(self, order_id: int):
        result = self.collection.delete_one({'order_id': order_id})
        if result.deleted_count == 1:
            return
        raise OrderIdNotFoundException()


class OrderIdsDao(IdsDao):
    def __init__(self) -> None:
        super().__init__()

    def setCollection(self) -> Collection:
        db = self.client[DATABASE_NAME]
        return db['order_ids']
