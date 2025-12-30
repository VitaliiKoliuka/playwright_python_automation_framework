from playwright.sync_api import expect
from automation_project.page_objects.base_page import BasePage
from automation_project.helper.utils import take_screenshot, log_message, LogLevel


class AppValidation(BasePage):
    def __init__(self, setup_all_pages):
        self.login_page, self.main_page = setup_all_pages
        super().__init__(self.login_page.page)



    def validate_logged_in(self):
        login_button = self.login_page.login_button
        try:
            expect(login_button).not_to_be_visible(), "failed to login"
        except Exception as e:
            log_message(self.logger,"login failed", LogLevel.ERROR)
            take_screenshot(self.page, "login failed")
            raise AssertionError("Login failed") from e


    def validate_failed_login(self, expected_error_message):
        login_button = self.login_page.login_button
        error_message = self.login_page.get_error_message(expected_error_message)

        try:
            expect(login_button).to_be_visible(), "login button was expected to be hidden, but it was visible"
            expect(error_message).to_be_visible(), "login button was expected to be hidden, but it was visible"
        except Exception as e:
            log_message(self.logger,"login button failed to be visible", LogLevel.ERROR)
            take_screenshot(self.page, "login_button_visible")
            raise AssertionError(
                "Expected login button to be visible after failed login"
            ) from e





