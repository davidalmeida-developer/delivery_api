from decimal import Decimal
from pydantic import BaseModel

from dto.customer_dtos.customer_dto import CustomerDto


class OrderDto(BaseModel):
    company_id: int
    customer_id: int
    value: float
