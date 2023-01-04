import pytest
from testcase_yaml.yaml_util import read_yaml
import requests
import json


class TestApi:

    @pytest.mark.parametrize('args', read_yaml('testcase_yaml/qa.yaml'))
    def test_qa(self, args):
        method = args['method']
        url = args['url']
        company_id = args['company_id']
        comment = args['comment']
        topk = args['topk']
        data = {
            "company_id": company_id,
            "comment": comment,
            "topk": topk
        }
        res = requests.request(method=method, url=url, json=data)
        result = res.json()
        print(result)


if __name__ == '__main__':
    pytest.main(['-vs', 'testcase_yaml/test_vap_api.py'])

