from playwright.sync_api import Page

class ProductComponent:
    def __init__(self, root_locator, page: Page):
        self.page = Page
        self.root = root_locator

    def get_product_name(self):
        return self.root.locator(".productinfo p").inner_text().strip()

    def get_product_price(self):
        return self.root.locator(".productinfo h2").inner_text().replace("Rs. ", "").strip()

    def is_product_image_loaded(self):
        img = self.root.locator(".productinfo img")
        img.wait_for(state="visible", timeout=5000)
        natural_width = img.evaluate("img => img.naturalWidth")

        if natural_width > 0:
            return True

        return False

    def click_view_product(self):
        self.root.locator(".choose a").click()


    def click_add_to_cart(self):
        self.root.locator(".productinfo a").click()

