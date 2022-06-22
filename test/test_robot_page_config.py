#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/22 15:11
# @Author : 郑春兴
# @Email : zhengchunxing@aegis-data.cn
# @File : test_robot_page_config.py
# @Project : PlaywrightProject
import time

import allure
import pytest

from common.handle_logging import test_log
from pages.equipmentmanage import EquipmentManage
from pages.robotpageconfig import RobotPageConfig

@allure.feature("机器人页面配置")
class TestRobotPageConfig:
    @allure.story("机器人首页背景配置")
    @allure.description('''
                    1.使用超级管理员账号登录成功，点击机器人管理菜单打开设备管理页
                    2.输入机器人编号点击查询，查询出指定机器人
                    3.在操作列点击“页面配置”进入页面配置页
                    4.在首页背景tab下更改背景图
                    5.点击提交并同步按钮
                    6.校验提交同步成功提示语句文本
                    7.在提交同步成功提示框中点击【确定】
                    8.再点击使用默认按钮，再次点击提交并同步按钮
                    ''')
    def test_background_config_home_page(self,page,superUserAmdin_login):
        userManagementPage = superUserAmdin_login
        userManagementPage.equipment_manage_menu.click()
        equipmentManagePage = EquipmentManage(page)
        equipmentManagePage.robot_number_input.wait_for()
        equipmentManagePage.robot_number_input.fill("D4A0D010020534M1D5")
        equipmentManagePage.search_button.click()
        time.sleep(1)
        equipmentManagePage.first_row_page_config_button.click()
        try:
            time.sleep(2)
            robotPageConfig = RobotPageConfig(page)
            robotPageConfig.background_config_tab.wait_for()
            robotPageConfig.upload_background_image.set_input_files("test\\background.png")
            time.sleep(2)
            robotPageConfig.commit_sync_button.click()
            time.sleep(1)
            robotPageConfig.assertText("//div[@class=\"deleteWarning\"]","机器人配置提交同步成功")
            robotPageConfig.commit_success_confirm_button.click()
            robotPageConfig.background_config_set_default_button.click()
            robotPageConfig.commit_sync_button.click()
            time.sleep(1)
            robotPageConfig.assertText("//div[@class=\"deleteWarning\"]", "机器人配置提交同步成功")
            robotPageConfig.commit_success_confirm_button.click()
            test_log.info("机器人首页背景配置测试通过")
        except Exception as e:
            allure.attach(page.screenshot(), "用例失败截图", allure.attachment_type.PNG)
            test_log.error('机器人首页背景配置测试不通过')
            test_log.debug('预期结果：首页背景更改和使用默认背景都能正常提交并同步成功')
            test_log.exception(e)
            pytest.fail("预期结果：首页背景更改和使用默认背景都能正常提交并同步成功")




