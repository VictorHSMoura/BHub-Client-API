import pytest
from apis.models.bank_details import BankDetails


def test_create_bank():
    """
    Tests the creation of a new bank.
    """
    bank = BankDetails(
        branch="34103",
        account="27423610",
        bank_name="Caixa Econômica Federal"
    )

    assert bank.branch == "34103"
    assert bank.account == "27423610"
    assert bank.bank_name == "Caixa Econômica Federal"


def test_create_bank_with_invalid_branch_number():
    """
    Tests the creation of a new bank with a branch number containing invalid
    characters.
    """
    with pytest.raises(ValueError):
        """ Branch number contains one non-numeric character. """
        BankDetails(
            branch="3410-3",
            account="27423610",
            bank_name="Caixa Econômica Federal"
        )


def test_create_bank_without_branch_number():
    """
    Tests the creation of a new bank without a branch number.
    """
    with pytest.raises(ValueError):
        """ Branch number not set. """
        BankDetails(
            account="27423610",
            bank_name="Caixa Econômica Federal"
        )


def test_create_bank_with_invalid_account_number():
    """
    Tests the creation of a new bank with an account number containing invalid
    characters.
    """
    with pytest.raises(ValueError):
        """ Account number contains one non-numeric character. """
        BankDetails(
            branch="34103",
            account="2742361-0",
            bank_name="Caixa Econômica Federal"
        )


def test_create_bank_without_account_number():
    """
    Tests the creation of a new bank without an account number.
    """
    with pytest.raises(ValueError):
        """ Account number not set. """
        BankDetails(
            branch="34103",
            bank_name="Caixa Econômica Federal"
        )


def test_create_bank_with_short_bank_name():
    """
    Tests the creation of a new bank with a short bank name.
    """
    with pytest.raises(ValueError):
        """ Bank name with less than two characters. """
        BankDetails(
            branch="34103",
            account="27423610",
            bank_name="C"
        )
