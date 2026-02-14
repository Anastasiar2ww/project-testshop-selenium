from pages.base_page import BasePage
from pages.locators import cart_locators as loc


class CartPage(BasePage):

    page_url = '/shop/cart'

    def check_cart_text(self, expected_text):
        empty_text = self.get_text(loc.empty_title_loc)

        assert expected_text in empty_text

    def check_cart_without_empty_text(self, expected_text):
        self.open_page()
        assert expected_text not in self.get_text(loc.empty_title_loc)

    def check_cart_total_is_displayed(self):
        cart_total = self.find(loc.cart_total_loc)
        assert cart_total.is_displayed()
