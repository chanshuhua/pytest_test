#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pytest_test 
@File    ：test_case05.py.py
@IDE     ：PyCharm 
@Author  ：chenshuhua
@Date    ：2022/5/8 1:54 
'''
import pytest
import requests

from common.yaml_util import read_yaml


class Test_05():
    @pytest.mark.parametrize('param',["hello","hi"])
    def test_case05(self,param):
        print("do sth in test_case05 : " + str(param))

    @pytest.mark.parametrize('arg1,arg2', [['a', 1],['b', 2],['c', 3]])
    def test_case05_1(self,arg1,arg2):
        print("do  %s  and %s  in test_case05_1"% (arg1,arg2))

    @pytest.mark.parametrize('getToken',read_yaml('data/yaml/get_token.yaml'))
    def test_getToken(self,getToken):
        print(getToken)
        # print(read_yaml('data/yaml/get_token.yaml'))
        # print(getToken["name"])
        print(getToken["request"]["url"])
        req = requests.post(url=getToken["request"]["url"],data =getToken["request"]["data"] )
        print(req.content.decode())
        # assert getToken["name"] in [ "用例名称2", "用例名称1"]
