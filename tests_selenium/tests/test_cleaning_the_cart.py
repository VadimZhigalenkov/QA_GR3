import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.main_page import MainPage

def test_cleaning_the_cart(driver_fix):

    driver = driver_fix
    lp = LoginPage(driver)
    lp.authorization() # авторизация

    mp = MainPage(driver)
    mp.click_select_product()
    mp.click_to_cart() # переход в корзину

    cp = CartPage(driver)
    cp.remove_product()

    """проверка, что товаров стало 0"""
    count_items = cp.get_cart_items_count()
    assert count_items == 0
    print("в корзине нет товаров")