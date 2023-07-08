from email_validator import  EmailNotValidError, validate_email
from phonenumbers import is_valid_number, parse, NumberParseException
from pydantic import BaseModel, EmailStr, ValidationError, validator

from src.dto.helpers.cpf_cnpj_helper import Documento

class UserDto(BaseModel):
    document:str
    password:str
    company_name:str
    email:str
    phone_number:str

    @validator('document')
    def validateCnpj(cls, document):
        document = Documento.criaDocumento(document)
        return str(document)

    @validator('email')
    def validateEmail(cls, email):
        try:
            validate_email(email=email)
        except EmailNotValidError:
            raise ValueError('Email inválido')
        return email
    
    @validator('phone_number')
    def validatePhone(cls, phone_number):
        try:
            if len(phone_number) in [11,10] and phone_number[0:2] != "+55":
                phone_number = f"+55{phone_number}"
            parsed_number = parse(phone_number, None)
            if not is_valid_number(parsed_number):
                raise ValueError('Número de telefone inválido')
        except NumberParseException:
            raise ValueError('Número de telefone inválido')
        return phone_number