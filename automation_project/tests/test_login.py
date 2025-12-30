import pytest

from automation_project.helper.config import VALID_CREDENTIALS
from automation_project.helper.validation import AppValidation

def test_successfully_login(setup_login_page, validation):
    login_page = setup_login_page
    login_page.perform_login(VALID_CREDENTIALS["email"],VALID_CREDENTIALS["password"])
    validation.validate_logged_in()




@pytest.mark.parametrize(
    "username, password, error_message",
    [
        ("wrong_username_template","valid_password","isn't connected to an account."),
        ("valid_username","wrong_password","isn't connected to an account."),
        ("", "valid_password","isn't connected to an account."),
        ("valid_username","","isn't connected to an account.")

    ])
def test_invalid_login_and_verify_error_message(setup_login_page,validation, username, password, error_message):
    login_page = setup_login_page
    login_page.perform_login(username, password)
    validation.validate_failed_login(error_message)