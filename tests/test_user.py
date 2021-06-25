import requests

def test_get_user():
    response = requests.get("http://python:5000/?id=1")
    assert response.status_code == 200

def test_add_user():
    response = requests.post("http://python:5000/add",json={"id":77,"name":"test"})
    assert response.status_code == 200