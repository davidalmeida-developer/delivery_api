from pydantic import BaseModel


class LoginDto(BaseModel):
    user:str
    password:str