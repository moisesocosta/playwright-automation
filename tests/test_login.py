import pytest
from pages.login_page import LoginPage

test_data = [
    ("standard_user", "secret_sauce", True, None),
    ("locked_out_user", "secret_sauce", False, "Epic sadface: Sorry, this user has been locked out."),
    ("invalid_user", "secret_sauce", False, "Epic sadface: Username and password do not match any user in this service"),
    ("standard_user", "wrong_password", False, "Epic sadface: Username and password do not match any user in this service")
]

@pytest.mark.parametrize("username, password, should_pass, expected_error", test_data)
def test_login(page, username, password, should_pass, expected_error):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(username, password)

    if should_pass:
        # Verify successful login by checking URL
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    else:
        # Verify error message
        error = login_page.get_error_message()
        assert error == expected_error