import pytest


@pytest.fixture(scope='function', autouse=False)
def product_fixture():  # 名字可自定义 无参数
    print('\n这是product前置')
    yield
    print('\n这是product后置')
