import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.client_information_page import ClientInformationPage

@allure.suite("Покупка товара")
class TestSuccessfulPurchase:
    @allure.title("Покупка товара")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("feature","Оформление заказа")
    def test_successful_purchase(self, driver_fix):

        driver = driver_fix
        login = LoginPage(driver)
        login.authorization() # авторизация

        mp = MainPage(driver)
        mp.click_select_product()
        mp.click_to_cart() # переход в корзину

        cp = CartPage(driver)
        cp.product_confirmation() # оформление

        ci = ClientInformationPage(driver)
        ci.input_information() # внесение данных

        """проверка финального текста"""
        actual_text = ci.get_success_text()
        assert 'Thank you for your order' in actual_text, "Нет сообщения об успешном заказе"
        print("Thank you for your order!")