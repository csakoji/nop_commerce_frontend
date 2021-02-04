import pytest
from selenium import webdriver
from utilities.custom_logging import LogGen

logger = LogGen.log_gen()


@pytest.fixture(scope='function')
def setup(browser):
    if browser == 'firefox':
        logger.info("Opening firefox browser")
        driver = webdriver.Firefox()
    else:
        logger.info("Opening chrome browser")
        driver = webdriver.Chrome()
    yield driver
    logger.info("Quitting browser")
    driver.quit()


@pytest.fixture
def browser(request):
    return request.config.getoption('--browser')


def pytest_addoption(parser):
    parser.addoption('--browser')
