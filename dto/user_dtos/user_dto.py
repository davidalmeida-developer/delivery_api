from pydantic import BaseModel, validator

from dto.helpers.cpf_cnpj_helper import Validator


class UserDto(BaseModel):
    document: str
    password: str
    company_name: str
    email: str
    phone_number: str

    @validator('document')
    def validateDocument(cls, document):
        return Validator.validateDocument(document)

    @validator('email')
    def validateEmail(cls, email):
        return Validator.validateEmail(email)

    @validator('phone_number')
    def validatePhone(cls, phone_number):
        return Validator.validatePhoneNumber(phone_number)
