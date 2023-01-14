from fastapi.testclient import TestClient


def default_client():
    return {
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


def default_response():
    return {
        "id": 1,
        "corporate_name": "ABC Atacarejo",
        "phone": "3138642736",
        "address": "Rua 12, Lagoinha, Belo Horizonte",
        "register_date": "2020-09-28",
        "declared_billing": 15000.0,
        "bank_details": [
            {
                "id": 1,
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


def test_get_clients_after_insertion(client: TestClient):
    client.post("/clients", json=default_client())
    response = client.get("/clients")

    assert response.status_code == 200
    assert response.json() == [default_response()]


def test_add_invalid_client(client: TestClient):
    invalid_client = default_client()
    invalid_client["phone"] = "34+557398"

    response = client.post("/clients", json=invalid_client)

    assert response.status_code == 400


def test_get_client_with_id(client: TestClient):
    client.post("/clients", json=default_client())
    response = client.get("/clients/1")

    assert response.status_code == 200
    assert response.json() == default_response()


def test_get_client_with_unexistent_id(client: TestClient):
    response = client.get("/clients/1")

    assert response.status_code == 404
    assert response.json() == {"detail": "Client not found."}


def test_update_client(client: TestClient):
    client.post("/clients", json=default_client())

    updated_client = default_client()
    updated_client["declared_billing"] = 20000.00
    
    client.put("/clients/1", json=updated_client)

    response = client.get("/clients/1")

    updated_response = default_response()
    updated_response["declared_billing"] = 20000.00

    assert response.status_code == 200
    assert response.json() == updated_response


def test_update_client_with_invalid_parameter(client: TestClient):
    client.post("/clients", json=default_client())

    updated_client = default_client()
    updated_client["register_date"] = "/09/2020"
    
    response = client.put("/clients/1", json=updated_client)

    assert response.status_code == 400

def test_update_id_not_possible(client: TestClient):
    client.post("/clients", json=default_client())

    updated_client = default_client()
    updated_client["id"] = 2
    
    client.put("/clients/1", json=updated_client)

    response = client.get("/clients/1")

    assert response.status_code == 200
    assert response.json() == default_response()