#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pytest_test 
@File    ：common_yaml.py
@IDE     ：PyCharm 
@Author  ：chenshuhua
@Date    ：2022/5/10 17:01 
'''
import os

import yaml


class getyamldata():
    def get_yaml_data(self, test_data_path):
        case = []  # 保存测试用例名称
        http = []  # 保存请求对象
        expected = []  # 保存预期结果
        with open(test_data_path, encoding='utf-8') as f:  #!!重点
            dat = yaml.load(f.read(), Loader=yaml.SafeLoader) # !!重点
            test = dat['tests']
            # print(dat["tests"])
            for it in test:
                case.append(it.get('case', ''))  # get返回对应value值(key,return default='')
                http.append(it.get('http', {}))
                expected.append(it.get('expected', {}))

        parameters = (case,http,expected)
        # parameters = zip(case, http, expected)
        return parameters

    def read_yaml_params_byfilename(self, yaml_file_name):
        # print(os.path.dirname(os.path.abspath(__file__)))

        # ！路径地址调用join（根目录路径 + 指定路径 + 文件名）
        datapath = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data/yaml/',
                                yaml_file_name)
        # print(datapath)
        parameters = self.get_yaml_data(datapath)
        list_params = list(parameters)
        return list_params

if __name__ == '__main__':
    # resp = getyamldata().get_yaml_data('../data/yaml/test_case.yaml')
    # print(resp)

    resp = getyamldata().read_yaml_params_byfilename('test_case.yaml')
    print(resp)