import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import ChromeOptions


@pytest.fixture(scope='function')
def driver():
    drivers = {}

    # firefox_opts = FirefoxOptions()
    # firefox_opts.add_argument("--headless")
    # drivers['firefox'] = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    chrome_options = ChromeOptions()
    # chrome_options.add_argument('--headless')

    drivers['chrome'] = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    yield drivers

    for driver in drivers.values():
        driver.close()


def pytest_addoption(parser):
    parser.addoption('--browsers', action='store', default='chrome', help='list of browser to run tests')


def pytest_generate_tests(metafunc):
    if "browsers" in metafunc.fixturenames:
        metafunc.parametrize("browsers", metafunc.config.getoption("--browsers").split())

