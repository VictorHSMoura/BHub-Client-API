from fastapi import APIRouter, HTTPException

from typing import List
from models.api import ClientAPIModel
import db.clients as db

router = APIRouter(
    prefix="/clients",
    tags=["clients"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[ClientAPIModel])
async def get_users():
    """ Returns a list with all registered clients. """
    clients = db.return_all_clients()
    return clients


@router.get("/{client_id}", response_model=ClientAPIModel)
async def get_users_with_id(client_id: int):
    """ Returns a client with the specified id. """
    client = db.return_client_with_specified_id(client_id=client_id)
    if client is None:
        raise HTTPException(404, detail="Client not found.")
    return client
