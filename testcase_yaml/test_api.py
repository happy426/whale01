import pytest
from testcase_yaml.yaml_util import read_yaml
import requests


class TestApi:

    session = requests.Session()

    @pytest.mark.parametrize('args', read_yaml('testcase_yaml/shizhan.yaml'))
    def test_access_token(self, args):
        # print(args)
        method = args['request']['method']
        url = args['request']['url']
        data = args['request']['data']
        res = TestApi.session.request(method=method, url=url, params=data)
        result = res.json()
        assert 'access_token' in result

    @pytest.mark.parametrize('args', read_yaml('testcase_yaml/creat_flag.yaml'))
    def test_create_flag(self, args):
        method = args['request']['method']
        url = args['request']['url'] + TestApi.access_token
        data = args['request']['data']
        res = TestApi.session.request(method=method, url=url, params=data)
        print(res.json())

