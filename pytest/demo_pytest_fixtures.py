import pytest
import selenium
from selenium import webdriver

driver = None
@pytest.fixture
def setup():
    print("start browser")
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield
    driver.quit()
    print("close browser")

def test1(setup):
    driver.get("http://www.google.com")
    print("test 1 executed")

def test2(setup):
    driver.get("http://www.gmail.com")
    print("test 2 executed")

def test3(setup):
    driver.get("http://www.facebook.com")
    print("test 3 executed")

