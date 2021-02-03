import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def setup(browser):
    if browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def browser(request):
    return request.config.getoption('--browser')


def pytest_addoption(parser):
    parser.addoption('--browser')
