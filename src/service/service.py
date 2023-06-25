from src.dao.users_dao import UsersDao
from src.dto.login_dto import LoginDto
from src.dto.user_dto import UserDto


class Service:
    def __init__(self) -> None:
        self.user_dao = UsersDao()

    def login(self, login_data:LoginDto):
        return self.user_dao.getUser(login_data=login_data)

    def register(self, user_data:UserDto):
        return self.user_dao.insertUser(user=user_data)