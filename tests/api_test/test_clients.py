from fastapi.testclient import TestClient


def test_get_clients(client: TestClient):
    response = client.get("/clients")

    assert response.status_code == 200
    assert response.json() == [
        {
            "corporate_name": "ABC Atacarejo",
            "phone": "3138642736",
            "address": "Rua 12, Lagoinha, Belo Horizonte",
            "register_date": "2020-09-28",
            "declared_billing": 15000.0,
            "bank_details": [
                {
                    "branch": "34103",
                    "account": "27423610",
                    "bank_name": "Caixa Econômica Federal"
                }
            ]
        }
    ]
