from playwright.sync_api import Page, expect

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_badge = page.locator('.shopping_cart_badge')
        self.sort_dropdown = page.locator('[data-test="product_sort_container"]')
        self.inventory_items = page.locator('.inventory_item')
        
    def add_item_to_cart(self, item_name: str):
        item = self.page.locator(f'.inventory_item:has-text("{item_name}")')
        add_button = item.locator('button:has-text("Add to cart")')
        add_button.click()
        
    def get_cart_count(self) -> str:
        return self.cart_badge.text_content()
        
    def sort_items(self, sort_option: str):
        self.sort_dropdown.select_value(sort_option)