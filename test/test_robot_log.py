#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/13 16:34
# @Author : 郑春兴
# @Email : zhengchunxing@aegis-data.cn
# @File : test_robot_log.py
# @Project : PlaywrightProject
import time

import allure
import pytest

from common.handle_logging import test_log
from pages.robotlogspage import RobotLogs

@allure.feature("机器人日志页面")
class TestRobotLog():
    @allure.story("机器人日志按条件查询并验证查询结果的用例")
    @allure.description('''
        1.登录成功后校验全局配置菜单是否可见
        2.在左侧导航栏中点击“全局配置>日志记录>机器人日志”打开机器人日志管理页面，并校验指定元素是否可见
        2.输入操作用户“唐”
        3.打开操作类型下拉列表选择”登录“，点击搜索按钮
        4.在查询结果列表中校验操作类型栏文本值和操作用户栏文本值，并输出测试通过或不通过日志
        ''')
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
            robotLogsPage.user_input.fill("汤")
            #robotLogsPage.start_date_input.fill("2022-05-20 00:00:00")
            #robotLogsPage.end_date_input.fill("2022-05-21 00:00:00")
            robotLogsPage.operation_type_drop_list.click()
            #content_test = robotLogsPage.login_operation_type.inner_text()
            #assert content_test == "登录"
            robotLogsPage.login_operation_type.click()
            robotLogsPage.search_button.click()

            time.sleep(1)
            robotLogsPage.assertText("//table[@class=\"el-table__body\"]/tbody/tr/td[5]/div","登录")
            robotLogsPage.assertText("//table[@class=\"el-table__body\"]/tbody/tr/td[2]/div","汤")
            test_log.info("机器人日志查询测试通过")
        except Exception as e:
            allure.attach(page.screenshot(), "用例失败截图", allure.attachment_type.PNG)
            test_log.error('机器人日志查询测试不通过')
            test_log.debug('预期结果：按照用户+日期+机器人+操作类型能查询出相关日志记录')
            test_log.exception(e)
            pytest.fail("预期结果：按照用户+日期+机器人+操作类型能查询出相关日志记录")

