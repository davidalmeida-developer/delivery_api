from email_validator import EmailNotValidError, validate_email
from pydantic import BaseModel, validator


class LoginDto(BaseModel):
    email:str
    password:str

    @validator('email')
    def validateEmail(cls, email):
        try:
            validate_email(email=email)
        except EmailNotValidError:
            raise ValueError('Email inválido')
        return email