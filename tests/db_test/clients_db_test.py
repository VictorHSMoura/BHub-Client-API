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


def test_get_clients_without_insertion(dbsession: Session):
    clients = return_all_clients(db=dbsession)
    assert clients == []


def test_get_insert_new_client(dbsession: Session):
    new_client = create_client(db=dbsession, client=default_client)
    assert new_client is not None

    assert new_client == default_client


def test_get_clients_after_insertion(dbsession: Session):
    new_client = create_client(db=dbsession, client=default_client)
    assert new_client is not None

    clients = return_all_clients(db=dbsession)
    assert clients == [default_client]


def test_get_specific_client(dbsession: Session):
    new_client = create_client(db=dbsession, client=default_client)
    assert new_client is not None

    client = return_client_with_specified_id(db=dbsession, client_id=1)
    assert client == default_client


def test_get_unexistent_client(dbsession: Session):
    client = return_client_with_specified_id(db=dbsession, client_id=1)
    assert client == None
