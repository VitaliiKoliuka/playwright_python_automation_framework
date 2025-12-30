import allure
from playwright.sync_api import Page
from automation_project.page_objects.base_page import BasePage
from automation_project.page_objects.main_page import MainPage
from automation_project.helper.utils import log_message, LogLevel, take_screenshot


class LoginPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)
        self.username_field = self.page.locator("[name = 'email']")
        self.password_field = self.page.locator("[name='pass']")
        self.login_button = self.page.locator("[name = 'login']")
        self.error_message = self.page.locator("//div[@id='email_container']")

    def accept_cookies_if_present(self):
        cookie_button = self.page.get_by_role(
            "button", name="Allow all cookies"
        )

        try:
            if cookie_button.is_visible(timeout=3000):
                cookie_button.click()
        except Exception:
            # Cookie popup not present – safe to ignore
            pass

    def get_error_message(self, expected_error_message):
        return self.page.locator(
            f'//div[contains(text(), "{expected_error_message}")]'
        )

    @allure.step("login")
    def perform_login(self, username: str, password: str) -> MainPage | None:
        log_message(self.logger,"performing login",level=LogLevel.INFO)
        self.type_text(self.username_field, username)
        self.type_text(self.password_field, password)
        self.click_element(self.login_button)
        if self.login_button.is_visible():
            log_message(self.logger, "Login failed", level=LogLevel.ERROR)
            take_screenshot(self.page, "login_failed")
            return None

        return MainPage(self.page)