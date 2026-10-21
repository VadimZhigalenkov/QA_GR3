from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # локаторы

    user_name = '//input[@id="user-name"]'
    password = '//input[@id="password"]'
    login_button = '//input[@id="login-button"]'

    standard_user_name = "standard_user"
    standard_password = "secret_sauce"

    wrong_username = "wrong_user"
    wrong_password = "wrong_password"

    error_mes = '//h3[@data-test="error"]'

    # гетеры
    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def error_message(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.error_mes))).text

    # действия

    def input_username(self, standard_user_name):
        self.get_user_name().send_keys(standard_user_name)
        print("input username")

    def input_password(self, standard_password):
        self.get_password().send_keys(standard_password)
        print("input password")

    def input_wrong_username(self, wrong_username):
        self.get_user_name().send_keys(wrong_username)
        print("input wrong username")

    def input_wrong_password(self, wrong_password):
        self.get_password().send_keys(wrong_password)
        print("input wrong password")


    def click_login_button(self):
        self.get_login_button().click()
        print("click login button")



    # методы

    def authorization(self):
        self.input_username(self.standard_user_name)
        self.input_password(self.standard_password)
        self.click_login_button()

    def wrong_authorization(self):
        self.input_wrong_username(self.wrong_username)
        self.input_wrong_password(self.wrong_password)
        self.click_login_button()
