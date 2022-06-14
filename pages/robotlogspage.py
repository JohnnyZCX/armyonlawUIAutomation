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
        # 开始日期输入框
        self.start_date_input = self.page.locator("//input[@placeholder=\"开始日期\"]") #开始日期输入框
        #结束日期输入框
        self.end_date_input = self.page.locator("//input[@placeholder=\"结束日期\"][@class=\"el-range-input\"]")  #结束日期输入框
        # 操作类型下拉箭头
        self.operation_type_drop_list = self.page.locator("text=操作类型：注册登录浏览咨询留言检索法规参与问卷调查收藏是否能答复：是否搜索 >> i >> nth=0")
        # 登录操作类型选项
        self.login_operation_type = self.page.locator("//li[@class=\"el-select-dropdown__item\"]/span[contains(text(), \'登录\')]")
        # 搜索按钮
        self.search_button = self.page.locator("//button[@class=\"el-button el-button--primary el-button--medium index-module_search__Pf4J\"]")

