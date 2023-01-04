import requests

"""
requests.get()
url是接口地址，params是参数

requests.post()
url是接口地址，data用于传参，json也适用于传参

requests.put()
requests.delete()

requests.request()
可以发送上面所有的方法。
"""


class TestRequest:

    # get请求：获取接口统一鉴权码token接口
    def test_get_token(self):
        url = 'https://www.runoob.com/try/ajax/json_demo.json'
        rel = requests.get(url)
        print(rel.json())

    def test_post_token(self):
        url = 'https://www.runoob.com/try/ajax/demo_post2.php'
        myobj = {'fname': 'RUNOOB', 'lname': 'Boy'}
        rel = requests.post(url, data=myobj)
        print(rel.text)


if __name__ == '__main__':
    # TestRequest.test_get_token()
    TestRequest.test_post_token()
