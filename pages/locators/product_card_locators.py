from selenium.webdriver.common.by import By

btn_add_to_cart_loc = (By.ID, "add_to_cart")
toast_text_loc = (By.CLASS_NAME, "toast-header")
link_loc = (By.LINK_TEXT, "Terms and Conditions")
btn_increase_loc = (By.XPATH, '//*[@title="Add one"]')
quantity_form_loc = (By.XPATH, '//*[@name="add_qty"]')
cart_icon_counter_loc = (By.CSS_SELECTOR, '.my_cart_quantity.badge')
