

from config import URL_YOUTUBE
from ui_tests.locators.youtube_page_locators import LocatorsForYoutube



class YoutubePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def enter_text_input_search(self, text):
        self.driver.find_element(LocatorsForYoutube.input_search).send_keys(text)