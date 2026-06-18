import requests

login_api = "https://automationexercise.com/api/verifyLogin"
request_params_valid =  {"email" : "filip.gonda1@gmail.com",
                        "password" : "Test123"}

request_params_invalid =  {"email" : "filip.gonda1@gmail.com",
                        "password" : "Test12"}

import requests

def test_login_positive():

    response = requests.post(login_api, data = request_params_valid)

    assert response.status_code == 200
    assert response.json()["responseCode"] == 200
    assert response.json()["message"] == "User exists!"

def test_login_negative():

    response = requests.post(login_api, data=request_params_invalid)

    assert response.status_code == 200
    assert response.json()["responseCode"] == 404
    assert response.json()["message"] == "User not found!"

def test_login_no_params():

    response = requests.post(login_api)

    assert response.status_code == 200
    assert response.json()["responseCode"] == 400
    assert response.json()["message"] == "Bad request, email or password parameter is missing in POST request."