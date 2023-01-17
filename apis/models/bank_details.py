from pydantic import BaseModel, validator
from typing import Optional


class BankDetails(BaseModel):
    id: Optional[int]
    branch: str
    account: str
    bank_name: str

    @validator('branch')
    def branch_must_contain_numbers(cls, branch_number: str):
        if not branch_number.isdigit(): 
            # Also checks if len(branch_number) >= 1
            raise ValueError('Branch number must contain only digits.')
        return branch_number

    @validator('account')
    def account_must_contain_numbers(cls, account_number: str):
        if not account_number.isdigit():
            # Also checks if len(account_number) >= 1
            raise ValueError('Account number must contain only digits.')
        return account_number

    @validator('bank_name')
    def bank_name_must_contain_numbers(cls, bank_name: str):
        if len(bank_name) < 2:
            raise ValueError('Bank name must contain at least 2 characters.')
        return bank_name

    class Config:
        orm_mode = True
