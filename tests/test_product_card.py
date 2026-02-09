def test_add_to_cart(product_card_page):
    product_card_page.open_page()
    product_card_page.check_click_add_to_cart()
    product_card_page.check_toast_after_adding()

def test_link_terms(product_card_page):
    product_card_page.open_page()
    product_card_page.check_link_href()

def test_increase_count_products(product_card_page):
    product_card_page.open_page()
    product_card_page.check_increase_count()
