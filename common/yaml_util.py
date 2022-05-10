#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pytest_test 
@File    ：yaml_util.py
@IDE     ：PyCharm 
@Author  ：chenshuhua
@Date    ：2022/5/8 9:32 
'''
import os

import yaml

# 获取项目路径
def get_obj_path():
    # fatherpath =  os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + ".")
    # print(fatherpath)
    return os.path.dirname(__file__).split('common')[0]
### os.getcwd()
### os.path.abspath('.')
### os.path.dirname(__file__)
### split('') 根据内容分割


# 读取yaml文件
def read_yaml(yaml_path):
    with open(get_obj_path()+yaml_path,mode='r',encoding='utf-8') as f:
        value = yaml.load(stream=f,Loader=yaml.FullLoader)
        return value


if __name__ == '__main__':
    print(get_obj_path())
    print(read_yaml('data/yaml/test.yaml'))
    print(read_yaml('data/yaml/get_token.yaml'))