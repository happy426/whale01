from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.baidu.com/")
    # print(page.title())
    x = page.locator('//*[@id="hotsearch-content-wrapper"]/li/a/span[2]').all_text_contents()
    print(x)
    browser.close()
