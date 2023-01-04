import time

import pytest


class TestPrint:

    def test_huang(self, pr):
        time.sleep(4)
        print('黄')

    @pytest.mark.skip(reason='无理由')
    def test_zhuang(self, pr):
        time.sleep(5)
        print('庄')

    @pytest.mark.run(order=1)
    @pytest.mark.smoke
    def test_maoyan(self, pr):
        time.sleep(3)
        print('this is smoke_case')

    def test_manage(self, pr):
        time.sleep(6)
        print('this id usermanage')
