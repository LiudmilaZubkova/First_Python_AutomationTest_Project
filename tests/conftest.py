from selenium import webdriver
import pytest


@pytest.fixture()
def driver():
    print("Creating chrome driver")
    my_driver = webdriver.Chrome()
    yield my_driver
    print("Closing chrome diver")
    my_driver.quit()
