from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_AND_SIGN_UP_BUTTON = (By.CSS_SELECTOR, '.buttonSecondary[type="button"]')
    CREATE_LISTING = (By.XPATH, '//button[text()="Разместить объявление"]')

class LoginLocators:
    ENTER_EMAIL = (By.XPATH, '//h1[text()="Войти"]/../..//input[@name="email"]')
    ENTER_PASSWORD = (By.CSS_SELECTOR, '.input_inputStandart__JweLZ[name="password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')
    AUTH_TO_ADD_LISTING_POPUP = (By.XPATH, '//h1[text()="Чтобы разместить объявление, авторизуйтесь"]')

class SignUpLocators:
    NO_ACC_BUTTON = (By.XPATH, '//button[text()="Нет аккаунта"]') #need to stay here
    ENTER_EMAIL = (By.XPATH, '//h1[text()="Зарегистрироваться"]/../..//input[@name="email"]') #need to stay here
    ENTER_PASSWORD = (By.CSS_SELECTOR, '.input_inputStandart__JweLZ[name="password"]')
    RE_ENTER_PASSWORD = (By.CSS_SELECTOR, '.input_inputStandart__JweLZ[name="submitPassword"]')
    CREATE_ACC = (By.XPATH, '//button[text()="Создать аккаунт"]')
    SIGNUP_ERROR = (By.XPATH, '//span[text()="Ошибка"]')
    INCORRECT_EMAIL = (By.XPATH, '//input[@placeholder = "Введите Email"]/..')
    INCORRECT_ENTER_PASSWORD = (By.XPATH, '//input[@placeholder = "Пароль"]/..')
    INCORRECT_RE_ENTER_PASSWORD = (By.XPATH, '//input[@placeholder = "Повторите пароль"]/..')

class ProfileLocators:
    PROFILE_PHOTO = (By.CSS_SELECTOR, '.circleSmall')
    PROFILE_NAME = (By.CSS_SELECTOR, '.profileText.name')
    EXIT_PROFILE = (By.XPATH, '//button[text()="Выйти"]')
    MY_LISTINGS_TITLE = (By.XPATH, '//h1[text()="Мои объявления"]')
    MY_LISTING_CARD = (By.CSS_SELECTOR, '.card')

class ListingLocators:
    LISTING_TITLE = (By.CSS_SELECTOR, '.createListing_title__IFtFs')
    LISTING_NAME = (By.CSS_SELECTOR, '.input_inputStandart__JweLZ[name="name"]')
    LISTING_TYPE_DROPDOWN = (By.XPATH, '//input[@name="category"]/..//button')
    LISTING_TYPE_VALUE = (By.XPATH, '//span[text()="Технологии"]')
    LISTING_USED_CONDITION = (By.XPATH, '//label[text()="Б/У"]/../div')
    LISTING_CITY_DROPDOWN = (By.XPATH, '//input[@name="city"]/../button')
    LISTING_CITY_VALUE = (By.XPATH, '//span[text()="Санкт-Петербург"]')
    LISTING_DESCRIPTION = (By.CSS_SELECTOR, '.textarea_inputStandart__IoNxq')
    LISTING_PRICE = (By.CSS_SELECTOR, '.input_inputStandart__JweLZ[name="price"]')
    PUBLISH_LISTING = (By.CSS_SELECTOR, '.buttonPrimary[type="submit"]')
