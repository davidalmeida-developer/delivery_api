class UserAlreadyExistsException(Exception):
    def __init__(self) -> None:
        super().__init__('Email já cadastrado.')


class UserIdNotFoundException(Exception):
    def __init__(self) -> None:
        super().__init__('Id do usuário não encontrado.')


class OrderIdNotFoundException(Exception):
    def __init__(self) -> None:
        super().__init__('Id do pedido não encontrado.')


class CustomerIdNotFoundException(Exception):
    def __init__(self) -> None:
        super().__init__('Id do cliente não encontrado.')
