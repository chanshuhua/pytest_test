#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pytest_test 
@File    ：test_case01.py
@IDE     ：PyCharm 
@Author  ：chenshuhua
@Date    ：2022/5/4 20:16 
'''
import pytest


class Test_01():
    age = 18

    @pytest.mark.run(order=3)
    @pytest.mark.DEV_SMOKE_TEST
    def test_case01(self):
        print("test01 here")

    @pytest.mark.skipif(age>18,reason='llll')
    @pytest.mark.run(order=1)
    def test_case01_2(self):
        print("test01_2 here")

    @pytest.mark.run(order=2)
    def test_case01_3(self):
        print("test01_3 here")
        # assert 1==2

