from asyncio import wait_for

from pages.main_page import MainPage
from pages.products_page import ProductsPage
from pages.product_page import ProductPage
from conftest import setup
from pages.base_page import BasePage
from data.expected_data import get_product_names
from data.expected_data import get_products_count
from data.expected_data import get_product_prices

def test_verify_all_products_and_product_detail_page(setup):
    ## classes
    base_page = BasePage(setup)
    main_page = MainPage(setup)
    products_page = ProductsPage(setup)
    product_page = ProductPage(setup)
    header = main_page.get_header()

    ## navigate to products page
    header.click_products()

    ## verify page title and heading
    assert base_page.get_title() == "Automation Exercise - All Products"
    assert products_page.get_products_header().upper() == "ALL PRODUCTS"

    #verify all products loaded correctly
    assert products_page.get_product_card_count() == get_products_count()

    # get actual and expected data
    actual_products = products_page.get_product_cards()
    expected_products_names = get_product_names()
    expected_product_prices = get_product_prices()

    # compare actual and expected data
    for product in actual_products:

        # compare product name
        product_name = product.get_product_name()
        assert product_name in expected_products_names

        #compare product price
        product_price = product.get_product_price()
        assert product_price in expected_product_prices

        ##check if product image loaded correctly
        assert product.is_product_image_loaded() == True

        ## open product page for product
        product.click_view_product()

        ##compare product data with product page
        assert product_page.get_product_name() == product_name
        assert product_page.get_product_price() == product_price
        assert product_page.is_image_loaded() == True

        ##go back to products page
        header.click_products()




