from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from locators.locators import first_name, last_name, postal_code, continue_button, finish_button, success_header

class ClientInformationPage:

    def __init__(self, driver):
        self.driver = driver

    faker = Faker()

    fake_first_name = faker.first_name()
    fake_last_name = faker.last_name()
    fake_postal_code = faker.postcode()

    # гетеры

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, first_name)))
    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, last_name)))
    def get_postal_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, postal_code)))
    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, continue_button)))
    def get_finish_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, finish_button)))
    def get_success_header(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, success_header)))
    def get_success_text(self):
        return self.get_success_header().text


    # действия

    def input_first_name(self, first_name):
        self.get_first_name(). send_keys(first_name)
        print("input first name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("input last name")

    def input_postal_code(self, postal_code):
        self.get_postal_code().send_keys(postal_code)
        print("input postal code")

    def click_continue_button(self):
        self.get_continue_button().click()
        print("сlick continue")

    def click_finish_button(self):
        self.get_finish_button().click()
        print("click finish button")


    # методы

    def input_information(self):
        self.input_first_name(self.fake_first_name)
        self.input_last_name(self.fake_last_name)
        self.input_postal_code(self.fake_postal_code)
        self.click_continue_button()
        self.click_finish_button()

