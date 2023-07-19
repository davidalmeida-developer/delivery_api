from typing import Dict
from pydantic import BaseModel, validator
from dto.helpers.cpf_cnpj_helper import Validator

from dto.customer_dtos.address_dto import AddressDto


class CustomerDto(BaseModel):
    name: str
    document: str
    phone_number: str
    address: AddressDto

    @validator('document')
    def validateDocument(cls, document: str):
        return Validator.validateDocument(document)

    @validator('phone_number')
    def validatePhone(cls, phone_number: str):
        return Validator.validatePhoneNumber(phone_number)
