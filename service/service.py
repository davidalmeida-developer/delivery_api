from dao.customers_dao import CustomersDao
from dto.customer_dtos.customer_dto import CustomerDto
from dao.orders_dao import OrdersDao
from dto.order_dtos.order_dto import OrderDto
from dao.users_dao import UsersDao
from dto.user_dtos.login_dto import LoginDto
from dto.user_dtos.user_dto import UserDto


class Service:
    def __init__(self) -> None:
        self.users_dao = UsersDao()
        self.orders_dao = OrdersDao()
        self.customers_dao = CustomersDao()
    
    # Users
    def login(self, login_dto: LoginDto):
        return self.users_dao.getUser(login_dto)

    def register(self, user_dto: UserDto):
        return self.users_dao.insertUser(user_dto)

    # Orders
    def createOrder(self, order_dto: OrderDto):
        order = order_dto.dict()

        order['company'] = self.users_dao.getUserById(order_dto.company_id)
        order['customer'] = self.customers_dao.getCustomerById(order_dto.customer_id)
        
        return self.orders_dao.insertOrder(order)

    def getOrders(self, limit: int):
        return self.orders_dao.getAll(limit)

    def getOrder(self, order_id: int):
        return self.orders_dao.getOrder(order_id)

    def updateOrder(self, order_id: int, order_dto: OrderDto) -> bool:
        return self.orders_dao.updateOrder(order_id, order_dto)
    
    def deleteOrder(self, order_id: int):
        self.orders_dao.deleteOrder(order_id)

    # Customers
    def createCustomer(self, customer_dto: CustomerDto):
        return self.customers_dao.insertCustomer(customer_dto)

    def updateCustomer(self, customer_id: int, customer_dto: CustomerDto):
        return self.customers_dao.updateCustomer(customer_id, customer_dto)

    def getCustomers(self, limit: int):
        return self.customers_dao.getAll(limit)

    def getCustomer(self, customer_id: int):
        return self.customers_dao.getCustomer(customer_id)
    
    def deleteCustomer(self, customer_id: int):
        self.customers_dao.deleteCustomer(customer_id)
    
