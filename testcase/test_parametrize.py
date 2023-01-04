import pytest


class TestRegister:

    @pytest.mark.parametrize('caseinfo', ['张三', '李四', '王二'])
    def test_add_list(self, caseinfo):
        print(type(caseinfo))
        print("用户注册：" + caseinfo)

    @pytest.mark.parametrize('caseinfo02', [{'username': "张三", 'password': "123456"},
                                            {'username': "李四", 'password': "huang666"}])
    def test_add_dictInList(self, caseinfo02):
        print(type(caseinfo02))
        print("用户注册：" + str(caseinfo02))  # 需要强制转换类型

    @pytest.mark.parametrize('name, password', [['张三', 'zhangsan123'], ['李四', 'lisi123']])
    def test_add_manyParam(self, name, password):
        print(type(name))
        print("用户注册：" + str(name) + ' ' + str(password))


if __name__ == '__main__':
    pytest.main(['testcase/test_parametrize.py'])
