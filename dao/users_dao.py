from pymongo.collection import Collection
from errors.errors import UserAlreadyExistsException

from dto.user_dtos.login_dto import LoginDto
from dto.user_dtos.user_dto import UserDto
from db.init_db import InitDb
from settings import DATABASE_NAME


class UsersDao:

    def __init__(self) -> None:
        self.client = InitDb().connectDb()
        self.collection = self.setCollection()

    def setCollection(self) -> Collection:
        db = self.client[DATABASE_NAME]
        return db['users']

    def insertUser(self, user: UserDto):
        if self.collection.count_documents({'email': user.email}) > 0:
            raise UserAlreadyExistsException()

        result = self.collection.insert_one(user.__dict__)

        return str(result.inserted_id)

    def getAll(self, limit: int = 20):
        return list(self.collection.find().limit(limit=limit))

    def getUser(self, login_dto: LoginDto):
        result = list(self.collection.find(
            login_dto.__dict__, {"password": 0}))

        if len(result) > 0:
            return result[0]
        raise ValueError("Usuário ou senha inválidos.")
