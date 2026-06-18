from components.cart import CartComponent
from components.footer import FooterComponent

from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page: Page):
        self.cart = page.locator(".cart_info")
        self.proceed_button = page.locator("#do_action .btn-default")
        self.footer = page.locator("#footer")

    def get_cart(self):
        return CartComponent(self.cart)

    def click_proceed_button(self):
        self.proceed_button.click()

    def get_footer(self):
        return FooterComponent(self.footer)









