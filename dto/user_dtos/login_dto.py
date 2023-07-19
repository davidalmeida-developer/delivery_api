from email_validator import EmailNotValidError, validate_email
from pydantic import BaseModel, validator

from dto.helpers.cpf_cnpj_helper import Validator


class LoginDto(BaseModel):
    email: str
    password: str

    @validator('email')
    def validateEmail(cls, email):
        return Validator.validateEmail(email)
