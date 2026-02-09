from pages.base_page import BasePage
from pages.locators import cart_locators as loc


class CartPage(BasePage):

    page_url = '/shop/cart'

    def check_text_empty_cart(self):
        empty_text = self.get_text(loc.empty_title_loc)

        assert 'Your cart is empty!' in empty_text

    def check_cart_without_empty_text(self):
        self.open_page()
        assert 'Your cart is empty!' not in self.get_text(loc.empty_title_loc)

    def check_cart_total_is_displayed(self):
        cart_total = self.find(loc.cart_total_loc)
        assert cart_total.is_displayed()
