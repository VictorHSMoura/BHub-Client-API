from fastapi import APIRouter

router = APIRouter(
    prefix="/clients",
    tags=["clients"],
    responses={404: {"description": "Not found"}},
)


# Returns all users
@router.get("/")
async def get_users():
    default_user = {
        "corporate_name": "ABC Atacarejo",
        "phone": "31 38642736",
        "address": "Rua 12, Lagoinha, Belo Horizonte",
        "register_date": "28/09/2020",
        "declared_billing": "15000",
        "bank_details": [
            {
                "branch": "34103",
                "account": "27423610",
                "bank_name": "Caixa Econômica Federal"
            }
        ]
    }
    return [default_user]
