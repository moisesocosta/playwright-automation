import pytest
from playwright.sync_api import expect
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.test_data import LOGIN_CREDENTIALS, INVENTORY_ITEMS, SORT_OPTIONS

def test_add_item_to_cart(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    item = INVENTORY_ITEMS["backpack"]
    
    # Adiciona item ao carrinho
    inventory.add_item_to_cart(item["name"])
    
    # Verifica contagem do carrinho
    assert inventory.get_cart_count() == "1"
    
    # Verifica se o botão mudou para "Remove"
    remove_button = logged_in_page.locator(f'.inventory_item:has-text("{item["name"]}") button')
    expect(remove_button).to_have_text("Remove")

def test_sort_items_price_high_to_low(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    
    # Ordena por preço (maior para menor)
    inventory.sort_items(SORT_OPTIONS["high_low"])
    
    # Pega os preços dos itens
    prices = logged_in_page.locator('.inventory_item_price').all_text_contents()
    prices = [float(price.replace('$', '')) for price in prices]
    
    # Verifica se os preços estão em ordem decrescente
    assert prices == sorted(prices, reverse=True), "Items are not sorted by price high to low"

def test_sort_items_name_az(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    
    # Ordena por nome (A a Z)
    inventory.sort_items(SORT_OPTIONS["az"])
    
    # Pega os nomes dos itens
    names = logged_in_page.locator('.inventory_item_name').all_text_contents()
    
    # Verifica se os nomes estão em ordem alfabética
    assert names == sorted(names), "Items are not sorted alphabetically A to Z"
