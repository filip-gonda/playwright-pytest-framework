import requests

products_api = "https://automationexercise.com/api/productsList"


def test_get_all_products():

    response = requests.get(products_api)

    assert response.status_code == 200
    assert response.json()["responseCode"] == 200

    api_data = response.json()

    assert "products" in api_data

    for product in api_data["products"]:
        assert "id" in product
        assert "name" in product
        assert "price" in product
        assert "brand" in product
        assert "category" in product

def test_post_to_all_products ():

    response = requests.post(products_api)

    assert response.status_code == 200
    assert response.json()["responseCode"] == 405
    assert response.json()["message"] == "This request method is not supported."


