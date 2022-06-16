#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/16 11:46
# @Author : 郑春兴
# @Email : zhengchunxing@aegis-data.cn
# @File : test_sensitive_word.py
# @Project : PlaywrightProject
import time

import allure
import pytest

from common.handle_logging import test_log
from pages.sensitivewordpage import SensitiveWordPage


@allure.feature("敏感词预警页面")
class TestSensitiveWord():
    @allure.story("查询敏感词测试用例")
    @allure.description('''
            1.登录成功后校验全局配置菜单是否可见
            2.在左侧导航栏中点击“全局配置>敏感词预警”打开敏感词预警页面，并校验指定元素是否可见
            2.操作日期中输入2022-05-01至2022-05-30
            3.打开机器人下拉列表选择其中一个机器人ID
            4.点击【搜索】按钮
            5.在查询敏感词结果列表中判断机器人ID列的值是否正确
            ''')
    def test_query_sensitive_word(self,page,login_hospital):
        userManagementPage = login_hospital
        # 打开全局配置菜单
        userManagementPage.global_configuration.click()
        userManagementPage.sensitive_word_warning_menu.click()
        sensitiveWordPage = SensitiveWordPage(page)
        time.sleep(1)
        sensitiveWordPage.sensitive_config_button.wait_for()
        try:
            sensitiveWordPage.date_icon.click()
            sensitiveWordPage.start_date_input.fill("2022-05-01")
            sensitiveWordPage.end_data_input.fill("2022-05-30")
            sensitiveWordPage.date_panel_confirm_button.click()
            sensitiveWordPage.robot_drop_down_list.click()
            sensitiveWordPage.robot_list_second.click()
            sensitiveWordPage.search_button.click()
            time.sleep(2)
            sensitiveWordPage.assertText("//tr[@class=\"el-table__row\"]/td[5]/div","D4A0D010020534M1D5")
            test_log.info("查询敏感词测试通过")
        except Exception as e:
            allure.attach(page.screenshot(), "用例失败截图", allure.attachment_type.PNG)
            test_log.error('查询敏感词测试不通过')
            test_log.debug('预期结果：按照日期+机器人ID能查询出相关敏感词操作记录')
            test_log.exception(e)
            pytest.fail("预期结果：按照日期+机器人ID能查询出相关敏感词操作记录")

    @allure.story("敏感词内容配置测试用例")
    @allure.description('''
                1.登录成功后在左侧导航栏中点击“全局配置>敏感词预警”打开敏感词预警页面
                2.点击【敏感词内容配置】按钮打开配置敏感词弹窗
                3.输入敏感词词条内容
                4.点击【保存】按钮并等待保存成功提示语句可见
                5.点击配置弹窗右上角的关闭按钮关掉配置窗口
                ''')
    def test_config_sensitive_word(self,page,login_hospital):
        userManagementPage = login_hospital
        # 打开全局配置菜单
        userManagementPage.global_configuration.click()
        userManagementPage.sensitive_word_warning_menu.click()
        sensitiveWordPage = SensitiveWordPage(page)
        try:
            sensitiveWordPage.sensitive_config_button.click()
            sensitiveWordPage.sensitive_config_textarea.fill("靠，偷渡，代孕，*奸*，偷税，漏税，共产党，国民党，吸毒，黄赌毒，杀人，犯人，溜冰，群殴，黑社会，洗钱，非法*")
            sensitiveWordPage.config_popups_save_button.click()
            sensitiveWordPage.operate_success_alert.wait_for()
            sensitiveWordPage.config_popups_close_button.click()
            test_log.info("敏感词内容配置测试通过")
        except Exception as e:
            allure.attach(page.screenshot(), "用例失败截图", allure.attachment_type.PNG)
            test_log.error('敏感词内容配置测试不通过')
            test_log.debug('预期结果：打开敏感词内容配置窗口输入敏感词词条点击保存，提示保存成功')
            test_log.exception(e)
            pytest.fail("预期结果：打开敏感词内容配置窗口输入敏感词词条点击保存，提示保存成功")





