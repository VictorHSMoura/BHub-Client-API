from fastapi import APIRouter, HTTPException

from typing import List
from models.api import Client as ClientModel, Bank as BankModel

router = APIRouter(
    prefix="/clients",
    tags=["clients"],
    responses={404: {"description": "Not found"}},
)


# Returns all users
@router.get("/")
async def get_users() -> List[ClientModel]:
    try:
        default_user = ClientModel(
            corporate_name="ABC Atacarejo",
            phone="3138642736",
            address="Rua 12, Lagoinha, Belo Horizonte",
            register_date="28/09/2020",
            declared_billing=15000,
            bank_details=[
                BankModel(
                    branch="34103",
                    account="27423610",
                    bank_name="Caixa Econômica Federal"
                )
            ]
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=f"Bad Request: {repr(error)}")

    return [default_user]
