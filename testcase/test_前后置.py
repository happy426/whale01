import time

import pytest


class TestPrint:

    # 在所有用例之前只执行一次
    def setup_class(self):
        print('\n在每个类执行后的扫尾工作：比如：创建日志对象，创建数据库的连接，创建接口的请求对象')

    # 在每个用例之前执行一次
    def setup(self):
        print('\n执行用例之前初始化代码:打开浏览器，加载网页')

    def test_01(self):
        # time.sleep(3)
        print('1')

    @pytest.mark.smoke
    def test_02(self):
        # time.sleep(3)
        print('2')

    def test_03(self):
        # time.sleep(3)
        print('3')

    def teardown(self):
        # time.sleep(3)
        print('\n执行用例之后的扫尾工作：关闭浏览器')

    def teardown_class(self):
        print('在每个类执行后的扫尾工作：比如：销毁日志对象，销毁数据库的连接，销毁接口的请求对象')
