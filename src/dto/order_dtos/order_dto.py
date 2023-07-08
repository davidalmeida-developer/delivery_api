from pydantic import BaseModel

from src.dto.order_dtos.address_dto import AddressDto


class OrderDto(BaseModel):
    client_name: str
    client_phone_number: str
    client_address: AddressDto
