from http.client import responses

import requests

brands_api = "https://automationexercise.com/api/brandsList"

def test_get_all_brands():

    response = requests.get(brands_api)

    assert response.status_code == 200
    assert response.json()["responseCode"] == 200

    brands = response.json()["brands"]

    for brand in brands:
        assert "id" in brand
        assert "brand" in brand

def test_put_to_brands():

    response = requests.put(brands_api)

    assert response.status_code == 200
    assert response.json()["responseCode"] == 405
    assert response.json()["message"] == "This request method is not supported."