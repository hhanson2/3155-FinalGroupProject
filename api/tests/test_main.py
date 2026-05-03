from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_create_resource():
    response = client.post("/resources/", json={"item": "bread", "amount": 10})
    assert response.status_code == 200
    assert response.json()["item"] == "bread"

    # Cleanup
    resource_id = response.json()["id"]
    client.delete(f"/resources/{resource_id}")


