import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        # browser = await p.chromium.launch()
        """
        Playwright 以无头模式运行浏览器。要查看浏览器 UI，请在启动浏览器时传递headless=False标志。您还可以使用slow_mo来减慢执行速度
        """
        browser = await p.chromium.launch(headless=False, slow_mo=50)
        page = await browser.new_page()
        await page.goto("https://www.baidu.com/")
        print(await page.title())
        await browser.close()

asyncio.run(main())
