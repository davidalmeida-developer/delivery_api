class UserAlreadyExistsException(Exception):
    def __init__(self) -> None:
        super().__init__('Email já cadastrado.')