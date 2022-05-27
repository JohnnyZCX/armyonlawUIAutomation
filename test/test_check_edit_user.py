"""
查看用户详情以及编辑用户详情
"""
import pytest
from playwright.async_api import Page

from pages.adduserpage import AddUser
from pages.loginpage import LoginPage
from pages.userdetailpage import UserDetailPage
from pages.usermanagementpage import UserManagement

@pytest.mark.check_edit_user
def test_check_edit_user(page: Page):
    loginPage = LoginPage(page)
    loginPage.login("zhengchunxing", "axing_2010")
    userManagementPage = UserManagement(page)
    userManagementPage.global_configuration.wait_for() #等待是否跳转成功
    userManagementPage.card_tab.click()
    userManagementPage.list_tab.click()
    userManagementPage.account_input.fill("zhengchunxing")
    userManagementPage.search_button.click()
    userManagementPage.check_details_button.click()
    userDetailPage = UserDetailPage(page)
    userDetailPage.assertVisible("li:has-text(\"zhengchunxing\")")
    userDetailPage.edit_detail_button.click()
    addUserPage = AddUser(page)
    #addUserPage.assertText("text=REGSRRP0S","REGSRRP0S")
    addUserPage.assertText("//*[@id=\"app\"]/section/div/section/main/div[2]/div/div[1]/form/div[2]/div[8]/div", "REGSRRP0S") #验证邀请码文本内容
    addUserPage.save_button.click()
    #userManagementPage.assertVisible("div[role=\"alert\"]:has-text(\"保存成功！\")")
    userManagementPage.save_success_alert.wait_for() #等待跳转页面上提示保存成功


