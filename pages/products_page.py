from playwright.sync_api import Page, expect
from utils.text_utils import clean_text
from data.data_generator import get_random_product
from components.product import ProductComponent
import csv
from components.cart_modal import CartModalComponent

class ProductsPage():
    def __init__(self, page: Page):
        self.page = page
        self.products_cards = page.locator(".features_items .product-image-wrapper")
        self.view_product_button = page.locator(".features_items .choose li > a").first
        self.search_product_field = page.locator("#advertisement #search_product")
        self.search_button = page.locator("#advertisement #submit_search")
        self.searched_products_header = page.locator(".features_items > h2")
        self.cart_modal = page.locator("#cartModal .modal-content")

    def get_products_header(self):
        return self.page.locator(".features_items > h2").inner_text().strip().lower()

    def get_product_card_count(self):
        return self.products_cards.count()

    def get_product_cards(self):
        products = []
        count = self.get_product_card_count()

        ## create ProductComponent for all products visible on page
        for i in range(count):
            product = self.products_cards.nth(i)
            products.append(ProductComponent(product, Page))
        return products

    def search_product(self, product_to_search):
        self.search_product_field.fill(product_to_search)
        self.search_button.click()


    def get_cart_modal(self, go_to_cart = False):
        return CartModalComponent(self.cart_modal)













    def scrap_product_data(self):

        count = self.get_product_card_count()
        data = []
        for i in range(count):

            product = self.page.locator(".features_items .productinfo").nth(i)
            name = product.locator("p").inner_text()
            price = product.locator("h2").inner_text()
            data.append([name, price])

        with open("data/products_data.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "price"])
            writer.writerows(data)






