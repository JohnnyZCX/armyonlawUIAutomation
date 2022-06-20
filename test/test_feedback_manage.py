#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/17 15:19
# @Author : 郑春兴
# @Email : zhengchunxing@aegis-data.cn
# @File : test_feedback_manage.py
# @Project : PlaywrightProject
import time

import allure
import pytest

from common.handle_logging import test_log
from pages.feedbackpage import FeedbackPage

@allure.feature("反馈管理页面")
class TestFeedbackManage():
    @allure.story("查询咨询反馈测试用例")
    @allure.description('''
                1.登录成功后在左侧导航栏中点击“全局配置>反馈管理”打开反馈管理页面，并校验指定元素（咨询反馈tab）是否可见
                2.打开处理状态下拉列表，选择已处理
                3.操作日期中输入2022-05-01至2022-05-30
                4.在查询反馈结果列表中判断处理状态列的值是否为“已处理”
                ''')
    def test_query_feedback(self,page,login_hospital):
        userManagementPage = login_hospital
        # 打开全局配置菜单
        userManagementPage.global_configuration.click()
        userManagementPage.feedback_manage_menu.click()
        try:
            feedbackManagePage = FeedbackPage(page)
            feedbackManagePage.consult_feedback_tab.wait_for()
            feedbackManagePage.status_drop_down_list.click()
            feedbackManagePage.status_list_second.click()
            feedbackManagePage.date_icon.click()
            feedbackManagePage.start_date_input.fill("2022-05-01")
            feedbackManagePage.end_date_input.fill("2022-05-30")
            feedbackManagePage.date_panel_confirm_button.click()
            time.sleep(1)
            feedbackManagePage.assertText("//tr[@class=\"el-table__row\"]/td[7]/div/span","已处理")
            test_log.info("查询咨询反馈测试通过")
        except Exception as e:
            allure.attach(page.screenshot(), "用例失败截图", allure.attachment_type.PNG)
            test_log.error('查询咨询反馈测试不通过')
            test_log.debug('预期结果：按照处理状态+操作日期能查询出相关咨询反馈记录')
            test_log.exception(e)
            pytest.fail("预期结果：按照处理状态+操作日期能查询出相关咨询反馈记录")

    @allure.story("查看反馈详情测试用例")
    @allure.description('''
                    1.登录成功后在左侧导航栏中点击“全局配置>反馈管理”打开反馈管理页面，并校验指定元素（咨询反馈tab）是否可见
                    2.打开处理状态下拉列表，选择已处理
                    3.操作日期中输入2022-05-01至2022-05-30
                    4.在查询反馈结果列表中获取反馈时间的值并赋给变量存储
                    5.在列表中点击"详情查看"按钮打开反馈详情窗口
                    6.在详情中判断反馈时间字段值是否为列表中获取的反馈时间
                    ''')
    def test_view_feedback_details(self,page,login_hospital):
        userManagementPage = login_hospital
        # 打开全局配置菜单
        userManagementPage.global_configuration.click()
        userManagementPage.feedback_manage_menu.click()
        try:
            feedbackManagePage = FeedbackPage(page)
            feedbackManagePage.consult_feedback_tab.wait_for()
            feedbackManagePage.status_drop_down_list.click()
            feedbackManagePage.status_list_second.click()
            feedbackManagePage.date_icon.click()
            feedbackManagePage.start_date_input.fill("2022-05-01")
            feedbackManagePage.end_date_input.fill("2022-05-30")
            feedbackManagePage.date_panel_confirm_button.click()
            # 获取列表中第一条反馈记录的反馈时间值
            feedback_time = feedbackManagePage.getElementContent("//tr[@class=\"el-table__row\"]/td[2]/div")
            feedbackManagePage.view_details_button.click()
            time.sleep(1)
            feedbackManagePage.assertText("//div[@class=\"el-dialog__body\"]//div[@class=\"index-module_detailTitle_3VXsW\"][1]","反馈时间: "+feedback_time)
            feedbackManagePage.forward_back_button.click()
            test_log.info("查看反馈详情测试通过")

        except Exception as e:
            allure.attach(page.screenshot(), "用例失败截图", allure.attachment_type.PNG)
            test_log.error('查看反馈详情测试不通过')
            test_log.debug('预期结果：反馈详情的数据应该与反馈记录列表中的一致')
            test_log.exception(e)
            pytest.fail("预期结果：反馈详情的数据应该与反馈记录列表中的一致")










