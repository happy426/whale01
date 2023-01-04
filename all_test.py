import os

import pytest

if __name__ == '__main__':
    # os.system('rm -rf temp')
    # os.system('rm -rf report')
    # # pytest.main()
    # pytest.main(['-vs', './testcase/test_login_alivia_stage.py'])
    # os.system('allure generate ./temp -o ./report --clean')

    # pytest.main(['./testcase/test_parametrize.py'])
    # pytest.main(['./testcase_yaml/test_api.py'])  # yaml实战
    pytest.main(['-vs', 'testcase/test_01.py'])
