import pytest
from sqlalchemy.orm import Session

from db.clients import create_client
from db.bank_details import *
from apis.models import ClientAPIModel, BankDetailsAPIModel


def default_client():
    return ClientAPIModel(
        corporate_name="ABC Atacarejo",
        phone="3138642736",
        address="Rua 12, Lagoinha, Belo Horizonte",
        register_date="28/09/2020",
        declared_billing=15000.0,
        bank_details=[]
    )


def default_bank_details():
    return BankDetailsAPIModel(
        branch="34103",
        account="27423610",
        bank_name="Caixa Econômica Federal"
    )


def default_bank_details_response():
    return BankDetailsAPIModel(
        id=1,
        branch="34103",
        account="27423610",
        bank_name="Caixa Econômica Federal"
    )


@pytest.fixture(scope="function")
def new_client(dbsession: Session):
    create_client(db=dbsession, client=default_client())
    yield


def test_get_bank_detail_without_insertion(dbsession: Session, new_client: None):
    bank_details = return_all_bank_details(db=dbsession)
    assert bank_details == []


def test_get_clients_after_insertion(dbsession: Session, new_client: None):
    create_bank_details(db=dbsession, bank_details=default_bank_details(),
                        client_id=1)

    bank_details = return_all_bank_details(db=dbsession)
    assert bank_details == [default_bank_details_response()]


def test_get_specific_bank_details(dbsession: Session, new_client: None):
    create_bank_details(db=dbsession, bank_details=default_bank_details(),
                        client_id=1)

    bank_details = return_bank_details_with_specified_id(
        db=dbsession, bank_details_id=1)
    assert bank_details == default_bank_details_response()


def test_get_unexistent_bank_details(dbsession: Session, new_client: None):
    bank_details = return_bank_details_with_specified_id(
        db=dbsession, bank_details_id=1)
    assert bank_details is None


def test_insert_bank_for_unexistent_client(dbsession: Session, new_client: None):
    bank_details = create_bank_details(db=dbsession,
                                       bank_details=default_bank_details(),
                                       client_id=2)
    assert bank_details is None

    bank_details = return_bank_details_with_specified_id(
        db=dbsession, bank_details_id=1)
    assert bank_details is None
