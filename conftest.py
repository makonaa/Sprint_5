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

