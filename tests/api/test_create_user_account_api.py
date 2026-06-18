import requests
from data.data_generator import get_register_user_form_data

create_account_api = "https://automationexercise.com/api/createAccount"

def test_create_account_positive():

    response = requests.post(create_account_api, data=get_register_user_form_data())

    assert response.status_code == 200
    assert response.json()["responseCode"] == 201
    assert response.json()["message"] == "User created!"

