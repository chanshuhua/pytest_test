#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pytest_test 
@File    ：test_case03.py.py
@IDE     ：PyCharm 
@Author  ：chenshuhua
@Date    ：2022/5/5 14:46 
'''
from common.common_util import CommonUtil


class Test_03(CommonUtil):
    def test_case03(self,paramss_list):
        print("testcase2_case03 here")

class Test_03_1():
    def test_case03_conftest(self,paramss_list):
        print("case03"+str(paramss_list))