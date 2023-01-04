import time

import allure
import pytest
from playwright.sync_api import Browser


class TestAlivia:

    def test_02(self, browser: Browser):
        context = browser.new_context(storage_state="../data/state.json")
        page = context.new_page()
        page.goto('https://blankme.stage.meetwhale.com/assets-new/content/share')
        print(page.url)


if __name__ == '__main__':
    pytest.main(['-vs', './testcase_pr/test_alivia_login02.py'])
