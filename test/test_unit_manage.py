"""测试机构切换/机构管理菜单/机构管理页面校验"""
#-*- coding: utf-8 -*-
import time

import allure
import pytest
from playwright.async_api import Page

from common.handle_logging import test_log
from pages.loginpage import LoginPage
from pages.unitmanagepage import UnitManage
from pages.usermanagementpage import UserManagement

@allure.feature("机构管理页面")
class TestUnitManage():
    @allure.story("机器人日志按条件查询并验证查询结果的用例")
    @allure.description('''
            1.使用超级管理员账号登录成功，后打开全局配置下拉菜单，查看机构管理菜单是否可见
            2.打开选择机构下拉列表，选择一个机构名称
            2.校验用户列表中机构名称是否正确
            3.再次打开选择机构列表切换为另一个机构名称
            4.再次校验用户列表中的机构名称是否正确
            5.点击机构管理菜单打开机构管理页面并校验页面指定元素是否可见
            6.点击新增按钮，后校验新增机构弹窗和新增机器人弹窗是否可见
            7.在机构列表中点击“机构管理”按钮，后校验编辑机构弹窗是否可见
            8.在弹窗中点击确定按钮并校验修改并更新机构成功提示语是否可见
            ''')
    def test_unit_manage(self,page:Page):
        loginPage = LoginPage(page)
        loginPage.login("superUserAdmin", "123789456")
        userManagementPage = UserManagement(page)
        userManagementPage.global_configuration.click()
        userManagementPage.assertVisible("text=机构管理")
        userManagementPage.switch_institution.click()
        userManagementPage.institution_list_qd.click()
        #校验用户列表中机构名称
        time.sleep(2)
        userManagementPage.assertText("//*[@id=\"app\"]/section/div/section/main/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]","擎盾大学勿删")

        userManagementPage.switch_institution_again.click()
        userManagementPage.institution_list_xa.click()
        time.sleep(2)
        userManagementPage.assertText("//*[@id=\"app\"]/section/div/section/main/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]", "国防科技大学-西安校区")

        userManagementPage.unit_manage_menu.click()
        unitManagePage = UnitManage(page)
        unitManagePage.assertVisible("th:has-text(\"单位编号\")")
        try:
            unitManagePage.new_unit_button.click()
            unitManagePage.assertVisible("label[role=\"radio\"]:has-text(\"新增机构\")")
            unitManagePage.assertVisible("label[role=\"radio\"]:has-text(\"新增机器人\")")
            unitManagePage.dialog_cancel_button.click()
            test_log.info("新增机构测试通过")
        except Exception as e:
            allure.attach(page.screenshot(), "用例失败截图", allure.attachment_type.PNG)
            test_log.error('新增机构测试不通过')
            test_log.debug('点击新增按钮会出现新增机构和新增机器人弹窗')
            test_log.exception(e)
            pytest.fail("点击新增按钮会出现新增机构和新增机器人弹窗")

        try:
            unitManagePage.edit_unit_button.click()
            unitManagePage.assertVisible("label[role=\"radio\"]:has-text(\"编辑机构\")")
            unitManagePage.dialog_confirm_button.click()
            # 校验更新成功提示语是否可见
            time.sleep(1)
            unitManagePage.assertVisible("//div[@role=\"alert\"]/p[@class=\"el-message__content\"]")
            test_log.info("编辑机构测试通过")
        except Exception as e:
            allure.attach(page.screenshot(), "用例失败截图", allure.attachment_type.PNG)
            test_log.error('编辑机构测试不通过')
            test_log.debug('编辑已存在的机构后点击确定会提示更新成功')
            test_log.exception(e)
            pytest.fail("编辑已存在的机构后点击确定会提示更新成功")
