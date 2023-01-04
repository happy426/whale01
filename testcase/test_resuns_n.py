import time

import pytest


class TestPrint:

    def test_01(self):
        # time.sleep(3)
        print('1')

    def test_02(self):
        # time.sleep(3)
        print('到这一步')
        assert 1==2
        print('未输出')

    def test_03(self):
        # time.sleep(3)
        print('3')

    def test_04(self):
        # time.sleep(3)
        print('4')
