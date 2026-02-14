from pages.base_page import BasePage
from pages.locators import product_card_locators as loc

class ProductCardPage(BasePage):

    page_url = 'shop/furn-9999-office-design-software-7?category=9'

    def check_click_add_to_cart(self):
        self.find(loc.btn_add_to_cart_loc).click()
        self.wait_for_text_in_element(loc.cart_icon_counter_loc, '1')

    def check_toast_after_adding(self):
        self.wait_until_visible(loc.toast_text_loc)
        toast_test = self.get_text(loc.toast_text_loc)
        assert toast_test == 'Item(s) added to your cart'

    def check_terms_in_link_href(self):
        link = self.find(loc.link_loc)
        href = link.get_attribute("href")
        assert "/terms" in href

    def check_increase_count(self, expected_count: int):
        expected = str(expected_count)
        increase_count = self.find(loc.btn_increase_loc)
        increase_count.click()

        self.wait_for_value_in_element(loc.quantity_form_loc, expected, timeout=5)
        value = self.find(loc.quantity_form_loc).get_attribute('value')

        assert value == expected
