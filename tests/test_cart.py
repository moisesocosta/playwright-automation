import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.test_data import LOGIN_CREDENTIALS, INVENTORY_ITEMS, URLS

def test_add_and_remove_from_cart(page):
    # Login
    login_page = LoginPage(page)
    login_page.navigate()
    credentials = LOGIN_CREDENTIALS["valid_user"]
    login_page.login(credentials["username"], credentials["password"])
    
    # Adicionar ao carrinho
    inventory = InventoryPage(page)
    item = INVENTORY_ITEMS["backpack"]
    inventory.add_item_to_cart(item["name"])
    
    # Verificar quantidade no carrinho
    assert inventory.get_cart_count() == "1"
    
    # Verificar e remover do carrinho
    cart = CartPage(page)
    cart.navigate()
    expect(page).to_have_url(URLS["cart"])
    cart.remove_item(item["name"])
    
    # Verificar se o item foi removido (o badge do carrinho deve desaparecer)
    expect(page.locator('.shopping_cart_badge')).not_to_be_visible()
