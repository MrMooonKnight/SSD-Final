import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test that the home page returns 200 OK"""
    rv = client.get('/')
    assert rv.status_code == 200