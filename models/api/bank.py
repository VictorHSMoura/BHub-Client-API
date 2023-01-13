from pydantic import BaseModel, validator

class Bank(BaseModel):
    branch: str
    account: str
    bank_name: str

    @validator('branch')
    def branch_must_contain_numbers(cls, branch_number: str):
        if not branch_number.isdigit():
            raise ValueError('Branch number must contain only digits')
        return branch_number

    @validator('account')
    def account_must_contain_numbers(cls, account_number):
        if not account_number.isdigit():
            raise ValueError('Account number must contain only digits')
        return account_number