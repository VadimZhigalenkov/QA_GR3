import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage


def test_unsuccessful_authorization(driver_fix):
    driver = driver_fix
    lp = LoginPage(driver)
    lp.wrong_authorization()

    """проверка сообщения об ошибке"""
    actual_text_error = lp.error_message()
    assert 'Username and password do not match any user in this service' in actual_text_error, \
        "не появилось сообщение об ошибке авторизации"
    print("Username and password do not match any user in this service")