#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/7 14:24
# @Author : 郑春兴
# @Email : zhengchunxing@aegis-data.cn
# @File : conftest.py
# @Project : PlaywrightProject
import os
from io import BytesIO

import allure
import playwright
import pytest

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
    loginPage.login(base_url,request.param['userName'], request.param['password'])
    userManagementPage = UserManagement(page)
    yield userManagementPage
    userManagementPage.logout_button.click()
    userManagementPage.logout_confirm_button.click()
    loginPage.page.context.close()
    loginPage.page.close()


@pytest.fixture()
def login_hospital(page: Page):
    loginPage = LoginPage(page)
    loginPage.login(base_url,"DoctorZheng", "123456")
    userManagementPage = UserManagement(page)
    yield userManagementPage
    userManagementPage.logout_button.click()
    userManagementPage.logout_confirm_button.click()
    loginPage.page.context.close()
    loginPage.page.close()
