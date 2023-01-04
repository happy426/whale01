from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.webkit.launch()
    page = browser.new_page()
    page.goto("https://www.baidu.com/")
    page.screenshot(path="result/example.png")
    browser.close()
