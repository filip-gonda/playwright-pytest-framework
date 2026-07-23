import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, Page

from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.signin_register_page import SignInRegisterPage

load_dotenv()

base_url = os.getenv("BASE_URL")
email = os.getenv("EMAIL")
pw = os.getenv("PASSWORD")
headless = os.getenv("HEADLESS", "true").lower() == "true"
test_id = os.getenv("TESTID")

BLOCKED = [
    "googlesyndication.com",
    "doubleclick.net",
    "googleadservices.com",
    "adservice.google.com",
    "adtrafficquality.google",
]


def block_ads(page: Page):
    """Abort any request going to an ad domain, let everything else through."""
    def handler(route):
        if any(domain in route.request.url for domain in BLOCKED):
            route.abort()
        else:
            route.continue_()
    page.route("**/*", handler)


@pytest.fixture(scope="function")
def setup():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=headless)
    page = browser.new_page()
    playwright.selectors.set_test_id_attribute(test_id)

    block_ads(page)          # <-- must come BEFORE main_page.start()

    main_page = MainPage(page)
    main_page.start()

    header = main_page.get_header()
    header.click_login()

    login_page = SignInRegisterPage(page)
    assert login_page.get_login_header() == "Login to your account"
    login_page.enter_mail(email)
    login_page.enter_password(pw)
    login_page.click_login_button()

    yield page
    browser.close()
    playwright.stop()


@pytest.fixture(scope="function")
def empty_cart(setup):
    page = setup             # reuse the logged-in page from setup

    main_page = MainPage(page)
    cart_page = CartPage(page)
    header = main_page.get_header()

    header.click_cart()
    cart = cart_page.get_cart()
    cart.delete_cart_products()
    header.click_home()

    yield page               # no teardown needed - setup closes the browser


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("setup") or item.funcargs.get("empty_cart")
        if page:
            os.makedirs("screenshots", exist_ok=True)
            page.screenshot(path=f"screenshots/{item.name}.png", full_page=True)