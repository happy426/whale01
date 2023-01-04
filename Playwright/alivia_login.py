from playwright.sync_api import Playwright, sync_playwright, expect
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://whale-login.stage.meetwhale.com/login
    page.goto("https://whale-login.stage.meetwhale.com/login")

    # Click [placeholder="请输入手机号"]
    page.locator("[placeholder=\"请输入手机号\"]").click()

    # Fill [placeholder="请输入手机号"]
    page.locator("[placeholder=\"请输入手机号\"]").fill("18709873932")

    # Click [placeholder="请输入密码"]
    page.locator("[placeholder=\"请输入密码\"]").click()

    # Fill [placeholder="请输入密码"]
    page.locator("[placeholder=\"请输入密码\"]").fill("Huang666")

    # Check input[type="checkbox"]
    page.locator("input[type=\"checkbox\"]").check()

    # Click button:has-text("登 录")
    page.locator("button:has-text(\"登 录\")").click()
    page.wait_for_timeout(3000)

    page.goto("https://blankme.stage.meetwhale.com/profile")
    # Click text=更换头像

    # page.locator("text=更换头像").click()

    page.locator('//*[@id="root"]/div[2]/div/div[1]/div[2]/div/div/div/label/img').set_input_files(r"/Users/edy/Desktop/头像01.jpeg")
    #
    time.sleep(3)
    # # Click button:has-text("完成裁切")
    page.locator('//*[@id="container"]/div/div/div[2]/div/div[2]/div[2]/button[2]').click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
