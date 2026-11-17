from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_crud_flow():
    # 1. POST (Create item)
    response = client.post("/items/1", json={"name": "Laptop", "price": 999.99})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Laptop", "price": 999.99}

    # 2. GET (Read item)
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Laptop"

    # 3. PUT (Update item)
    response = client.put("/items/1", json={"name": "Gaming Laptop", "price": 1299.99})
    assert response.status_code == 200
    assert response.json()["price"] == 1299.99

    # 4. DELETE (Remove item)
    response = client.delete("/items/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Item deleted"}

    # 5. Verify item is gone
    response = client.get("/items/1")
    assert response.status_code == 404
