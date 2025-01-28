# Dados de login
LOGIN_CREDENTIALS = {
    "valid_user": {
        "username": "standard_user",
        "password": "secret_sauce"
    },
    "locked_user": {
        "username": "locked_out_user",
        "password": "secret_sauce"
    },
    "problem_user": {
        "username": "problem_user",
        "password": "secret_sauce"
    },
    "invalid_user": {
        "username": "invalid_user",
        "password": "wrong_password"
    }
}

# Dados de produtos
INVENTORY_ITEMS = {
    "backpack": {
        "name": "Sauce Labs Backpack",
        "price": 29.99,
        "description": "carry.allTheThings() with the sleek, streamlined Sly Pack"
    },
    "bike_light": {
        "name": "Sauce Labs Bike Light",
        "price": 9.99,
        "description": "A red light isn't the desired state in testing"
    },
    "bolt_shirt": {
        "name": "Sauce Labs Bolt T-Shirt",
        "price": 15.99,
        "description": "Get your testing superhero on with the Sauce Labs bolt T-shirt"
    }
}

# Opções de ordenação
SORT_OPTIONS = {
    "az": "az",  # Nome (A a Z)
    "za": "za",  # Nome (Z a A)
    "low_high": "lohi",  # Preço (menor para maior)
    "high_low": "hilo"   # Preço (maior para menor)
}

# Dados para checkout
CHECKOUT_DATA = {
    "valid_info": {
        "first_name": "John",
        "last_name": "Doe",
        "postal_code": "12345"
    },
    "invalid_info": {
        "first_name": "",
        "last_name": "",
        "postal_code": ""
    }
}

# Mensagens de erro
ERROR_MESSAGES = {
    "locked_out": "Epic sadface: Sorry, this user has been locked out.",
    "invalid_login": "Epic sadface: Username and password do not match any user in this service",
    "missing_username": "Epic sadface: Username is required",
    "missing_password": "Epic sadface: Password is required",
    "missing_firstname": "Error: First Name is required",
    "missing_lastname": "Error: Last Name is required",
    "missing_postal": "Error: Postal Code is required"
}

# URLs
URLS = {
    "base": "https://www.saucedemo.com",
    "inventory": "https://www.saucedemo.com/inventory.html",
    "cart": "https://www.saucedemo.com/cart.html",
    "checkout_step_one": "https://www.saucedemo.com/checkout-step-one.html",
    "checkout_step_two": "https://www.saucedemo.com/checkout-step-two.html",
    "checkout_complete": "https://www.saucedemo.com/checkout-complete.html"
}