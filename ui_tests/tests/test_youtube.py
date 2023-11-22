import pytest
from config import URL_YOUTUBE


class TestYoutube:
    def test_find_video(self, browser_function, youtube_page):
        youtube_page.open()
        youtube_page.enter_text_input_search('Подготовка к собеседованию QA Automation: темы и вопросы')
