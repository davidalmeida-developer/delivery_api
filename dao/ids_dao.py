from abc import ABC, abstractmethod
from typing import Dict, List

from pymongo.collection import Collection
from dto.order_dtos.order_dto import OrderDto
from errors.errors import UserAlreadyExistsException

from db.init_db import InitDb
from settings import DATABASE_NAME


class IdsDao(ABC):

    def __init__(self) -> None:
        self.client = InitDb().connectDb()
        self.collection = self.setCollection()

    @abstractmethod
    def setCollection(self) -> Collection:
        pass

    def getId(self) -> int:
        if self.isEmpty():
            self.insertFirstId()

        current_order_id = self.collection.find_one_and_update(
            {'_id': 'id'}, {'$inc': {'seq': 1}})

        return current_order_id['seq']

    def isEmpty(self) -> bool:
        return self.collection.count_documents({}) == 0

    def insertFirstId(self):
        self.collection.insert_one({'_id': 'id', 'seq': 1})
