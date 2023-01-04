import pytest


@pytest.fixture(scope='function', autouse=False)
def all_fixture():  # 名字可自定义 无参数
    print('\n这是全局前置')
    yield
    print('\n这是全局后置')
