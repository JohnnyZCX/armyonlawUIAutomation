#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/13 16:34
# @Author : 郑春兴
# @Email : zhengchunxing@aegis-data.cn
# @File : test_robot_log.py
# @Project : PlaywrightProject
import time

import allure

from common.handle_logging import test_log
from pages.robotlogspage import RobotLogs

@allure.feature("机器人日志页面")
class TestRobotLog():
    def test_robot_log(self,page,login_hospital):
        userManagementPage = login_hospital
        # 打开全局配置菜单
        userManagementPage.global_configuration.click()
        # 打开日志记录下拉菜单
        userManagementPage.logging_menu.click()
        # 点击后台日志菜单
        userManagementPage.robot_log_menu.click()
        # 实例化后台日志页
        robotLogsPage = RobotLogs(page)
        robotLogsPage.date_icon.wait_for()
        try:
            robotLogsPage.user_input.fill("唐")
            #robotLogsPage.start_date_input.fill("2022-05-20 00:00:00")
            #robotLogsPage.end_date_input.fill("2022-05-21 00:00:00")
            robotLogsPage.operation_type_drop_list.click()
            robotLogsPage.login_operation_type.click()
            robotLogsPage.search_button.click()
            test_log.info("机器人日志查询测试通过")
        except Exception as e:
            test_log.error('机器人日志查询测试不通过')
            test_log.debug('预期结果：按照用户+日期+机器人+操作类型能查询出相关日志记录')
            test_log.exception(e)

