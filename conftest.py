import pytest
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.signin_register_page import SignInRegisterPage
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os

load_dotenv()

base_url = os.getenv("BASE_URL")
email = os.getenv("EMAIL")
pw = os.getenv("PASSWORD")
headless = os.getenv("HEADLESS")
test_id = os.getenv("TESTID")


@pytest.fixture(scope="function")
def setup():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    playwright.selectors.set_test_id_attribute(test_id)


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
def empty_cart():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    playwright.selectors.set_test_id_attribute(test_id)

    main_page = MainPage(page)
    cart_page = CartPage(page)
    header = main_page.get_header()


    main_page.start()
    header.click_login()

    login_page = SignInRegisterPage(page)

    assert login_page.get_login_header() == "Login to your account"

    login_page.enter_mail(email)
    login_page.enter_password(pw)
    login_page.click_login_button()

    header.click_cart()

    cart = cart_page.get_cart()
    cart.delete_cart_products()
    header.click_home()

    yield page
    browser.close()
    playwright.stop()

import os
import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("setup") or item.funcargs.get("empty_cart")

        if page:
            os.makedirs("screenshots", exist_ok=True)
            page.screenshot(
                path=f"screenshots/{item.name}.png",
                full_page=True
            )
