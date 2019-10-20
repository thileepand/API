from selenium import webdriver
import time
import pytest

@pytest.fixture(scope="module")
def setpath():
    global driver
    driver = webdriver.Chrome()
    baseURL = 'https://httpbin.org/get'
    driver.get(baseURL)
    yield
    driver.close()

def test_Validate_Registration(setpath):
    driver.maximize_window()


def test_Invalid_Registration(setpath):
    driver.maximize_window()


def test_Invalid(setpath):
    driver.maximize_window()





