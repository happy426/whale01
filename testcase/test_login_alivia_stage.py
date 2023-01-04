import os
import time

import allure
import pytest
from playwright.sync_api import Browser


@allure.feature("直播复盘模块")
class TestAliviaBlankMe:

    @allure.title("直播复盘列表页")
    @allure.severity("critical")
    def test_blankme_zhibo_login01(self, browser: Browser):
        context = browser.new_context(storage_state="cookie_hyx.json")
        page = context.new_page()
        page.goto("https://blankme.stage.meetwhale.com/vap/entry")
        page.wait_for_timeout(3000)
        assert "https://blankme.stage.meetwhale.com/vap/entry" == page.url
        allure.attach(page.screenshot(), '登录成功', allure.attachment_type.PNG)
        print("01截图成功")
        # 断言语句失败

    @allure.title("直播复盘进入直播间")
    @allure.severity("critical")
    def test_blankme_zhibo_login02(self, browser: Browser):
        context = browser.new_context(storage_state="cookie_hyx.json")
        page = context.new_page()
        page.goto("https://blankme.stage.meetwhale.com/vap/entry")
        page.locator("text=738").click()
        page.wait_for_timeout(5000)
        assert "https://blankme.stage.meetwhale.com/vap/live-detail/73" == page.url
        allure.attach(page.screenshot(), '进入成功', allure.attachment_type.PNG)
        print("02截图成功")



