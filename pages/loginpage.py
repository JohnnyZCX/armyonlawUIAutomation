"""
管理后台登录页
"""
import pytest
from playwright.async_api import Page


class LoginPage:
    def __init__(self,page:Page):
        self.page = page
        self.password_input = self.page.locator("[placeholder=\"请输入密码\"]")
        self.user_account = self.page.locator("[placeholder=\"请输入账号\"]")
        self.login_button = self.page.locator("button:has-text(\"登录\")")

    def login(self,userName,password):
        # 页面窗口最大化
        self.page.set_viewport_size({"width": 1920, "height": 1080})
        self.page.goto("https://t-rulearmylaw.aegis-info.com/login")
        visible = self.page.is_visible('[placeholder=\"请输入密码\"]')
        assert visible
        self.password_input.fill(password)
        self.user_account.fill(userName)
        self.login_button.click()

    def assertVisible(self,element):
        visible = self.page.is_visible(element)
        assert visible





