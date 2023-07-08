from pydantic import BaseModel


class AddressDto(BaseModel):
    street: str
    number: str
    district: str
    city: str
    complement: str
