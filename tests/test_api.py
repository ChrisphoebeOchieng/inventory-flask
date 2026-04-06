import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_get_inventory(client):
    res = client.get("/inventory")
    assert res.status_code == 200

def test_add_item(client):
    res = client.post("/inventory", json={
        "product_name": "Test",
        "price": 100,
        "stock": 5,
        "barcode": "123"
    })
    assert res.status_code == 201