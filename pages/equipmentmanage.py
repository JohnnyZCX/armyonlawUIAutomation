#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/21 9:48
# @Author : 郑春兴
# @Email : zhengchunxing@aegis-data.cn
# @File : equipmentmanage.py
# @Project : PlaywrightProject
from playwright.async_api import Page


class EquipmentManage:
    def __init__(self,page:Page):
        self.page = page
        # 机器人编号输入框
        self.robot_number_input = self.page.locator("//input[@placeholder=\"请输入机器人编号\"]")
        # 机器人名称输入框
        self.robot_name_input = self.page.locator("//input[@placeholder=\"请输入机器人名称\"]")
        # 查询按钮
        self.search_button = self.page.locator("//form[@class=\"el-form el-form--inline\"]//button")
        # 机构管理菜单
        self.unit_manage_menu = self.page.locator("text=机构管理")
        # 列表中第一行机器人的编号值  //table[@class="el-table__body"]//tr[1]/td[2]/div,20220621201
        # 列表中第一行机器人的名称值 //table[@class="el-table__body"]//tr[1]/td[3]/div,修改已有的机器人
        # 列表中查询无数据的文本校验 //span[@class="el-table__empty-text"],暂无数据

    def assertText(self,element,text_value):
        text = self.page.inner_text(element)
        assert text ==  text_value
