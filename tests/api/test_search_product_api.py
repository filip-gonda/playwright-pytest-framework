import requests

search_product_api = "https://automationexercise.com/api/searchProduct"
body_request_param_positive = {"search_product": "Top"}
body_request_param_negative = {"search_product": "blabla"}

def test_post_to_search_product_api_positive():

    response = requests.post(search_product_api, data=body_request_param_positive)

    assert response.status_code == 200
    assert response.json()["responseCode"] == 200

    products = response.json()["products"]

    for product in products:
        name_match = body_request_param_positive["search_product"] in product["name"]
        category_match = body_request_param_positive["search_product"] in product["category"]["category"]

        assert name_match or category_match


def test_post_to_search_product_api_no_result():

    response = requests.post(search_product_api, data=body_request_param_negative)

    assert response.status_code == 200
    assert response.json()["responseCode"] == 200

    assert response.json()["products"] == []

def test_post_to_search_product_api_no_param():

    response = requests.post(search_product_api)

    assert response.status_code == 200
    assert response.json()["responseCode"] == 400
    assert response.json()["message"] == "Bad request, search_product parameter is missing in POST request."




