#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/14 16:55
# @Author : 郑春兴
# @Email : zhengchunxing@aegis-data.cn
# @File : run.py
# @Project : PlaywrightProject
# encoding=utf-8
import os
import pytest

if __name__ == "__main__":
    # 收集并运行测试用例，同时以json格式文件生成测试结果数据且覆盖之前的结果数据，--reruns=4代表失败重跑4次，--headed代表有头浏览器模式
    pytest.main(['--headed', '--screenshot=on', '--video=on', '-sv', '--reruns=4', '--reruns-delay=3', '--alluredir', 'allure_result', '--clean-alluredir'])
    # 下面命令开启无头模式，--screenshot=on和--video=on代表开启截图和录屏功能
    """pytest.main(
        ['--screenshot=on', '--video=on', '-sv', '--reruns=4', '--reruns-delay=2', '--alluredir', 'allure_result',
         '--clean-alluredir'])"""
    # 生成测试报告并清空历史报告的数据
    os.system(r"allure generate allure_result -c -o allure-report")
    # 打开浏览器并展示报告
    os.system(r"allure open allure-report")
