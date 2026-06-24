from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators import ProfileLocators, MainPageLocators
from testdata import TestData
from help_functions import HelpFunctions

class TestUserLogin:
    def test_user_login(self, driver, email):
        HelpFunctions.full_sign_up_flow(driver = driver, email = email, password = TestData.password)
        HelpFunctions.exit_flow(driver)
        WebDriverWait(driver, 2).until(ec.element_to_be_clickable(MainPageLocators.LOGIN_AND_SIGN_UP_BUTTON))
        HelpFunctions.login_flow(driver = driver, email = email, password = TestData.password)
        WebDriverWait(driver, 2).until(ec.visibility_of_element_located(ProfileLocators.PROFILE_PHOTO))

        assert (driver.find_element(*ProfileLocators.PROFILE_PHOTO).is_displayed() and
                driver.find_element(*ProfileLocators.PROFILE_NAME).is_displayed())

class TestUserLogout:
    def test_user_logout(self, driver, email):
        HelpFunctions.full_sign_up_flow(driver = driver, email = email, password = TestData.password)
        HelpFunctions.exit_flow(driver)
        WebDriverWait(driver, 2).until(ec.element_to_be_clickable(MainPageLocators.LOGIN_AND_SIGN_UP_BUTTON))

        assert driver.find_element(*MainPageLocators.LOGIN_AND_SIGN_UP_BUTTON).is_displayed()
