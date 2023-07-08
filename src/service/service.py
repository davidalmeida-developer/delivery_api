from src.dao.orders_dao import OrdersDao
from src.dto.order_dtos.order_dto import OrderDto
from src.dao.users_dao import UsersDao
from src.dto.user_dtos.login_dto import LoginDto
from src.dto.user_dtos.user_dto import UserDto


class Service:
    def __init__(self) -> None:
        self.users_dao = UsersDao()
        self.orders_dao = OrdersDao()

    def login(self, login_dto: LoginDto):
        return self.users_dao.getUser(login_dto)

    def register(self, user_dto: UserDto):
        return self.users_dao.insertUser(user_dto)

    def createOrder(self, order_dto: OrderDto):
        return self.orders_dao.insertOrder(order_dto)
    
    def getOrders(self, limit:int):
        return self.orders_dao.getAll(limit)
    
    def updateOrder(self, order_id:int, order_dto:OrderDto) -> bool:
        return self.orders_dao.updateOrder(order_id, order_dto)
    
