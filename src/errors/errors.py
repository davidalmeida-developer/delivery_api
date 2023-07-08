class UserAlreadyExistsException(Exception):
    def __init__(self) -> None:
        super().__init__('Email já cadastrado.')

class OrderIdNotFoundException(Exception):
    def __init__(self) -> None:
        super().__init__('Id do pedido não encontrado.')