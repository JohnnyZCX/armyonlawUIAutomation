#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/2 11:11
# @Author : 郑春兴
# @Email : zhengchunxing@aegis-data.cn
# @File : cmslogspage.py
# @Project : PlaywrightProject
"""
后台管理日志页面封装
"""
from playwright.async_api import Page


class CmsLogs:
    def __init__(self,page:Page):
        self.page = page
        self.user_account_input = self.page.locator("//div[@class=\"el-input el-input--medium index-module_userIpt_3U6PO\"]/input[@placeholder=\"请输入内容\"]") #操作用户输入框
        self.date_icon = self.page.locator("//i[@class=\"el-input__icon el-range__icon el-icon-time\"]")
        self.date_table_today = self.page.locator("//div[@class=\"el-picker-panel__content el-date-range-picker__content is-left\"]/table[@class=\"el-date-table\"]//td[@class=\"available today\"]") #日期控件今日日期
        self.date_table_end_date = self.page.locator("//div[@class=\"el-picker-panel__content el-date-range-picker__content is-right\"]//tr[4]//td[@class=\"available\"][1]") #结束日期元素
        self.date_table_confirm_button = self.page.locator("//button[@class=\"el-button el-picker-panel__link-btn el-button--default el-button--mini is-plain\"]") #日期控件确定按钮
        self.top_level_module_input = self.page.locator("//input[@placeholder=\"请选择一级模块\"]") #一级模块输入框
        self.global_manage_option = self.page.locator("li:has-text(\"全局管理\")")#一级模块--全局管理
        self.robot_manage_option = self.page.locator("li:has-text(\"机器人管理\")")#一级模块--机器人管理

        self.secondary_level_module_input = self.page.locator("//input[@placeholder=\"请选择二级模块\"]") #二级模块输入框
        self.questionnaire_investigate_option = self.page.locator("span:has-text(\"问卷调查管理\")") #二级模块--全局管理--问卷调查管理
        self.operation_type_input = self.page.locator("//input[@placeholder=\"请选择\"]") # 操作类型选择框
        self.add_operation_option = self.page.locator("li:has-text(\"新增\")") #新增操作类型选项
        self.search_button = self.page.locator("//div[@class=\"index-module_chooseTwo_2U1kY\"]/button[@class=\"el-button el-button--primary el-button--medium index-module_search__Pf4J\"]") #搜索按钮
        self.first_row_operate_type = self.page.locator("//table[@class=\"el-table__body\"]/tbody/tr/td[6]/div") #第一行日志记录操作类型列值：新增
        self.first_row_operate_content = self.page.locator("//table[@class=\"el-table__body\"]/tbody/tr/td[7]/div") #第一行日志记录操作内容列值：新增问卷：擎盾大学问卷（一）

    def assertText(self,element,text_value):
        text = self.page.inner_text(element)
        assert text ==  text_value

