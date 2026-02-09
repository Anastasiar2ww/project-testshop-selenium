from pages.base_page import BasePage
from pages.locators import main_locators as loc


class MainPage(BasePage):
    page_url = '/'

    def check_search_field_enable(self):
        search_field = self.find(loc.search_field_loc)
        search_field.is_enabled()

    def check_horizontal_scroll_enable(self):
        horizontal_scroll = self.find(loc.horizontal_scroll_loc)
        horizontal_scroll.is_enabled()

    def footer_text(self, expected_text):
        footer_text = self.get_text(loc.footer_text_loc)
        assert footer_text == expected_text
