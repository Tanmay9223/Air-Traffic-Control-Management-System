import pytest
import importlib

@pytest.fixture
def client():
    app_module = importlib.import_module('2')
    app = app_module.app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_login_wrong_username(client):
    response = client.post('/index', data={'fname': 'wrong', 'lname': '12345'})
    assert response.data == b'Wrong username!'

def test_login_wrong_password(client):
    response = client.post('/index', data={'fname': 'user', 'lname': 'wrong'})
    assert response.data == b'Wrong password!'

def test_login_wrong_both(client):
    response = client.post('/index', data={'fname': 'wrong', 'lname': 'wrong'})
    assert response.data == b'Wrong username and password'
