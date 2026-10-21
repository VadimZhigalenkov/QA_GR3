from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import select_product_1, cart



class MainPage:

    def __init__(self, driver):
        self.driver = driver


    # гетеры
    def select_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, select_product_1)))
    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, cart)))

    # действия

    def click_select_product(self): # обавляем в корзину
        self.select_product().click()
        print("сlick product 1")
    def click_to_cart(self): # кликаем на корзину
        self.get_cart().click()
        print("сlick to cart")

