# tests/test_users.py


def test_get_users_empty(client):
    """
    Test GET /users with no users in database.
    """
    # Act
    response = client.get("/users")
    
    # Assert
    assert response.status_code == 200
    assert response.json() == []


def test_create_user(client):
    """
    Test POST /users creates a user and returns it.
    """
    # Arrange
    user_data = {
        "email": "test@example.com",
        "name": "testuser"
    }
    
    # Act
    response = client.post("/users", json=user_data)
    
    # Assert
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "test@example.com"
    assert data["name"] == "testuser"
    assert "id" in data


def test_get_user_by_id(client):
    """
    Test GET /users/{id} returns a specific user.
    """
    # Arrange: create a user first
    user_data = {"email": "alice@example.com", "name": "alice"}
    create_response = client.post("/users", json=user_data)
    user_id = create_response.json()["id"]
    
    # Act
    response = client.get(f"/users/{user_id}")
    
    # Assert
    assert response.status_code == 200
    assert response.json()["name"] == "alice"


def test_get_user_not_found(client):
    """
    Test GET /users/{id} returns 404 for non-existent user.
    Verifies exception handler works correctly.
    """
    # Act
    response = client.get("/users/99999")
    
    # Assert
    assert response.status_code == 404
    assert "detail" in response.json()

def test_delete_user_by_id(client):
    # Arrange: create a user first
        user_data = {"email": "alice2@example.com", "name": "alice"}
        create_response = client.post("/users", json=user_data)
        user_id = create_response.json()["id"]
        
        # Act
        response = client.delete(f"/users/{user_id}")

        assert response.status_code == 200