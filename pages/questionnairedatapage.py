#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/2 9:33
# @Author : 郑春兴
# @Email : zhengchunxing@aegis-data.cn
# @File : questionnairedatapage.py
# @Project : PlaywrightProject
from playwright.async_api import Page


class QuestionnaireData:
    def __init__(self,page:Page):
        self.page = page
        self.questionnaire_title = self.page.locator("//h1[@class=\"title\"]")
        self.back_button = self.page.locator("//div[@class=\"btn\"]/button[@class=\"el-button el-button--default el-button--medium\"]")

    def assertText(self,element,text_value):
        text = self.page.inner_text(element)
        assert text ==  text_value

