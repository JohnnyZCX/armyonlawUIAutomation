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

@allure.feature("查看并编辑用户页面")
class TestCheckEditUser():
    @allure.story("查看用户详情并编辑用户信息的用例")
    @allure.description('''
        1.登录后查看全局配置菜单是否可见
        2.点击用户管理页的卡片展示tab
        3.点击用户管理页的列表展示tab
        4.账号输入框输入“zhengchunxing”
        5.点击查询按钮
        6.点击操作栏下的“查看详情”按钮跳转用户详情页
        7.在用户详情页判断账号是否显示“zhengchunxing”
        8.点击编辑按钮刷新成编辑用户页面
        9.先在编辑用户页校验注册邀请码是否正确（由于注册邀请码都是唯一的，所以校验这个字段值是否正确）
        10.直接点击保存按钮，并等待页面提示保存成功
        ''')
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

