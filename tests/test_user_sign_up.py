from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators import SignUpLocators, ProfileLocators, MainPageLocators
from testdata import TestData
from help_functions import HelpFunctions

class TestUserSignUp:
    def test_new_user_sign_up_successful(self, driver):
        email = HelpFunctions.get_email()
        HelpFunctions.full_sign_up_flow(driver = driver, email = email, password = TestData.password)
        WebDriverWait(driver, 2).until(ec.visibility_of_element_located(ProfileLocators.PROFILE_PHOTO))

        assert (driver.find_element(*ProfileLocators.PROFILE_PHOTO).is_displayed() and
                driver.find_element(*ProfileLocators.PROFILE_NAME).is_displayed())

    def test_incorrect_email_error_shown(self, driver):
        incorrect_email = HelpFunctions.get_incorrect_email()
        HelpFunctions.full_sign_up_flow(driver = driver, email = incorrect_email, password = TestData.password)
        WebDriverWait(driver, 2).until(ec.visibility_of_element_located(SignUpLocators.SIGNUP_ERROR))
        email_color = driver.find_element(*SignUpLocators.INCORRECT_EMAIL).value_of_css_property('border')
        enter_password_color = driver.find_element(*SignUpLocators.INCORRECT_ENTER_PASSWORD).value_of_css_property('border')
        re_enter_password_color = driver.find_element(*SignUpLocators.INCORRECT_RE_ENTER_PASSWORD).value_of_css_property('border')
        assert (driver.find_element(*SignUpLocators.SIGNUP_ERROR).is_displayed() and
                email_color == TestData.error_color and
                enter_password_color == TestData.error_color and
                re_enter_password_color == TestData.error_color)

    def test_signup_of_existing_user_error_shown(self, driver):
        email = HelpFunctions.get_email()
        HelpFunctions.full_sign_up_flow(driver = driver, email = email, password = TestData.password)
        HelpFunctions.exit_flow(driver)
        WebDriverWait(driver, 2).until(ec.element_to_be_clickable(MainPageLocators.LOGIN_AND_SIGN_UP_BUTTON))
        HelpFunctions.full_sign_up_flow(driver = driver, email = email, password = TestData.password)
        WebDriverWait(driver, 2).until(ec.visibility_of_element_located(SignUpLocators.SIGNUP_ERROR))
        email_color = driver.find_element(*SignUpLocators.INCORRECT_EMAIL).value_of_css_property('border')
        enter_password_color = driver.find_element(*SignUpLocators.INCORRECT_ENTER_PASSWORD).value_of_css_property(
            'border')
        re_enter_password_color = driver.find_element(
            *SignUpLocators.INCORRECT_RE_ENTER_PASSWORD).value_of_css_property('border')
        assert (driver.find_element(*SignUpLocators.SIGNUP_ERROR).is_displayed() and
                email_color == TestData.error_color and
                enter_password_color == TestData.error_color and
                re_enter_password_color == TestData.error_color)
