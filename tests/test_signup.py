import random
import string

def random_email():
    return f"testuser_{''.join(random.choices(string.ascii_lowercase, k=6))}@mergington.edu"

def test_signup_success(client):
    # Arrange
    email = random_email()
    activity = "Chess Club"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    assert f"Signed up {email} for {activity}" in response.json().get("message", "")

def test_signup_duplicate(client):
    # Arrange
    email = random_email()
    activity = "Programming Class"
    # First signup
    client.post(f"/activities/{activity}/signup?email={email}")

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 400
    assert "already signed up" in response.json().get("detail", "")

def test_signup_activity_not_found(client):
    # Arrange
    email = random_email()
    activity = "Nonexistent Club"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 404
    assert "Activity not found" in response.json().get("detail", "")
