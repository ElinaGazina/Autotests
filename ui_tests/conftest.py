from selenium import webdriver
import pytest
import logging
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from ui_tests.pages.youtube_page import YoutubePage


def pytest_addoption(parser):
    parser.addoption('--mode',
                     help='Choise where exec tests',
                     choices=['local', 'remote'],
                     default='local')


def custom_driver(mode_browser):
    logging.debug('custom driver config start')
    if mode_browser == 'local':
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    elif mode_browser == 'remote':
        pass
    else:
        raise ValueError('mode_browser does not set')
    driver.maximize_window()
    logging.debug('custom driver config finish')
    return driver


@pytest.fixture(scope='session')
def mode_browser(request):
    return request.config.getoption('--mode')


@pytest.fixture(scope='function')
def browser_function(mode_browser):
    driver = custom_driver(mode_browser)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def youtube_page():
    return YoutubePage
