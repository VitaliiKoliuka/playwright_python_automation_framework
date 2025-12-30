from venv import logger
import pytest
from automation_project.page_objects.login_page import LoginPage
from automation_project.page_objects.main_page import MainPage
from automation_project.helper.config import URL
from automation_project.helper.utils import log_message, LogLevel
from automation_project.helper.validation import AppValidation


@pytest.fixture()
def setup_playwright(playwright, request):
    headed = request.config.getoption("--headed", default=False)
    browser = playwright.chromium.launch(headless=not headed)
    page = browser.new_page()
    try:
        yield page
    finally:
        log_message(logger,"closing browser", LogLevel.INFO)
        browser.close()

@pytest.fixture()
def setup_login_page(setup_playwright):
    login_page = LoginPage(setup_playwright)
    login_page.navigate_to(URL)
    login_page.accept_cookies_if_present()
    log_message(logger, f"navigate to {URL}", LogLevel.INFO)
    yield login_page

@pytest.fixture()
def setup_all_pages(setup_playwright):
    login_page = LoginPage(setup_playwright)
    main_page = MainPage(setup_playwright)
    yield login_page, main_page

@pytest.fixture()
def validation(setup_all_pages):
    yield AppValidation(setup_all_pages)