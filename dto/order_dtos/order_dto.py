from decimal import Decimal
from pydantic import BaseModel

from dto.customer_dtos.customer_dto import CustomerDto


class OrderDto(BaseModel):
    customer:CustomerDto
    value:Decimal
