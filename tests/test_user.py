import requests

def test_get_user():
    response = requests.get("http://python:5000/users/1")
    assert response.status_code == 200

def test_add_user():
    response = requests.post("http://python:5000/users/",json={"nickname":"test111112312____2123nickname","role":"test_role"})
    assert response.status_code == 200

def test_add_user_400_scace():
    response = requests.post("http://python:5000/users/",json={"nickname":"test nick_name12","role":"test-role"})
    assert response.status_code == 400

def test_add_user_400_dash():
    response = requests.post("http://python:5000/users/",json={"nickname":"test-nickn32ame","role":"test-role"})
    assert response.status_code == 400