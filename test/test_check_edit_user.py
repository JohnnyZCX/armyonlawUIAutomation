"""
查看用户详情以及编辑用户详情
"""
import time

import allure
import pytest
from playwright.async_api import Page

from common.handle_logging import test_log
from pages.adduserpage import AddUser
from test.conftest import login
from pages.userdetailpage import UserDetailPage
from pages.usermanagementpage import UserManagement

@allure.feature("编辑用户页面")
class TestCheckEditUser():
    #@pytest.mark.check_edit_user
    def test_check_edit_user(self,page: Page,login):
        userManagementPage = login
        # 等待是否跳转成功
        userManagementPage.global_configuration.wait_for()
        userManagementPage.card_tab.click()
        userManagementPage.list_tab.click()
        userManagementPage.account_input.fill("zhengchunxing")
        userManagementPage.search_button.click()
        userManagementPage.check_details_button.click()
        userDetailPage = UserDetailPage(page)
        time.sleep(1)
        userDetailPage.assertVisible("li:has-text(\"zhengchunxing\")")
        userDetailPage.edit_detail_button.click()
        addUserPage = AddUser(page)
        #addUserPage.assertText("text=REGSRRP0S","REGSRRP0S")
        # 验证邀请码文本内容
        addUserPage.assertText("//*[@id=\"app\"]/section/div/section/main/div[2]/div/div[1]/form/div[2]/div[8]/div", "REGSRRP0S")
        addUserPage.save_button.click()

        try:
            # 等待跳转页面上提示保存成功
            userManagementPage.save_success_alert.wait_for()
            test_log.info('用例查看和编辑用户通过')
        except Exception as e:
            test_log.error('用例查看和编辑用户不通过')
            test_log.debug('预期结果：保存成功并弹出提示语句')
            test_log.exception(e)

