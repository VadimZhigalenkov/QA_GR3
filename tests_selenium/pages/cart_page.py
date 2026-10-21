from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:

    def __init__(self, driver):
        self.driver = driver

    # локаторы
    cart_checkout_button = '//button[@id="checkout"]'
    remove_button = '//button[@data-test="remove-sauce-labs-backpack"]'
    cart_item = '//div[@class="cart_item"]'

    # гетеры
    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_checkout_button)))
    def get_remove_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.remove_button)))
    def price_in_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.remove_button)))


    #действия
    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("click checkout button")
    def click_remove_button(self):
        self.get_remove_button().click()
        print("click remove button")

    # методы
    def product_confirmation(self):
        self.click_checkout_button()
    def remove_product(self):
        self.click_remove_button()

    def get_cart_items_count(self):
        items = self.driver.find_elements(By.XPATH, self.cart_item)
        return len(items)