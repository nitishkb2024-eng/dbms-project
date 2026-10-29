import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Test that the homepage returns the correct campus connect success string."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to CampusConnect! DevOps CI/CD Deployment Successful" in response.data

def test_health_route(client):
    """Test that the health endpoint returns operational json data."""
    response = client.get('/health')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['status'] == "healthy"
