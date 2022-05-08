#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pytest_test 
@File    ：test_case04.py.py
@IDE     ：PyCharm 
@Author  ：chenshuhua
@Date    ：2022/5/6 13:02 
'''
from common.common_util import CommonUtil


class Test_04(CommonUtil):
    def test_case04(self,paramss_list,module2_conftest):
        print("test_case04 here")
        print(paramss_list,module2_conftest)

    def test_case04_1(self,paramss_list,module2_conftest):
        print("one more")
        print(paramss_list)

    def test_case04_2(self,paramss_list):  # 全局paramss_list 其中已经引用len=2的list作为输入参数，则用例会执行两次
        print("nonononon"+str(paramss_list))  # 只能引用全局fixture打印出来看一下