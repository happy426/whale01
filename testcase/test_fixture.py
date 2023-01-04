import time

import pytest


"""
yield：分割前后置，也可以传参：yield request.param
scope(范围):``"function"`` (default), ``"class"``, ``"module"``, ``"package"`` or ``"session"``.
autouse(自动使用)：默认True，自动使用
param(参数化):params=['张三', '王二', '麻子']，这里params是参数名，有s，request.param是没有's'的
ids：当使用了params参数化时，给每一个值设置一个变量名，意义不大
names：给表示的是被@pytest.fixture标记的方法取一个别名。
"""


@pytest.fixture(scope='function', autouse=False)
def my_fixture():  # 名字可自定义 无参数
    print('\n这是前后置的方法，可以实现部分以及全部用例的前后置')
    yield
    print('\n这是后置的方法')


@pytest.fixture(scope='function', autouse=False, params=['张三', '王二', '麻子'])
def my_fixture2(request):  # 名字可自定义 有参数
    return request.param


@pytest.fixture(scope='function', autouse=False, params=['张三', '王二', '麻子'], ids=['zs', 'we', 'mz'])
def my_fixture3(request):  # 名字可自定义 有参数
    print('\n这是前后置的方法，可以实现部分以及全部用例的前后置')
    yield request.param  # 用yield返回参数
    print('\n这是后置的方法')


@pytest.fixture(scope='function', autouse=False, params=['张三', '王二', '麻子'], ids=['zs', 'we', 'mz'], name='a')
def my_fixture4(request):  # 名字可自定义 有参数
    print('\n这是前后置的方法，可以实现部分以及全部用例的前后置')
    yield request.param  # 用yield返回参数
    print('\n这是后置的方法')


@pytest.fixture(scope='class', autouse=True)
def login():
    print('这是登录')
    yield
    print("这是退出")


class TestPrint01:

    def test_11(self):
        # time.sleep(3)
        print('11')

    @pytest.mark.smoke
    def test_12(self):
        # time.sleep(3)
        print('12')

    def test_13(self):
        # time.sleep(3)
        print('13')


# class TestPrint02:
#
#     def test_21(self, my_fixture2):
#         # time.sleep(3)
#         print('21'+str(my_fixture2))
#
#     @pytest.mark.smoke
#     def test_22(self, my_fixture3):
#         # time.sleep(3)
#         print('22'+str(my_fixture3))
#
#     def test_23(self, a):
#         # time.sleep(3)
#         print('23'+str(a))


if __name__ == '__main__':
    pytest.main(['-vs', './testcase/test_fixture.py'])
