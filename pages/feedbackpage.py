#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/16 16:47
# @Author : 郑春兴
# @Email : zhengchunxing@aegis-data.cn
# @File : feedbackpage.py
# @Project : PlaywrightProject
from playwright.async_api import Page


class FeedbackPage:
    def __init__(self,page:Page):
        self.page = page
        # 处理状态选择下拉箭头
        self.status_drop_down_list = self.page.locator("//i[@class=\"el-select__caret el-input__icon el-icon-arrow-up\"]")
        # 处理状态第二个选项
        self.status_list_second = self.page.locator("//ul[@class=\"el-scrollbar__view el-select-dropdown__list\"]/li[2]")
        # 日历图标
        self.date_icon = self.page.locator("//i[@class=\"el-input__icon el-range__icon el-icon-time\"]")
        # 日历部件中的开始日期输入框
        self.start_date_input = self.page.locator("//div[@class=\"el-picker-panel__body\"]//input[@placeholder=\"开始日期\"]")
        # 日历部件中的结束日期输入框
        self.end_data_input = self.page.locator("//div[@class=\"el-picker-panel__body\"]//input[@placeholder=\"结束日期\"]")
        # 日历部件底部确定按钮
        self.date_panel_confirm_button = self.page.locator("//div[@class=\"el-picker-panel__footer\"]/button[2]/span")


    def assertText(self,element,text_value):  #验证处理状态列的值：//tr[@class="el-table__row"]/td[7]/div/span, 已处理
        text = self.page.inner_text(element)
        assert text ==  text_value





