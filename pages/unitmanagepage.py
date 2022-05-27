"""机构管理页"""
from playwright.async_api import Page


class UnitManage:
    def __init__(self,page:Page):
        self.page = page

        self.new_unit_button = self.page.locator("//*[@id=\"app\"]/section/div/section/main/div[2]/div/button")
        self.edit_unit_button = self.page.locator("//*[@id=\"app\"]/section/div/section/main/div[2]/div/div/div[3]/table/tbody/tr/td[6]/div/button")
        self.dialog_cancel_button = self.page.locator("button:has-text(\"取 消\")")
        self.dialog_confirm_button = self.page.locator("button:has-text(\"确 定\")")

    def assertVisible(self,element):
        visible = self.page.is_visible(element)
        assert visible
