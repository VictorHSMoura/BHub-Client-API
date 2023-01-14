from models.api import ClientAPIModel, BankDetailsAPIModel
from typing import List, Optional

default_client = ClientAPIModel(
    corporate_name="ABC Atacarejo",
    phone="3138642736",
    address="Rua 12, Lagoinha, Belo Horizonte",
    register_date="28/09/2020",
    declared_billing=15000,
    bank_details=[
        BankDetailsAPIModel(
            branch="34103",
            account="27423610",
            bank_name="Caixa Econômica Federal"
        )
    ]
)

# TODO: add DB and retrieve info from it.

def return_all_clients() -> List[ClientAPIModel]:
    """ Returns all clients from DB. """
    return [default_client]

def return_client_with_specified_id(client_id: int) -> Optional[ClientAPIModel]:
    """ 
    Search client with specified id on DB and returns it. If it doesn't
    exist, returns None.
    """
    # TODO: query on db and verify if user exists.
    if (client_id == 1):
        return default_client
    return None
