from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class MainPage:

    def __init__(self, driver):
        self.driver = driver

    #локаторы

    select_product_1 = '//button[@data-test="add-to-cart-sauce-labs-backpack"]' #Sauce Labs Backpack
    cart = '//div[@id="shopping_cart_container"]'


    # гетеры
    def select_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))
    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    # действия

    def click_select_product(self): # обавляем в корзину
        self.select_product().click()
        print("сlick product 1")
    def click_to_cart(self): # кликаем на корзину
        self.get_cart().click()
        print("сlick to cart")

