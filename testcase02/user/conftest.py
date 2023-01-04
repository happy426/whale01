import pytest


@pytest.fixture(scope='function', autouse=False)
def user_fixture():  # 名字可自定义 无参数
    print('\n这是user前置')
    yield
    print('\n这是user后置')
