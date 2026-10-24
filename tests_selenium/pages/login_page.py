from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import user_name, password, login_button, error_mes
import allure

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.standard_user_name = "standard_user"
        self.standard_password = "secret_sauce"

        self.wrong_username = "wrong_user"
        self.wrong_password = "wrong_password"

    # гетеры
    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, login_button)))

    def error_message(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, error_mes))).text

    # действия
    @allure.step("Ввод логина: {username_text}")
    def input_username(self, username_text):
        self.get_user_name().send_keys(username_text)
        print("input username")
        
    @allure.step("Ввод пароля")
    def input_password(self, pwd_text):
        self.get_password().send_keys(pwd_text)
        print("input password")
        
    @allure.step("Ввод неверного логина: {wrong_username}")
    def input_wrong_username(self, wrong_username):
        self.get_user_name().send_keys(wrong_username)
        print("input wrong username")

    @allure.step("Ввод неверного пароля: {wrong_password}")
    def input_wrong_password(self, wrong_password):
        self.get_password().send_keys(wrong_password)
        print("input wrong password")

    @allure.step("Нажатие кнопки login")
    def click_login_button(self):
        self.get_login_button().click()
        print("click login button")



    # методы
    @allure.step("Авторизация стандартным пользователем")
    def authorization(self):
        self.input_username(self.standard_user_name)
        self.input_password(self.standard_password)
        self.click_login_button()

    @allure.step("Авторизация с неверными данными")
    def wrong_authorization(self):
        self.input_wrong_username(self.wrong_username)
        self.input_wrong_password(self.wrong_password)
        self.click_login_button()
