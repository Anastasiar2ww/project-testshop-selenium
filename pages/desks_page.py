from pages.base_page import BasePage
from pages.locators import desks_locators as loc


class DesksPage(BasePage):
    page_url = 'shop/category/desks-1'

    def check_breadcrumbs_text(self, text):
        breadcrumbs = self.find(loc.breadcrumbs_desk_loc)
        assert breadcrumbs.text == text

    def check_cart_icon_enable(self):
        cart_icon = self.find(loc.cart_icon_loc)
        cart_icon.is_enabled()

    def check_count_of_elements_legs(self):
        elements = self.find(loc.elements_legs_loc)
        form_checks = elements.find_elements(*loc.form_checks_loc)
        assert len(form_checks) == 3
