from email_validator import  EmailNotValidError, validate_email
from phonenumbers import is_valid_number, parse, NumberParseException
from pydantic import BaseModel, EmailStr, ValidationError, validator
from validate_docbr import CNPJ

class UserDto(BaseModel):
    user:str
    password:str
    company_name:str
    cnpj:str
    email:str
    phone_number:str

    @validator('cnpj')
    def validateCnpj(cls, cnpj):
            
        cnpj_validator = CNPJ()
        is_valid = cnpj_validator.validate(cnpj)
        if not is_valid:
            raise ValueError('CNPJ inválido')
        
        return cnpj_validator.mask(cnpj)

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