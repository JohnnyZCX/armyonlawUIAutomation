#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/1 14:39
# @Author : 郑春兴
# @Email : zhengchunxing@aegis-data.cn
# @File : robotlogspage.py
# @Project : PlaywrightProject
from playwright.async_api import Page


class RobotLogs:
    def __init__(self,page:Page):
        self.page = page
        self.user_input = self.page.locator("//div[@class=\"el-input el-input--medium index-module_userIpt_3U6PO\"]/input[@placeholder=\"请输入内容\"]")
        self.operation_type_input = self.page.locator("//input[@placeholder=\"请选择\"]")
        #日历图标
        self.date_icon = self.page.locator("//i[@class=\"el-input__icon el-range__icon el-icon-time\"]")
        # 日期控件今日日期
        self.date_table_today = self.page.locator("//div[@class=\"el-picker-panel__content el-date-range-picker__content is-left\"]/table[@class=\"el-date-table\"]//td[@class=\"available today\"]")
        #结束日期元素
        self.date_table_end_date = self.page.locator("//div[@class=\"el-picker-panel__content el-date-range-picker__content is-right\"]//tr[4]//td[@class=\"available\"][1]")
        # 日期控件确定按钮
        self.date_table_confirm_button = self.page.locator("//button[@class=\"el-button el-picker-panel__link-btn el-button--default el-button--mini is-plain\"]")


