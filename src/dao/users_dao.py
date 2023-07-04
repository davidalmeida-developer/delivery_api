from typing import  Dict, List

from pymongo.collection import Collection
from src.errors.errors import UserAlreadyExistsException

from src.dto.login_dto import LoginDto
from src.dto.user_dto import UserDto
from src.db.init_db import InitDb
from settings import DATABASE_NAME

class UsersDao:
    
    def __init__(self) -> None:
        self.client = InitDb().connectDb()

    def insertUser(self, user:UserDto):
        
        user_dict = user.__dict__
        collection = self.setColecao()
        
        if collection.count_documents({'email': user_dict['email']}) > 0:
            raise UserAlreadyExistsException()

        result = collection.insert_one(user_dict)

        return str(result.inserted_id)
    
    def getAll(self,):

        colecao = self.setColecao()
        result = colecao.find()
        
        return list(result)
    
    def getUser(self, login_data:LoginDto):

            collection = self.setColecao()

            filtro = login_data.__dict__

            result = list(collection.find(filtro, {"password":0}))

            if len(result) > 0:
                return result
            raise ValueError("Usuário ou senha inválidos.")
    
    def setColecao(self)-> Collection:
        db = self.client[DATABASE_NAME]
        return db['users']

    
    
    def getEnderecos(self) -> List[Dict]:
        collection = self.setColecao()
        enderecos = list(collection.find({},{"tipo_logradouro" : 1, "logradouro" : 1, "bairro" : 1, "uf" : 1, "cep" : 1}))

        return enderecos