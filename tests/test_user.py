import requests

def test_get_user():
    response = requests.get("http://python:5000/users/1")
    assert response.status_code == 200

def test_add_user():
    response = requests.post("http://python:5000/users/",json={"nickname":"test-nickname","role":"test-role"})
    assert response.status_code == 200