import pytest
from config import URL_YOUTUBE

class TestYoutube:
    @pytest.mark.usefixtures('browser_function')
    def test_find_video(self, youtube_page):
        youtube_page.open(URL_YOUTUBE)
        youtube_page.enter_text_input_search('Подготовка к собеседованию QA Automation: темы и вопросы')
