import pytest
from apis.models.client import Client
from datetime import date

def test_create_client_without_bank_details():
    """
    Tests the creation of a new client without bank details.
    """
    client = Client(
        corporate_name="ABC Atacarejo",
        phone="3138642736",
        address="Rua 12, Lagoinha, Belo Horizonte",
        register_date="28/09/2020",
        declared_billing=15000
    )

    assert client.corporate_name == "ABC Atacarejo"
    assert client.phone == "3138642736"
    assert client.address == "Rua 12, Lagoinha, Belo Horizonte"
    assert client.register_date == date(2020, 9, 28)
    assert client.declared_billing == 15000

def test_create_client_with_bank_details():
    """
    Tests the creation of a new client without bank details.
    """
    client = Client(
        corporate_name="ABC Atacarejo",
        phone="3138642736",
        address="Rua 12, Lagoinha, Belo Horizonte",
        register_date="28/09/2020",
        declared_billing=15000,
        bank_details=[
            {
                "branch": "34103",
                "account": "27423610",
                "bank_name": "Caixa Econômica Federal"
            }
        ]
    )

    assert client.corporate_name == "ABC Atacarejo"
    assert client.phone == "3138642736"
    assert client.address == "Rua 12, Lagoinha, Belo Horizonte"
    assert client.register_date == date(2020, 9, 28)
    assert client.declared_billing == 15000
    assert client.bank_details[0].branch == "34103"
    assert client.bank_details[0].account == "27423610"
    assert client.bank_details[0].bank_name == "Caixa Econômica Federal"

def test_create_client_with_invalid_phone_number():
    """
    Tests the creation of a new client with an phone number containing invalid
    characters. 
    """
    with pytest.raises(ValueError):
        """ Phone number contains one non-numeric character. """
        Client(
            corporate_name="ABC Atacarejo",
            phone="31-38642736",
            address="Rua 12, Lagoinha, Belo Horizonte",
            register_date="28/09/2020",
            declared_billing=15000,
            bank_details=[]
        )

def test_create_client_with_invalid_register_date():
    """
    Tests the creation of a new client with an register date incorrectly
    formatted.
    """
    with pytest.raises(ValueError):
        """ Register date is missing day number. """
        Client(
            corporate_name="ABC Atacarejo",
            phone="3138642736",
            address="Rua 12, Lagoinha, Belo Horizonte",
            register_date="/09/2020",
            declared_billing=15000,
            bank_details=[]
        )