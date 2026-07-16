from playwright.sync_api import Page
from components.cart import CartComponent

class CheckOutPage():
    def __init__(self, page: Page):
        self.delivery_data = page.locator("#address_delivery li")
        self.cart_header = page.locator("thead > tr")
        self.cart_table_products = page.locator("tbody > tr")
        self.place_order_button = page.locator("a").filter(has_text="Place Order")
        self.cart = page.locator(".cart_info")

    def get_delivery_address_count(self):
        return self.delivery_data.count()

    def get_delivery_address(self):
        # return dict with address information
        address = {"name": self.delivery_data.nth(1).inner_text().strip(),
                   "address1": self.delivery_data.nth(2).inner_text().strip(),
                   "address2": self.delivery_data.nth(3).inner_text().strip(),
                   "house_number": self.delivery_data.nth(4).inner_text().strip(),
                   "full_address": self.delivery_data.nth(5).inner_text().strip(),
                   "state": self.delivery_data.nth(6).inner_text().strip(),
                   "phone_number": self.delivery_data.nth(7).inner_text().strip()
        }
        return address

    def get_cart(self):
        return CartComponent(self.cart)

    def click_place_order_button(self):
        self.place_order_button.click()



