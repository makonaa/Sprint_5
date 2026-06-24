from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators import LoginLocators, ProfileLocators, MainPageLocators, ListingLocators
from testdata import TestData
from help_functions import HelpFunctions


class TestCreateListing:
    def test_create_listing_unauthorized_login_popup_shown(self, driver):
        driver.find_element(*MainPageLocators.CREATE_LISTING).click()
        WebDriverWait(driver, 2).until(ec.visibility_of_element_located(LoginLocators.AUTH_TO_ADD_LISTING_POPUP))

        assert driver.find_element(*LoginLocators.AUTH_TO_ADD_LISTING_POPUP).is_displayed()

    def test_create_listing_success(self, driver, email, item_name, item_price):
        HelpFunctions.full_sign_up_flow(driver = driver, email = email, password = TestData.password)
        WebDriverWait(driver, 2).until(ec.visibility_of_element_located(ProfileLocators.PROFILE_PHOTO))
        driver.find_element(*MainPageLocators.CREATE_LISTING).click()
        WebDriverWait(driver, 2).until(ec.visibility_of_element_located(ListingLocators.LISTING_TITLE))
        driver.find_element(*ListingLocators.LISTING_NAME).send_keys(item_name)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.find_element(*ListingLocators.LISTING_TYPE_DROPDOWN).click()
        WebDriverWait(driver, 2).until(ec.visibility_of_element_located(ListingLocators.LISTING_TYPE_VALUE))
        driver.find_element(*ListingLocators.LISTING_TYPE_VALUE).click()
        driver.find_element(*ListingLocators.LISTING_USED_CONDITION).click()
        driver.find_element(*ListingLocators.LISTING_CITY_DROPDOWN).click()
        WebDriverWait(driver, 2).until(ec.visibility_of_element_located(ListingLocators.LISTING_CITY_VALUE))
        driver.find_element(*ListingLocators.LISTING_CITY_VALUE).click()
        driver.find_element(*ListingLocators.LISTING_DESCRIPTION).send_keys('some description')
        driver.find_element(*ListingLocators.LISTING_PRICE).send_keys(item_price)
        driver.find_element(*ListingLocators.PUBLISH_LISTING).click()
        driver.find_element(*ProfileLocators.PROFILE_PHOTO).click()
        WebDriverWait(driver, 2).until(ec.visibility_of_element_located(ProfileLocators.MY_LISTING_CARD))
        assert driver.find_element(*ProfileLocators.MY_LISTING_CARD).is_displayed()
