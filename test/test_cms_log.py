#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/2 15:11
# @Author : 郑春兴
# @Email : zhengchunxing@aegis-data.cn
# @File : test_cms_log.py
# @Project : PlaywrightProject
import time

from playwright.async_api import Page

from common.handle_logging import test_log
from pages.cmslogspage import CmsLogs
from test.conftest import login
from pages.usermanagementpage import UserManagement


def test_cms_log(page,login):
    userManagementPage = login
    # 打开全局配置菜单
    userManagementPage.global_configuration.click()
    # 打开日志记录下拉菜单
    userManagementPage.logging_menu.click()
    # 点击后台日志菜单
    userManagementPage.cms_log_menu.click()
    # 实例化后台日志页
    cmsLogsPage = CmsLogs(page)
    try:
        # 操作用户输入
        cmsLogsPage.user_account_input.fill("zhengchunxing")
        # 点击日历控件
        cmsLogsPage.date_icon.click()
        # 选择今日日期作为开始日期
        cmsLogsPage.date_table_today.click()
        # 选择一个结束日期
        cmsLogsPage.date_table_end_date.click()
        # 点击日历控件上的确定按钮
        cmsLogsPage.date_table_confirm_button.click()
        # 打开一级模块选择下拉列表
        cmsLogsPage.top_level_module_input.click()
        # 选择全局管理一级模块
        cmsLogsPage.global_manage_option.click()
        # 二级模块选择
        cmsLogsPage.secondary_level_module_input.click()
        # 选择问卷调查管理
        cmsLogsPage.questionnaire_investigate_option.click()
        # 操作类型选择
        cmsLogsPage.operation_type_input.click()
        # 选择新增操作类型
        cmsLogsPage.add_operation_option.click()
        # 点击搜索按钮
        cmsLogsPage.search_button.click()
        time.sleep(1)
        cmsLogsPage.assertText("//table[@class=\"el-table__body\"]/tbody/tr/td[6]/div","新增")
        cmsLogsPage.assertText("//table[@class=\"el-table__body\"]/tbody/tr/td[7]/div","新增问卷：擎盾大学问卷（一）")
        test_log.info("后台日志测试通过")
    except Exception as e:
        test_log.error('后台日志测试不通过')
        test_log.debug('预期结果：按照用户+日期+模块名+操作类型能查询出相关日志记录')
        test_log.exception(e)


