#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pytest_test 
@File    ：CommonUtil.py
@IDE     ：PyCharm 
@Author  ：chenshuhua
@Date    ：2022/5/5 15:27 
'''

class CommonUtil:
    def setup(self):
        print("setup start")
    # 每个测试用例之前执行一次
    def teardown(self):
        print("teardown end")
    # 每个测试用例之后执行一次

    def setup_class(self):
        print("setup_class start!!")
    # 每个类之前执行一次
    def teardown_class(self):
        print("teardown_class end!!")
    # 每个类之后执行一次



