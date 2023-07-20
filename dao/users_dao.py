from pymongo.collection import Collection
from dao.ids_dao import IdsDao
from errors.errors import UserAlreadyExistsException, UserIdNotFoundException

from dto.user_dtos.login_dto import LoginDto
from dto.user_dtos.user_dto import UserDto
from db.init_db import InitDb
from settings import DATABASE_NAME


class UsersDao:

    def __init__(self) -> None:
        self.client = InitDb().connectDb()
        self.collection = self.setCollection()
        self.user_ids_dao = UserIdsDao()

    def setCollection(self) -> Collection:
        db = self.client[DATABASE_NAME]
        return db['users']

    def insertUser(self, user_dto: UserDto):
        if self.collection.count_documents({'email': user_dto.email}) > 0:
            raise UserAlreadyExistsException()

        user = user_dto.dict()

        user['user_id'] = self.user_ids_dao.getId()

        result = self.collection.insert_one(user)

        return str(result.inserted_id)

    def getAll(self, limit: int = 20):
        return list(self.collection.find().limit(limit=limit))

    def getUser(self, login_dto: LoginDto):
        result = list(self.collection.find(
            login_dto.dict(), {"password": 0}))

        if len(result) > 0:
            return result[0]
        raise ValueError("Usuário ou senha inválidos.")

    def getUserById(self, user_id: int):
        result = self.collection.find_one({'user_id': user_id})
        if result:
            return result
        raise UserIdNotFoundException()


class UserIdsDao(IdsDao):
    def __init__(self) -> None:
        super().__init__()

    def setCollection(self) -> Collection:
        db = self.client[DATABASE_NAME]
        return db['user_ids']
