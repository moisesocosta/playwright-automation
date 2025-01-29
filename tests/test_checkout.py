import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.test_data import LOGIN_CREDENTIALS, CHECKOUT_DATA, INVENTORY_ITEMS, ERROR_MESSAGES, URLS

def test_complete_purchase(page):
    # Login
    login_page = LoginPage(page)
    login_page.navigate()
    credentials = LOGIN_CREDENTIALS["valid_user"]
    login_page.login(credentials["username"], credentials["password"])
    
    # Adicionar item ao carrinho
    inventory = InventoryPage(page)
    inventory.add_item_to_cart(INVENTORY_ITEMS["backpack"]["name"])
    
    # Ir para o checkout
    cart = CartPage(page)
    cart.navigate()
    cart.proceed_to_checkout()
    
    # Completar informações e finalizar
    checkout = CheckoutPage(page)
    info = CHECKOUT_DATA["valid_info"]
    checkout.fill_information(
        info["first_name"],
        info["last_name"],
        info["postal_code"]
    )
    checkout.complete_purchase()
    
    # Verificar se chegou à página de confirmação
    expect(page).to_have_url(URLS["checkout_complete"])
