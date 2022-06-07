"""


"""
import pytest
from playwright.async_api import Page

from common.handle_logging import test_log
from pages.loginpage import LoginPage
from pages.usermanagementpage import UserManagement


#@pytest.mark.login
def test_login_fail(page:Page):
    loginPage = LoginPage(page)
    try:
        loginPage.login("zhengchunxing_11", "123456")
        loginPage.assertVisible('text=登录失败，账户名或密码错误')
        test_log.info("登录失败测试通过")
    except Exception as e:
        test_log.error("登录失败测试不通过")
        test_log.debug("预期结果：登录不成功并提示账户名或密码错误")
        test_log.exception(e)

#@pytest.mark.login

def test_login_pass(page: Page):
    loginPage = LoginPage(page)
    try:
        loginPage.login("zhengchunxing","axing_2010")
        userManagementPage = UserManagement(page)
        # 等待是否跳转成功
        userManagementPage.global_configuration.wait_for()
        test_log.info("登录成功测试通过")
    except Exception as e:
        test_log.error("登录成功测试不通过")
        test_log.debug("预期结果：登录成功并跳转")
        test_log.exception(e)



