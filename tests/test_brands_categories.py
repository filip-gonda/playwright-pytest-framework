import pytest

from pages.main_page import MainPage
from data.expected_data import get_expected_categories, get_expected_brands
from pages.products_page import ProductsPage
from pages.product_page import ProductPage


def test_categories(setup):

    main_page = MainPage(setup)
    products_page = ProductsPage(setup)
    product_page = ProductPage(setup)
    left_sidebar = main_page.get_left_sidebar()

    # get categories from left sidebar
    actual_categories = left_sidebar.get_categories()

    # get expected categories
    expected_categories = get_expected_categories()

    for category, subcategories in expected_categories.items():

        # verify actual category with expected ones
        assert category in actual_categories

        for subcategory in subcategories:
            # verify actual subcategory in expected subcategories (subcategory is part of expected categories)
            assert subcategory in actual_categories[category]

            # click actual subcategory
            left_sidebar.click_subcategory(category.capitalize(), subcategory.capitalize())

            # verify page header (name of category in heading)
            products_page_header = products_page.get_products_header().capitalize()
            assert category.capitalize(), subcategory.capitalize() in products_page_header

            # get all category products
            category_products = products_page.get_product_cards()

            for category_product in category_products:

                #for each category product click product details
                category_product.click_view_product()

                # verify product category on product page
                assert subcategory == product_page.get_product_category()

                # go back
                left_sidebar.click_subcategory(category.capitalize(), subcategory.capitalize())


def test_brands(setup):

    main_page = MainPage(setup)
    products_page = ProductsPage(setup)
    product_page = ProductPage(setup)
    left_sidebar = main_page.get_left_sidebar()

    # get brands from left sidebar
    actual_brands = left_sidebar.get_brands()

    #get expected brands names
    expected_brands = get_expected_brands()

    assert left_sidebar.get_brands_heading() == "BRANDS"

    for brand, count in actual_brands.items():
        # compare actual brand with expected ones
        assert brand in expected_brands

        # click brand
        left_sidebar.click_brand(brand)

        # verify user was navigated to brands page
        assert brand in products_page.get_products_header().upper()

        # verify that amount of products on product page equals products count for brand in left sidebar
        assert products_page.get_product_card_count() == int(count)

        # get all brand products
        brand_products = products_page.get_product_cards()

        for product in brand_products:
            # for each brand product click product details
            product.click_view_product()

            # verify product brand on product page
            assert brand == product_page.get_product_brand().upper()

            # go back
            left_sidebar.click_brand(brand)









