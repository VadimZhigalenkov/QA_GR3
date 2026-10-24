import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import cart_checkout_button, remove_button, cart_item

class CartPage:

    def __init__(self, driver):
        self.driver = driver


    # гетеры
    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, cart_checkout_button)))
    def get_remove_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, remove_button)))

    #действия
    @allure.step("Нажатие кнопки checkout")
    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("click checkout button")

    @allure.step("Удаление товара из корзины")
    def click_remove_button(self):
        WebDriverWait(self.driver, 30).until(EC.url_contains("cart.html"))
        self.get_remove_button().click()

    # методы
    @allure.step("Оформление заказа из корзины")
    def product_confirmation(self):
        self.click_checkout_button()

    @allure.step("Очистка корзины")
    def remove_product(self):
        self.click_remove_button()

    def get_cart_items_count(self):
        items = self.driver.find_elements(By.XPATH, cart_item)
        return len(items)