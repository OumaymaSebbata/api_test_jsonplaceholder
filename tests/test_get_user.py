
from typing import Any
import pytest
from pytest import mark


from utils.apis import APIs
@mark.user
def test_get_user(load_user_data):
    json_body = load_user_data.copy()
    response = APIs.apis("GET","users",json_body)
    #print("response = ", response.json())
    response_code = response.status_code
    assert response_code ==200 ,f"response code is {response_code}"
    print("HERE IS THE USER")
#hi hello oumayma

@mark.createUser
def test_create_user(load_user_data):
    json_body = load_user_data.copy()
    json_body['email']="hello@test.com"
    response = APIs.apis("POST","users",json_body)
    #print("response = ", response.json())
    response_code = response.status_code
    assert response_code ==201 , f"response code is {response_code}"
    assert len(response.json())>0
    print("USER IS CREATED")

@mark.deleteUser
def test_delete_user(load_user_data):
    json_body = load_user_data.copy()

    response = APIs.apis("delete","users/1",json_body)
    #print("response = ", response.json())
    response_code = response.status_code
    assert response_code == 200 , f"response code is {response_code}"
    print('USER IS DELETED ')

@mark.UpdateUser
def test_update_user(load_user_data):
    json_body = load_user_data.copy()

    response = APIs.apis("POST","users",json_body)
    #print("response = ", response.json())
    response_code = response.status_code
    assert response_code == 201 , f"response code is {response_code}"
    print('SECOND USER IS DELETED ')

