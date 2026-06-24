import pytest
from selenium import webdriver
import string
import random

@pytest.fixture
def driver():
    d = webdriver.Chrome()
    d.get('https://qa-desk.education-services.ru/')
    yield d
    d.quit()

@pytest.fixture
def email():
    first_part = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    email = f'{first_part}+{random.randint(0,1000)}@gmail.com'
    return email

@pytest.fixture
def incorrect_email():
    first_part = ''.join(random.choice(string.ascii_letters) for i in range(10))
    incorrect_email_mask = random.choice(['@gmailcom', 'gmail.com', 'gmailcom'])
    incorrect_email = f'{first_part}{incorrect_email_mask}'
    return incorrect_email

@pytest.fixture
def item_name():
    item_part = ''.join(random.choice(string.ascii_lowercase) for i in range (5))
    item = f"Test item: {item_part}{random.randint(0, 1000)}"
    return item

@pytest.fixture
def item_price():
    return random.randint(10, 99999)
