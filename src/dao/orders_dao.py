from pymongo.collection import Collection
from typing import Dict, List

from dao.order_id_dao import OrderIdDao
from errors.errors import OrderIdNotFoundException
from src.dto.order_dtos.order_dto import OrderDto
from src.db.init_db import InitDb
from settings import DATABASE_NAME


class OrdersDao:

    def __init__(self) -> None:
        self.client = InitDb().connectDb()
        self.collection = self.setCollection()
        self.order_id_dao = OrderIdDao()

    def setCollection(self) -> Collection:
        db = self.client[DATABASE_NAME]
        return db['orders']

    def insertOrder(self, order_dto: OrderDto) -> int:
        order = order_dto.__dict__

        order['order_id'] = self.order_id_dao.getOrderId()

        self.collection.insert_one(order)

        return order["order_id"]

    def getAll(self, limit: int):
        return list(self.collection.find().limit(limit=limit))

    def getOrder(self, order_id: int):
        result = list(self.collection.find(filter={'order_id': order_id}))
        if len(result) > 0:
            return result[0]
        raise ValueError("Id do pedido não encontrado.")

    def updateOrder(self, order_id: int, order_dto: OrderDto) -> bool:
        result = self.collection.update_one(
            filter={'order_id': order_id}, update=order_dto.__dict__)

        if result.modified_count == 1:
            return True
        raise OrderIdNotFoundException()