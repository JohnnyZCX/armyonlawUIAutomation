#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/22 9:49
# @Author : 郑春兴
# @Email : zhengchunxing@aegis-data.cn
# @File : robotpageconfig.py
# @Project : PlaywrightProject
from playwright.async_api import Page


class RobotPageConfig:
    def __init__(self,page:Page):
        self.page = page
        # 背景配置tab
        self.background_config_tab = self.page.locator("//div[@role=\"tablist\"]/div[text()=\"背景配置\"]")
        # 大屏配置tab
        self.big_screen_config_tab = self.page.locator("//div[@role=\"tablist\"]/div[text()=\"大屏配置\"]")
        # 大标题配置tab
        self.headline_config_tab = self.page.locator("//div[@role=\"tablist\"]/div[text()=\"大标题配置\"]")
        # 热门问题配置tab
        self.popular_questions_config_tab = self.page.locator("//div[@role=\"tablist\"]/div[text()=\"热门问题配置\"]")
        # 功能模块配置tab
        self.function_module_config_tab = self.page.locator("//div[@role=\"tablist\"]/div[text()=\"功能模块配置\"]")
        # 小机器人形象配置tab
        self.little_robot_figure_config_tab = self.page.locator("//div[@role=\"tablist\"]/div[text()=\"小机器人形象配置\"]")
        # 推荐问法配置tab
        self.recommended_question_config_tab = self.page.locator("//div[@role=\"tablist\"]/div[text()=\"推荐问法配置\"]")
        # 提交并同步按钮
        self.commit_sync_button = self.page.locator("button:has-text(\"提交并同步\")")
        # 背景配置中的待机背景按钮
        self.standby_background_button = self.page.locator("//span[@class=\"index-module_activeBtn_1g9j1 index-module_backgroundBtn_1KpUy\"]")
        # 机器人配置提交同步成功文本校验  //div[@class="deleteWarning"],机器人配置提交同步成功
        # 机器人配置同步成功提示框中的确定按钮
        self.commit_success_confirm_button = self.page.locator("//div[@class=\"index-module_bottomSubmit_mTa1n\"]/following-sibling::div//button")
        # 背景配置tab中的使用默认按钮
        self.background_config_set_default_button = self.page.locator("//span[@class=\"index-module_backgroundBtn_1KpUy\"]/ancestor::div[@class=\"index-module_header_2PLLL\"]/following-sibling::div//span[text()=\'使用默认\']")
        # 背景配置tab中上传背景图input标签
        self.upload_background_image = self.page.locator("//span[@class=\"index-module_backgroundBtn_1KpUy\"]/ancestor::div[@class=\"index-module_header_2PLLL\"]/following-sibling::div//input[@type=\'file\']")




    def assertText(self,element,text_value):
        text = self.page.inner_text(element)
        assert text ==  text_value



