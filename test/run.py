#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/14 16:55
# @Author : 郑春兴
# @Email : zhengchunxing@aegis-data.cn
# @File : run.py
# @Project : PlaywrightProject
import os

import pytest

if __name__ == "__main__":
     #pytest.main(['-s', '-v', '-q', '--alluredir', 'allure_result'])
     os.system('pytest -sq --alluredir=../allure_result')
