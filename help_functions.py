from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators import LoginLocators, SignUpLocators, MainPageLocators, ProfileLocators
import random
import string

class HelpFunctions:

    @staticmethod
    def full_sign_up_flow(driver, email, password):
        driver.find_element(*MainPageLocators.LOGIN_AND_SIGN_UP_BUTTON).click()
        WebDriverWait(driver, 2).until(ec.element_to_be_clickable(SignUpLocators.NO_ACC_BUTTON))
        driver.find_element(*SignUpLocators.NO_ACC_BUTTON).click()
        WebDriverWait(driver, 2).until(ec.element_to_be_clickable(SignUpLocators.ENTER_EMAIL))
        driver.find_element(*SignUpLocators.ENTER_EMAIL).send_keys(email)
        driver.find_element(*SignUpLocators.ENTER_PASSWORD).send_keys(password)
        driver.find_element(*SignUpLocators.RE_ENTER_PASSWORD).send_keys(password)
        driver.find_element(*SignUpLocators.CREATE_ACC).click()

    @staticmethod
    def login_flow(driver, email, password):
        driver.find_element(*MainPageLocators.LOGIN_AND_SIGN_UP_BUTTON).click()
        WebDriverWait(driver, 2).until(ec.element_to_be_clickable(LoginLocators.ENTER_EMAIL))
        driver.find_element(*LoginLocators.ENTER_EMAIL).send_keys(email)
        driver.find_element(*LoginLocators.ENTER_PASSWORD).send_keys(password)
        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

    @staticmethod
    def exit_flow(driver):
        WebDriverWait(driver, 2).until(ec.element_to_be_clickable(ProfileLocators.EXIT_PROFILE))
        driver.find_element(*ProfileLocators.EXIT_PROFILE).click()

    @staticmethod
    def get_email():
        first_part = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        email = f'{first_part}+{random.randint(0, 1000)}@gmail.com'
        return email

    @staticmethod
    def get_incorrect_email():
        first_part = ''.join(random.choice(string.ascii_letters) for i in range(10))
        incorrect_email_mask = random.choice(['@gmailcom', 'gmail.com', 'gmailcom'])
        incorrect_email = f'{first_part}{incorrect_email_mask}'
        return incorrect_email

    @staticmethod
    def get_item_name():
        item_part = ''.join(random.choice(string.ascii_lowercase) for i in range (5))
        item = f"Test item: {item_part}{random.randint(0, 1000)}"
        return item

    @staticmethod
    def get_item_price():
        return random.randint(10, 99999)