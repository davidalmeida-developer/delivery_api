from pymongo.collection import Collection
from typing import Dict, List
from dao.ids_dao import IdsDao
from dto.customer_dtos.customer_dto import CustomerDto

from errors.errors import CustomerIdNotFoundException, CustomerIdNotFoundException
from dto.customer_dtos.customer_dto import CustomerDto
from db.init_db import InitDb
from settings import DATABASE_NAME


class CustomersDao:

    def __init__(self) -> None:
        self.client = InitDb().connectDb()
        self.collection = self.setCollection()
        self.customer_id_dao = CustomerIdsDao()

    def setCollection(self) -> Collection:
        db = self.client[DATABASE_NAME]
        return db['customers']

    def insertCustomer(self, customer_dto: CustomerDto) -> int:
        customer = customer_dto.dict()

        customer['customer_id'] = self.customer_id_dao.getId()

        self.collection.insert_one(customer)

        return customer["customer_id"]

    def getAll(self, limit: int):
        return list(self.collection.find().limit(limit=limit))

    def getCustomer(self, customer_id: int):
        result = list(self.collection.find(
            filter={'customer_id': (customer_id)}))
        if len(result) > 0:
            return result[0]
        raise CustomerIdNotFoundException()

    def getCustomerById(self, customer_id: int):
        result = self.collection.find_one({'customer_id': customer_id})
        if result:
            return result
        raise CustomerIdNotFoundException()

    def updateCustomer(self, customer_id: int, customer_dto: CustomerDto) -> bool:
        result = self.collection.update_one(
            filter={'customer_id': customer_id}, update=customer_dto.__dict__)

        if result.modified_count == 1:
            return True
        raise CustomerIdNotFoundException()

    def deleteCustomer(self, customer_id: int):
        result = self.collection.delete_one({'customer_id': customer_id})
        if result.deleted_count == 1:
            return
        raise CustomerIdNotFoundException()


class CustomerIdsDao(IdsDao):

    def __init__(self) -> None:
        super().__init__()

    def setCollection(self) -> Collection:
        db = self.client[DATABASE_NAME]
        return db['customer_ids']
