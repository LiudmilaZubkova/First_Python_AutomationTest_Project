from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (chrome or firefox)"
    )


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    #browser = request.config.getoption("--browser")
    browser = request.param
    print(f"Creating {browser} driver")
    if browser == "chrome":
        my_driver = webdriver.Chrome()
    elif browser == "firefox":
        my_driver = webdriver.Firefox()
    else:
        raise TypeError(f"Expected 'chrome or firefox, but got {browser}")
    yield my_driver
    print(f"Closing {browser} diver")
    my_driver.quit()
