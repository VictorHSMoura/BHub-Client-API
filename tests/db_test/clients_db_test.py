import pytest
from sqlalchemy.orm import Session

from db.clients import *
from models.api import ClientAPIModel, BankDetailsAPIModel

default_client = ClientAPIModel(
    corporate_name="ABC Atacarejo",
    phone="3138642736",
    address="Rua 12, Lagoinha, Belo Horizonte",
    register_date="28/09/2020",
    declared_billing=15000.0,
    bank_details=[
            BankDetailsAPIModel(
                branch="34103",
                account="27423610",
                bank_name="Caixa Econômica Federal"
            )
    ]
)

default_response = ClientAPIModel(
    id=1,
    corporate_name="ABC Atacarejo",
    phone="3138642736",
    address="Rua 12, Lagoinha, Belo Horizonte",
    register_date="28/09/2020",
    declared_billing=15000.0,
    bank_details=[
            BankDetailsAPIModel(
                id=1,
                branch="34103",
                account="27423610",
                bank_name="Caixa Econômica Federal"
            )
    ]
)


def test_get_clients_without_insertion(dbsession: Session):
    clients = return_all_clients(db=dbsession)
    assert clients == []


def test_get_clients_after_insertion(dbsession: Session):
    create_client(db=dbsession, client=default_client)

    clients = return_all_clients(db=dbsession)
    assert clients == [default_response]


def test_get_specific_client(dbsession: Session):
    create_client(db=dbsession, client=default_client)

    client = return_client_with_specified_id(db=dbsession, client_id=1)
    assert client == default_response


def test_get_unexistent_client(dbsession: Session):
    client = return_client_with_specified_id(db=dbsession, client_id=1)
    assert client is None


def test_update_client(dbsession: Session):
    client = create_client(db=dbsession, client=default_client)

    updated_client = default_client
    updated_client.corporate_name = "Joao Paulo Construções"

    client = update_client(db=dbsession, client_id=1, client=updated_client)

    updated_response = default_response
    updated_response.corporate_name = "Joao Paulo Construções"

    client = return_client_with_specified_id(db=dbsession, client_id=1)
    assert client == updated_response


def test_update_unexistent_client(dbsession: Session):
    updated_client = default_client
    updated_client.corporate_name = "Joao Paulo Construções"

    client = update_client(db=dbsession, client_id=1, client=updated_client)
    assert client is None

def test_update_id_not_possible(dbsession: Session):
    client = create_client(db=dbsession, client=default_client)

    updated_client = default_client
    updated_client.id = 2

    client = update_client(db=dbsession, client_id=1, client=updated_client)

    client = return_client_with_specified_id(db=dbsession, client_id=1)
    assert client == default_response
