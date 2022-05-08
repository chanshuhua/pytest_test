#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pytest_test 
@File    ：test_case02.py
@IDE     ：PyCharm 
@Author  ：chenshuhua
@Date    ：2022/5/4 20:17 
'''
import pytest


# @pytest.fixture(scope="class",autouse=True) # 全局
# function 函数/次
# class 类/次
# session 会话/次

@pytest.fixture(scope="class") # 部分
def sql_check_before():
    print("sqllllll check before")

@pytest.fixture(scope="class",autouse=True)
def sql_check_after():
    yield "success"
    print("sqlllllll check end")


class Test_02():

    def test_case02(self):
        print("test02 here")

    def test_case02_1(self,sql_check_before,sql_check_after):  #部分引用的办法
        print("test02_1 check before?")
        print(sql_check_after)

    def test_case02_2(self):
        print("test02check class02")

@pytest.mark.usefixtures("sql_check_before")
class Test_0222():

    def test_case0222(self):
        print("what the help")