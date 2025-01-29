import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from utils.test_data import LOGIN_CREDENTIALS, ERROR_MESSAGES, URLS

# Dados de teste usando as constantes do test_data.py
test_data = [
    (
        LOGIN_CREDENTIALS["valid_user"]["username"],
        LOGIN_CREDENTIALS["valid_user"]["password"],
        True,
        None
    ),
    (
        LOGIN_CREDENTIALS["locked_user"]["username"],
        LOGIN_CREDENTIALS["locked_user"]["password"],
        False,
        ERROR_MESSAGES["locked_out"]
    ),
    (
        LOGIN_CREDENTIALS["invalid_user"]["username"],
        LOGIN_CREDENTIALS["invalid_user"]["password"],
        False,
        ERROR_MESSAGES["invalid_login"]
    ),
    (
        LOGIN_CREDENTIALS["valid_user"]["username"],
        "wrong_password",
        False,
        ERROR_MESSAGES["invalid_login"]
    )
]

@pytest.mark.parametrize("username, password, should_pass, expected_error", test_data)
def test_login(page, username, password, should_pass, expected_error):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(username, password)

    if should_pass:
        # Verify successful login by checking URL
        expect(page).to_have_url(URLS["inventory"])
    else:
        # Verify error message
        error = login_page.get_error_message()
        assert error == expected_error