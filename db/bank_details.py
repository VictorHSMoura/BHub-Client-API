from apis.models import ClientAPIModel, BankDetailsAPIModel
from db.models import ClientDBModel, BankDetailsDBModel
from typing import List, Optional
from sqlalchemy.orm import Session


def return_all_bank_details(db: Session) -> List[BankDetailsAPIModel]:
    """ Returns all bank details from DB. """
    bank_details = db.query(BankDetailsDBModel).all()
    return [BankDetailsAPIModel.from_orm(bank) for bank in bank_details]


def return_bank_details_with_specified_id(
        db: Session, bank_details_id: int) -> Optional[BankDetailsAPIModel]:
    """
    Search client with specified id on DB and returns it. If it doesn't
    exist, returns None.
    """
    bank_details = db.query(BankDetailsDBModel).filter(
        BankDetailsDBModel.id == bank_details_id).first()
    return BankDetailsAPIModel.from_orm(bank_details)\
        if bank_details is not None else None


def create_bank_details(db: Session, bank_details: BankDetailsAPIModel,
                        client_id: int) -> Optional[BankDetailsAPIModel]:
    """ 
    Create bank details with specified parameters on DB and returns created
    bank details.
    """

    # Verify if client exists on database.
    db_client = db.query(ClientDBModel).filter(
        ClientDBModel.id == client_id).first()
    if db_client is None:
        return None

    # Convert bank details from Pydantic to ORM.
    db_bank_details = BankDetailsDBModel(
        **bank_details.dict(), client_id=client_id)

    # Add bank details to database and return created model.
    db.add(db_bank_details)
    db.commit()
    return BankDetailsAPIModel.from_orm(db_bank_details)


def update_bank_details(
        db: Session, bank_id: int,
        bank_details: BankDetailsAPIModel) -> Optional[BankDetailsAPIModel]:
    """ 
    Update client parameters on DB and returns new client. If it doesn't
    exist, returns None.
    """
    # Retrieve client from DB
    db_bank_details: BankDetailsDBModel = db.query(BankDetailsDBModel).filter(
        BankDetailsDBModel.id == bank_id).first()
    if db_bank_details is None:
        return None

    db_bank_details.account = bank_details.account
    db_bank_details.bank_name = bank_details.bank_name
    db_bank_details.branch = bank_details.branch

    # Add client to database and return created model.
    db.commit()
    return BankDetailsAPIModel.from_orm(db_bank_details)