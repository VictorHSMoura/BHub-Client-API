from fastapi import APIRouter, HTTPException, Depends, status
from apis.models import BankDetailsAPIModel

from sqlalchemy.orm import Session
import db.bank_details as db
from db.sqlalchemy_db import get_db_instance

router = APIRouter(
    prefix="/bank_details",
    tags=["bank_details"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[BankDetailsAPIModel],
            status_code=status.HTTP_200_OK)
def get_bank_details(db_instance: Session = Depends(get_db_instance)):
    """ Returns a list with all registered bank details. """
    all_bank_details = db.return_all_bank_details(db=db_instance)
    return all_bank_details


@router.get("/{bank_details_id}", response_model=BankDetailsAPIModel,
            status_code=status.HTTP_200_OK)
def get_bank_details_with_id(bank_details_id: int,
                             db_instance: Session = Depends(get_db_instance)):
    """ Returns a bank details with the specified id. """
    bank_details = db.return_bank_details_with_specified_id(
        db=db_instance, bank_id=bank_details_id)
    if bank_details is None:
        raise HTTPException(404, detail="Bank details not found.")
    return bank_details


@router.get("/client/{client_id}", response_model=list[BankDetailsAPIModel],
            status_code=status.HTTP_200_OK)
def get_bank_details_for_client(
        client_id: int, db_instance: Session = Depends(get_db_instance)):
    """ Returns a list with all registered bank details for a client. """
    bank_details = db.return_all_bank_details_for_client(db=db_instance,
                                                         client_id=client_id)
    return bank_details


@router.post("/client/{client_id}", response_model=BankDetailsAPIModel,
             status_code=status.HTTP_201_CREATED)
def creates_new_bank_details(bank_details: BankDetailsAPIModel,
                             client_id: int,
                             db_instance: Session = Depends(get_db_instance)):
    """ Creates a bank details with specified parameters. """
    bank_details = db.create_bank_details(
        db=db_instance, bank_details=bank_details, client_id=client_id)
    if bank_details is None:
        raise HTTPException(
            500, detail="Unexpected error on bank details creation.")
    return bank_details


@router.put("/{bank_details_id}", response_model=BankDetailsAPIModel,
            status_code=status.HTTP_200_OK)
def update_bank_details(
        bank_details_id: int, bank_details: BankDetailsAPIModel,
        db_instance: Session = Depends(get_db_instance)):
    """ Updates a bank details with specified parameters. """
    bank_details = db.update_bank_details(
        db=db_instance, bank_id=bank_details_id, bank_details=bank_details)
    if bank_details is None:
        raise HTTPException(404, detail="Bank details not found.")
    return bank_details


@router.delete("/{bank_details_id}", status_code=status.HTTP_200_OK)
def delete_bank_details(bank_details_id: int,
                        db_instance: Session = Depends(get_db_instance)):
    """ Deletes a bank details with specified ID. """
    is_delete_successfull = db.delete_bank_details(db=db_instance,
                                                   bank_id=bank_details_id)
    if not is_delete_successfull:
        raise HTTPException(404, detail="Bank details not found.")

    return {}
