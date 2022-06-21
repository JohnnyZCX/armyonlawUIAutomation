"""
新增用户页面字段校验
"""
import time

import pytest
from playwright.async_api import Page

from common.handle_logging import test_log
from pages.adduserpage import AddUser
from pages.usermanagementpage import UserManagement
from test.conftest import login
import allure

@allure.feature("新增用户页面")
class TestAddUser():
    #@pytest.mark.add_user
    @allure.story("新增用户测试用例")
    @allure.description('''
        1.点击新增按钮进入添加用户页
        2.在添加用户页面输入个人信息，添加权限配置，后点击保存，验证是否提示保存成功
        ''')
    def test_add_user(self,page:Page,login):
        #loginPage = LoginPage(page)
        #loginPage.login("zhengchunxing", "axing_2010")

        userManagementPage = login
        userManagementPage.add_user_button.click()
        addUserPage = AddUser(page)
        try:
            addUserPage.account_input.fill("zhangtiandi")
            addUserPage.nick_name_input.fill("Mr.Zhang")
            addUserPage.name_input.fill("xiaotiantian")
            addUserPage.password_input.fill("123456")
            addUserPage.confirm_password_input.fill("123456")
            addUserPage.save_button.click()
            addUserPage.upload_photo_alert.wait_for()
            addUserPage.upload_face_photo.set_input_files("test\\9ad2494035d47606fb66dad565748c4f.jpeg")
            addUserPage.upload_head_photo.set_input_files("test\\d15a281faa877cfe73f4d1adfcaa7f35.jpeg")
            addUserPage.local_configure_checkbox.click()
            addUserPage.save_button.click()
            # 等待跳转页面上提示保存成功
            time.sleep(0.5)
            userManagementPage.save_success_alert.wait_for()
            test_log.info("新增用户测试通过")
        except Exception as e:
            allure.attach(page.screenshot(), "用例失败截图", allure.attachment_type.PNG)
            test_log.error("新增用户测试不通过")
            test_log.debug("预期结果：新增用户点击保存按钮能保存成功并提示保存成功")
            test_log.exception(e)
            pytest.fail("预期结果：新增用户点击保存按钮能保存成功并提示保存成功")


    @allure.story("查询并删除用户测试用例")
    @allure.description('''
            1.在用户管理列表页输入账号查询条件
            2.点击【查询】按钮
            3.在查询结果列表中点击删除按钮
            4.在确认删除提示框中点击【确定】，查验是否提示删除成功
            ''')
    def test_delete_user(self,page:Page,login):
        userManagementPage = login
        #查询并删除该用户
        try:
            userManagementPage.account_input.fill("zhangtiandi")
            userManagementPage.search_button.click()
            userManagementPage.delete_account_button.click()
            userManagementPage.delete_confirm_button.click()
            time.sleep(2)
            userManagementPage.assertVisible("text=删除成功")
            test_log.info("查询用户并删除用户测试通过")
        except Exception as e:
            allure.attach(page.screenshot(), "用例失败截图", allure.attachment_type.PNG)
            test_log.error("查询用户并删除用户测试不通过")
            test_log.debug("预期结果：查询用户和删除用户能成功并提示删除成功")
            test_log.exception(e)
            pytest.fail("预期结果：查询用户和删除用户能成功并提示删除成功")







