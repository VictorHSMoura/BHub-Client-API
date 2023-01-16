import pytest

from fastapi.testclient import TestClient


def default_bank_details():
    return {
        "branch": "34103",
        "account": "27423610",
        "bank_name": "Caixa Econômica Federal"
    }


def default_response():
    return {
        "id": 1,
        "branch": "34103",
        "account": "27423610",
        "bank_name": "Caixa Econômica Federal"
    }


@pytest.fixture(scope="function")
def default_client(client: TestClient):
    default = {
        "corporate_name": "ABC Atacarejo",
        "phone": "3138642736",
        "address": "Rua 12, Lagoinha, Belo Horizonte",
        "register_date": "28/09/2020",
        "declared_billing": 15000.0,
        "bank_details": []
    }
    client.post("/clients", json=default)
    yield


def test_get_bank_details_without_insertion(client: TestClient,
                                            default_client: None):
    response = client.get("/bank_details")

    assert response.status_code == 200
    assert response.json() == []


def test_get_bank_details_after_insertion(client: TestClient,
                                          default_client: None):
    response = client.post("/bank_details/client/1",
                           json=default_bank_details())
    assert response.status_code == 201

    response = client.get("/bank_details")

    assert response.status_code == 200
    assert response.json() == [default_response()]


def test_get_bank_details_for_specific_client(client: TestClient,
                                              default_client: None):
    response = client.post("/bank_details/client/1",
                           json=default_bank_details())
    assert response.status_code == 201

    response = client.get("/bank_details/client/1")

    assert response.status_code == 200
    assert response.json() == [default_response()]

    response = client.get("/bank_details/client/2")

    assert response.status_code == 200
    assert response.json() == []


def test_get_bank_details_with_id(client: TestClient,
                                  default_client: None):
    client.post("/bank_details/client/1", json=default_bank_details())
    response = client.get("/bank_details/1")

    assert response.status_code == 200
    assert response.json() == default_response()


def test_get_bank_details_with_unexistent_id(client: TestClient,
                                             default_client: None):
    response = client.get("/bank_details/1")

    assert response.status_code == 404
    assert response.json() == {"detail": "Bank details not found."}


def test_add_invalid_bank_details(client: TestClient, default_client: None):
    invalid_bank_details = default_bank_details()
    invalid_bank_details["account"] = "3652-0"

    response = client.post("/bank_details/client/1", json=invalid_bank_details)

    assert response.status_code == 400


def test_update_bank_details(client: TestClient, default_client: None):
    client.post("/bank_details/client/1", json=default_bank_details())

    updated_bank_details = default_bank_details()
    updated_bank_details["bank_name"] = "Itaú Unibanco"

    response = client.put("/bank_details/1", json=updated_bank_details)
    assert response.status_code == 200

    response = client.get("/bank_details/1")

    updated_response = default_response()
    updated_response["bank_name"] = "Itaú Unibanco"

    assert response.status_code == 200
    assert response.json() == updated_response


def test_update_bank_details_with_invalid_parameter(client: TestClient,
                                                    default_client: None):
    client.post("/bank_details/client/1", json=default_bank_details())

    updated_bank_details = default_bank_details()
    updated_bank_details["branch"] = "765213-0"

    response = client.put("/bank_details/1", json=updated_bank_details)

    assert response.status_code == 400


def test_update_unexistent_bank_details(client: TestClient, default_client: None):
    response = client.put("/bank_details/1", json=default_bank_details())

    assert response.status_code == 404
    assert response.json() == {"detail": "Bank details not found."}


def test_update_id_not_possible(client: TestClient, default_client: None):
    client.post("/bank_details/client/1", json=default_bank_details())

    updated_bank_details = default_bank_details()
    updated_bank_details["id"] = 2

    client.put("/bank_details/1", json=updated_bank_details)

    response = client.get("/bank_details/1")

    assert response.status_code == 200
    assert response.json() == default_response()

    response = client.get("/bank_details/2")

    assert response.status_code == 404
    assert response.json() == {"detail": "Bank details not found."}


def test_delete_bank_details(client: TestClient, default_client: None):
    client.post("/bank_details/client/1", json=default_bank_details())

    response = client.delete("/bank_details/1")
    assert response.status_code == 200

    response = client.get("/bank_details/1")

    assert response.status_code == 404
    assert response.json() == {"detail": "Bank details not found."}


def test_delete_unexistent_bank_details(client: TestClient,
                                        default_client: None):
    response = client.delete("/bank_details/1")
    assert response.status_code == 404

    response = client.get("/bank_details/1")

    assert response.status_code == 404
    assert response.json() == {"detail": "Bank details not found."}
