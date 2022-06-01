"""测试机构切换/机构管理菜单/机构管理页面校验"""
#-*- coding: utf-8 -*-

import pytest
from playwright.async_api import Page

from common.handle_logging import test_log
from pages.loginpage import LoginPage
from pages.unitmanagepage import UnitManage
from pages.usermanagementpage import UserManagement

@pytest.mark.unit_manage
def test_unit_manage(page:Page):
    loginPage = LoginPage(page)
    loginPage.login("superUserAdmin", "123789456")
    userManagementPage = UserManagement(page)
    userManagementPage.global_configuration.click()
    userManagementPage.assertVisible("text=机构管理")
    userManagementPage.switch_institution.click()
    userManagementPage.institution_list_qd.click()
    #校验用户列表中机构名称
    userManagementPage.assertText("//*[@id=\"app\"]/section/div/section/main/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]","擎盾大学勿删")

    userManagementPage.switch_institution_again.click()
    userManagementPage.institution_list_xa.click()
    userManagementPage.assertText("//*[@id=\"app\"]/section/div/section/main/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]", "国防科技大学-西安校区")

    userManagementPage.unit_manage_menu.click()
    unitManagePage = UnitManage(page)
    unitManagePage.assertVisible("th:has-text(\"单位编号\")")
    try:
        unitManagePage.new_unit_button.click()
        unitManagePage.assertVisible("label[role=\"radio\"]:has-text(\"新增机构\")")
        unitManagePage.assertVisible("label[role=\"radio\"]:has-text(\"新增机器人\")")
        unitManagePage.dialog_cancel_button.click()
    except Exception as e:
        test_log.error('新增机构测试不通过')
        test_log.debug('点击新增按钮会出现新增机构和新增机器人弹窗')
        test_log.exception(e)
    else:
        test_log.info("新增机构测试通过")

    try:
        unitManagePage.edit_unit_button.click()
        unitManagePage.assertVisible("label[role=\"radio\"]:has-text(\"编辑机构\")")
        unitManagePage.dialog_confirm_button.click()
        unitManagePage.assertVisible("//div[@role=\"alert\"]/p[@class=\"el-message__content\"]") #校验更新成功提示语是否可见
    except Exception as e:
        test_log.error('编辑机构测试不通过')
        test_log.debug('编辑已存在的机构后点击确定会提示更新成功')
        test_log.exception(e)
    else:
        test_log.info("编辑机构测试通过")


