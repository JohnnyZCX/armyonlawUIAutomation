"""
用户详情页页面封装
"""
from playwright.async_api import Page


class UserDetailPage:
    def __init__(self,page:Page):
        self.page = page
        self.account_text = self.page.locator("li:has-text(\"zhengchunxing\")")
        self.edit_detail_button = self.page.locator("button:has-text(\"编辑\")")

    def assertVisible(self,element):
        visible = self.page.is_visible(element)
        assert visible


