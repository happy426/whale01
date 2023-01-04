# playwright学习
## 安装
安装Playwright依赖库（Playwright支持Async\Await语法，故需要Python3.7+）
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple playwright

version 1.23.1

安装Chromium、Firefox、WebKit等浏览器的驱动文件（内置浏览器）
python -m playwright install

与Pytest结合
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pytest-playwright

## Playwright Inspector
Playwright Inspector是一个 GUI 工具，可帮助创作和调试 Playwright 脚本。这是我们默认推荐的脚本故障排除工具。

## 测试生成器
### 生成
playwright codegen 网址

playwright codegen wikipedia.org

### 模拟

[//]: # (Emulate iPhone 11.)
playwright codegen --device="iPhone 11" wikipedia.org

## 常用方法

1. 进入网页  page.goto("https://whale-login.stage.meetwhale.com/login")
2. 定位  page.locator('#name')
3. 输入  page.fill("[placeholder=\"请输入密码\"]", "Huang666")
4. 点击  page.locator('button#submit').click()
5. 悬停  page.locator('#item').hover()
6. 截图  page.screenshot(path="screenshot.png")
7. 上传文件  page.locator('').set_input_files(r"/Users/edy/Desktop/头像02.jpeg")
8. 下载
```python
with page.expect_download() as download_info:
        page.click('//*[@href="//域名/template/导入知识目录.xlsx"]')
    download = download_info.value
    download.save_as('E:\playwrightPyinstaller\导入知识目录.xlsx')
```
