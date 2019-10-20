from selenium import webdriver
import time
import pytest

@pytest.mark.groupA
def test_Validate_Registration():
    baseURL = 'https://httpbin.org/get'
    driver  = webdriver.Chrome()
    driver.get(baseURL)
    driver.maximize_window()
    time.sleep(3)
    driver.quit()

@pytest.mark.groupB
def test_Invalid_Registration():
    baseURL = 'https://httpbin.org/get'
    driver = webdriver.Chrome()
    driver.get(baseURL)
    driver.maximize_window()
    time.sleep(3)
    driver.quit()

@pytest.mark.groupA
def test_Invalid():
    baseURL = 'https://httpbin.org/get'
    driver = webdriver.Chrome()
    driver.get(baseURL)
    driver.maximize_window()
    time.sleep(3)
    driver.quit()
