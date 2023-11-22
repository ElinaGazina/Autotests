from config import URL_YOUTUBE
from ui_tests.locators.youtube_page_locators import LocatorsForYoutube
from selene import browser


class YoutubePage:
    def __init__(self):
        self.url = URL_YOUTUBE

    def open(self):
        browser.open_url(self.url)

    def enter_text_input_search(self, text):
        self.driver.find_element(LocatorsForYoutube.input_search).send_keys(text)
