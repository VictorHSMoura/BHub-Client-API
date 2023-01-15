from datetime import datetime, date
from typing import List, Optional
from pydantic import BaseModel, validator

from apis.models.bank_details import BankDetails


class Client(BaseModel):
    id: Optional[int]
    corporate_name: str
    phone: str
    address: str
    register_date: date
    declared_billing: float
    bank_details: Optional[List[BankDetails]]

    @validator('register_date', pre=True)
    def validate_register_date(cls, register_date):
        if isinstance(register_date, str):
            return datetime.strptime(register_date, "%d/%m/%Y").date()
        return register_date

    @validator('phone')
    def phone_must_contain_at_least_eight_numbers(cls, phone_number):
        if not phone_number.isdigit():
            raise ValueError('Phone number must contain only digits.')
        if len(phone_number) < 8:
            raise ValueError('Phone number must contain at least 8 digits.')
        return phone_number

    @validator('corporate_name')
    def corporate_name_must_contain_at_least_two_chars(cls, corporate_name):
        if len(corporate_name) < 2:
            raise ValueError(
                'Corporate name must contain at least 2 characters.')
        return corporate_name

    @validator('declared_billing')
    def declared_billing_must_be_greater_than_zero(cls, declared_billing):
        if declared_billing <= 0:
            raise ValueError('Declared billing must be greater than 0.')
        return declared_billing

    class Config:
        orm_mode = True
