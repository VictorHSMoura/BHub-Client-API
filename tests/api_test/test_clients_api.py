from fastapi.testclient import TestClient

default_client = {
    "corporate_name": "ABC Atacarejo",
    "phone": "3138642736",
    "address": "Rua 12, Lagoinha, Belo Horizonte",
    "register_date": "28/09/2020",
    "declared_billing": 15000.0,
    "bank_details": [
        {
            "branch": "34103",
            "account": "27423610",
            "bank_name": "Caixa Econômica Federal"
        }
    ]
}

default_response = {
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


def test_get_clients_without_insertion(client: TestClient):
    response = client.get("/clients")

    assert response.status_code == 200
    assert response.json() == []


def test_add_new_client(client: TestClient):
    response = client.post("/clients", json=default_client)

    assert response.status_code == 200
    assert response.json() == default_response


def test_get_clients_after_insertion(client: TestClient):
    client.post("/clients", json=default_client)
    response = client.get("/clients")

    assert response.status_code == 200
    assert response.json() == [default_response]


def test_get_client_with_id(client: TestClient):
    client.post("/clients", json=default_client)
    response = client.get("/clients/1")

    assert response.status_code == 200
    assert response.json() == default_response


def test_get_client_with_unexistent_id(client: TestClient):
    response = client.get("/clients/1")

    assert response.status_code == 404
    assert response.json() == {"detail": "Client not found."}
