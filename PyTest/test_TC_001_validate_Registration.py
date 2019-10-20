from selenium import webdriver
import time
import pytest

# a = 101
# @pytest.mark.skipif (a>100, reason="Don't want to run the current build")
def test_Validate_Registration():
    baseURL = 'https://httpbin.org/get'
    driver  = webdriver.Chrome()
    driver.get(baseURL)
    driver.maximize_window()
    time.sleep(3)
    driver.quit()


def test_Invalid_Registration():
    baseURL = 'https://httpbin.org/get'
    driver = webdriver.Chrome()
    driver.get(baseURL)
    driver.maximize_window()
    time.sleep(3)
    driver.quit()



