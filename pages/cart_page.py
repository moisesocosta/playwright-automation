class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator('.cart_item')
        self.checkout_button = page.locator('[data-test="checkout"]')
        self.continue_shopping = page.locator('[data-test="continue-shopping"]')
        
    def navigate(self):
        self.page.click('.shopping_cart_link')
        
    def remove_item(self, item_name: str):
        item = self.page.locator(f'.cart_item:has-text("{item_name}")')
        remove_button = item.locator('button:has-text("Remove")')
        remove_button.click()
        
    def proceed_to_checkout(self):
        self.checkout_button.click()