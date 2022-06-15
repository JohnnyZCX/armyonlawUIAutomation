#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/7 14:24
# @Author : 郑春兴
# @Email : zhengchunxing@aegis-data.cn
# @File : conftest.py
# @Project : PlaywrightProject
import inspect
import os
from io import BytesIO

import allure
import playwright
import pytest
from PIL import ImageDraw, Image

from playwright.async_api import Page
from pytest_base_url.plugin import base_url

from common.handle_logging import test_log
from pages.loginpage import LoginPage
from pages.usermanagementpage import UserManagement

data = [{'userName': "zhengchunxing", 'password': "axing_2010"}]
ids = ['user_login']


@pytest.fixture(params=data, ids=ids)
def login(page: Page, request):
    loginPage = LoginPage(page)
    loginPage.login(request.param['userName'], request.param['password'])
    userManagementPage = UserManagement(page)
    yield userManagementPage
    userManagementPage.logout_button.click()
    userManagementPage.logout_confirm_button.click()
    loginPage.page.context.close()
    loginPage.page.close()


@pytest.fixture(params=data, ids=ids)
def login_hospital(page: Page):
    loginPage = LoginPage(page)
    loginPage.login("DoctorZheng", "123456")
    userManagementPage = UserManagement(page)
    yield userManagementPage
    userManagementPage.logout_button.click()
    userManagementPage.logout_confirm_button.click()
    loginPage.page.context.close()
    loginPage.page.close()


def highlight_screenshot(page, element, tips='高亮截图'):
    # 滚动页面将元素移动到视野中
    element.scroll_into_view_if_needed()

    # 获取元素的位置信息
    box = element.bounding_box()
    x, y, width, height = box['x'], box['y'], box['width'], box['height']

    # 获取页面截图，并读取为PIL.Image对象
    png = page.screenshot(type='png')
    img = Image.open(BytesIO(png))

    # 利用元素的位置信息在页面截图中标记出元素
    draw = ImageDraw.Draw(img)
    draw.rectangle((x, y, x + width, y + height), outline='red', width=3)

    # 将标记后的截图保存至allure报告中
    with BytesIO() as output:
        img.save(output, format='png')
        allure.attach(output.getvalue(), tips, allure.attachment_type.PNG)
