from datetime import datetime, date
from typing import List, Optional
from pydantic import BaseModel, validator

from models.api.bank import Bank

class Client(BaseModel):
    corporate_name: str
    phone: str
    address: str
    register_date: date
    declared_billing: float
    bank_details: Optional[List[Bank]]


    @validator('register_date', pre=True)
    def validate_register_date(cls, register_date):
        if isinstance(register_date, str):
            return datetime.strptime(register_date, "%d/%m/%Y").date()
        return register_date

    @validator('phone')
    def phone_must_contain_numbers(cls, phone_number):
        if not phone_number.isdigit():
            raise ValueError('Phone number must contain only digits')
        return phone_number
