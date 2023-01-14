from fastapi import APIRouter, HTTPException, Depends, status
from models.api import ClientAPIModel
from typing import List

from sqlalchemy.orm import Session
import db.clients as db
from db.sqlalchemy_db import get_db_instance

router = APIRouter(
    prefix="/clients",
    tags=["clients"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[ClientAPIModel],
            status_code=status.HTTP_200_OK)
def get_users(db_instance: Session = Depends(get_db_instance)):
    """ Returns a list with all registered clients. """
    clients = db.return_all_clients(db=db_instance)
    return clients


@router.get("/{client_id}", response_model=ClientAPIModel,
            status_code=status.HTTP_200_OK)
def get_users_with_id(client_id: int,
                      db_instance: Session = Depends(get_db_instance)):
    """ Returns a client with the specified id. """
    client = db.return_client_with_specified_id(
        db=db_instance, client_id=client_id)
    if client is None:
        raise HTTPException(404, detail="Client not found.")
    return client


@router.post("/", response_model=ClientAPIModel,
             status_code=status.HTTP_201_CREATED)
def creates_new_client(client: ClientAPIModel,
                       db_instance: Session = Depends(get_db_instance)):
    """ Creates a client with specified parameters. """
    client = db.create_client(db=db_instance, client=client)
    if client is None:
        raise HTTPException(500, detail="Unexpected error on client creation.")
    return client


@router.put("/{client_id}", response_model=ClientAPIModel,
            status_code=status.HTTP_200_OK)
def update_client(client_id: int, client: ClientAPIModel,
                  db_instance: Session = Depends(get_db_instance)):
    """ Updates a client with specified parameters. """
    client = db.update_client(db=db_instance, client_id=client_id,
                              client=client)
    if client is None:
        raise HTTPException(404, detail="Client not found.")
    return client


@router.delete("/{client_id}", status_code=status.HTTP_200_OK)
def delete_client(client_id: int,
                  db_instance: Session = Depends(get_db_instance)):
    """ Deletes a client with specified ID. """
    is_delete_successfull = db.delete_client(db=db_instance,
                                             client_id=client_id)
    if not is_delete_successfull:
        raise HTTPException(404, detail="Client not found.")

    return {}
