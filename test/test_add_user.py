"""
新增用户页面字段校验
"""
import pytest
from playwright.async_api import Page

from common.handle_logging import test_log
from pages.adduserpage import AddUser
from pages.usermanagementpage import UserManagement
from test.conftest import login
import allure


#@pytest.mark.add_user
def test_add_user(page:Page,login):
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
        addUserPage.upload_face_photo.set_input_files("9ad2494035d47606fb66dad565748c4f.jpeg")
        addUserPage.upload_head_photo.set_input_files("d15a281faa877cfe73f4d1adfcaa7f35.jpeg")
        addUserPage.local_configure_checkbox.click()
        addUserPage.save_button.click()
        # 等待跳转页面上提示保存成功
        userManagementPage.save_success_alert.wait_for()
        test_log.info("新增用户测试通过")
    except Exception as e:
        test_log.error("新增用户测试不通过")
        test_log.debug("预期结果：新增用户点击保存按钮能保存成功")
        test_log.exception(e)

    #查询并删除该用户
    try:
        userManagementPage.account_input.fill("zhangtiandi")
        userManagementPage.search_button.click()
        userManagementPage.delete_account_button.click()
        userManagementPage.delete_confirm_button.click()
        userManagementPage.assertVisible("text=删除成功")
        test_log.info("查询用户并删除用户测试通过")
    except Exception as e:
        test_log.error("查询用户并删除用户测试不通过")
        test_log.debug("预期结果：查询用户和删除用户能成功")
        test_log.exception(e)






