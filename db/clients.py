from models.api import ClientAPIModel, BankDetailsAPIModel
from models.db import ClientDBModel, BankDetailsDBModel
from typing import List, Optional
from sqlalchemy.orm import Session

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


def return_all_clients(db: Session) -> List[ClientAPIModel]:
    """ Returns all clients from DB. """
    clients = db.query(ClientDBModel).all()
    return [ClientAPIModel.from_orm(client) for client in clients]


def return_client_with_specified_id(
        db: Session, client_id: int) -> Optional[ClientAPIModel]:
    """ 
    Search client with specified id on DB and returns it. If it doesn't
    exist, returns None.
    """
    client = db.query(ClientDBModel).filter(
        ClientDBModel.id == client_id).first()
    return ClientAPIModel.from_orm(client) if client is not None else None


def create_client(db: Session,
                  client: ClientAPIModel) -> Optional[ClientAPIModel]:
    """ 
    Search client with specified id on DB and returns it. If it doesn't
    exist, returns None.
    """
    # Extract bank details from user.
    db_bank_details = [BankDetailsDBModel(
        **bank.dict()) for bank in client.bank_details]

    # Create DB model for client.
    user_data = client.dict()
    user_data.pop("bank_details")
    db_client = ClientDBModel(**user_data, bank_details=db_bank_details)

    # Add client to database and return created model.
    db.add(db_client)
    db.add_all(db_bank_details)
    db.commit()
    return ClientAPIModel.from_orm(db_client)
