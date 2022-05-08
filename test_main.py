# -*- coding:utf-8 -*-
from time import sleep

import pytest
import os
import sys

if __name__ == '__main__':
    pytest.main(['-sv','./testcase'])
    sleep(3)
    os.system("allure generate ./temp -o ./report/allure_reports --clean ")


# # 系统变量
#     env_dist = os.environ
#     print(env_dist.get('PATH'))
