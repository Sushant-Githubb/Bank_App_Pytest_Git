import pytest as pytest
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()

    else:
        driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://apps.credence.in/")
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(params=[
    ("Demo567", "pass"),
    ("Tushar", "pass"),
    ("Admin420", "pass"),
    ("demo2", "pass"),
    ("demo5", "fail")

])
def getDataForSearchUser(request):
    return request.param
