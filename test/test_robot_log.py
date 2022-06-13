#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/13 16:34
# @Author : 郑春兴
# @Email : zhengchunxing@aegis-data.cn
# @File : test_robot_log.py
# @Project : PlaywrightProject
from pages.robotlogspage import RobotLogs


def test_robot_log(page,login_hospital):
    userManagementPage = login_hospital
    # 打开全局配置菜单
    userManagementPage.global_configuration.click()
    # 打开日志记录下拉菜单
    userManagementPage.logging_menu.click()
    # 点击后台日志菜单
    userManagementPage.robot_log_menu.click()
    # 实例化后台日志页
    robotLogsPage = RobotLogs(page)
