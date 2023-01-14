import pytest
from models.api.bank_details import BankDetails
from datetime import date

def test_create_bank():
    """
    Tests the creation of a new bank.
    """
    bank = BankDetails(
        branch = "34103",
        account = "27423610",
        bank_name = "Caixa Econômica Federal"
    )

    assert bank.branch == "34103"
    assert bank.account == "27423610"
    assert bank.bank_name == "Caixa Econômica Federal"

def test_create_bank_with_invalid_branch_number():
    """
    Tests the creation of a new bank with an branch number containing invalid
    characters. 
    """
    with pytest.raises(ValueError):
        """ Branch number contains one non-numeric character. """
        BankDetails(
            branch = "3410-3",
            account = "27423610",
            bank_name = "Caixa Econômica Federal"
        )

def test_create_bank_with_invalid_account_number():
    """
    Tests the creation of a new bank with an account number containing invalid
    characters. 
    """
    with pytest.raises(ValueError):
        """ Account number contains one non-numeric character. """
        BankDetails(
            branch = "34103",
            account = "2742361-0",
            bank_name = "Caixa Econômica Federal"
        )
