import time

import pytest
from playwright.sync_api import Browser


@pytest.fixture(scope='session', autouse=True)
def setup(browser: Browser):
    context = browser.new_context(locale="zh-CN")
    # context.add_init_script(js)
    page = context.new_page()
    page.goto("https://whale-login.stage.meetwhale.com/login")
    page.fill('//*[@id="container"]/section/div[2]/div/div[3]/div[1]/div/span/input', "18709873932")
    page.fill('//*[@id="container"]/section/div[2]/div/div[3]/div[2]/div/span/input', "Huang666")
    # Check input[type="checkbox"]
    page.locator('//*[@id="container"]/section/div[2]/div/div[3]/div[4]/label/span[1]/input').check()
    # Click button:has-text("登 录")
    page.locator('//*[@id="container"]/section/div[2]/div/div[3]/div[5]/button/span').click()
    page.wait_for_timeout(3000)
    # Save storage state into the file.
    context.storage_state(path="../data/state.json")

    # # Create a new context with the saved storage state.
    # context = browser.new_context(storage_state="../data/state.json")
