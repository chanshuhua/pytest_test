#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pytest_test 
@File    ：conftest.py.py
@IDE     ：PyCharm 
@Author  ：chenshuhua
@Date    ：2022/5/6 19:17 
'''
import pytest

@pytest.fixture(scope="function",name="module2_conftest")
def func_fixture():
    print("module2 before")
    yield
    print("module2 end")