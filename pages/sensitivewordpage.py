#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/16 11:07
# @Author : 郑春兴
# @Email : zhengchunxing@aegis-data.cn
# @File : sensitivewordpage.py
# @Project : PlaywrightProject

"""
敏感词页面封装
"""
from playwright.async_api import Page


class SensitiveWordPage:
    def __init__(self,page:Page):
        self.page = page
        # 日历图标
        self.date_icon = self.page.locator("//i[@class=\"el-input__icon el-range__icon el-icon-time\"]")
        # 日历部件中的开始日期输入框
        self.start_date_input = self.page.locator("//div[@class=\"el-picker-panel__body\"]//input[@placeholder=\"开始日期\"]")
        # 日历部件中的开始时间输入框
        self.start_time_inpput = self.page.locator("//div[@class=\"el-picker-panel__body\"]//input[@placeholder=\"开始时间\"]")
        # 日历部件中的结束日期输入框
        self.end_data_input = self.page.locator("//div[@class=\"el-picker-panel__body\"]//input[@placeholder=\"结束日期\"]")
        # 日历部件中的结束时间输入框
        self.end_time_input = self.page.locator("//div[@class=\"el-picker-panel__body\"]//input[@placeholder=\"结束时间\"]")
        # 日历部件底部确定按钮
        self.date_panel_confirm_button = self.page.locator("//div[@class=\"el-picker-panel__footer\"]/button[2]/span")
        # 机器人下拉箭头
        self.robot_drop_down_list = self.page.locator("//i[@class=\"el-select__caret el-input__icon el-icon-arrow-up\"]")
        # 机器人下拉列表第二个选项
        self.robot_list_second = self.page.locator("//ul[@class=\"el-scrollbar__view el-select-dropdown__list\"]/li[2]")
        # 搜索按钮
        self.search_button = self.page.locator("//button[@class=\"el-button el-button--primary el-button--medium index-module_search_3--Jz\"]")
        # 敏感词内容配置按钮
        self.sensitive_config_button = self.page.locator("//button[@class=\"el-button el-button--default el-button--medium index-module_config_1Vy18\"]")
        # 敏感词配置弹窗文本输入框
        self.sensitive_config_textarea = self.page.locator("//div[@class=\"ql-editor\"][@data-placeholder=\"请输入\"]")
        # 敏感词配置弹窗中的保存按钮
        self.config_popups_save_button = self.page.locator("//div[@class=\"el-dialog__wrapper\"]//div[@class=\"el-dialog__footer\"]//button[2]")
        # 敏感词配置弹窗关闭按钮
        self.config_popups_close_button = self.page.locator("//button[@class=\"el-dialog__headerbtn\"][@aria-label=\"Close\"]")
        # 保存成功提示语
        self.operate_success_alert = self.page.locator("//div[@role=\"alert\"]/p")



    def assertText(self,element,text_value):  #验证机器人ID列的值：//tr[@class="el-table__row"]/td[5]/div, D4A0D010020534M1D5
        text = self.page.inner_text(element)
        assert text ==  text_value