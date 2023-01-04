import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            browser = await browser_type.launch()
            page = await browser.new_page()
            await page.goto('https://xingzheai.cn/')
            await page.wait_for_selector("text=智能内容审核")
            await page.screenshot(path=f'./result/example-{browser_type.name}.png')
            await browser.close()


asyncio.get_event_loop().run_until_complete(main())
