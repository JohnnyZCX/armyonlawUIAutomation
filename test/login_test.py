"""


"""
import time

import allure
import pytest
from playwright.async_api import Page
from pytest_base_url.plugin import base_url

from common.handle_logging import test_log
from pages.loginpage import LoginPage
from pages.usermanagementpage import UserManagement


#@pytest.mark.login
@allure.feature("登录页面")
class TestLogin():
    @allure.story("登录失败的用例")
    @allure.description('''
    1.登录页面输入错误的账号和密码
    2.断言登录失败提示语句是否可见
    3.输出测试通过或不通过日志
    ''')
    def test_login_fail(self,page:Page):
        loginPage = LoginPage(page)
        try:
            loginPage.login("zhengchunxing_11", "123456")
            time.sleep(2)
            loginPage.assertVisible('text=登录失败，账户名或密码错误')
            test_log.info("登录失败测试通过")
        except Exception as e:
            allure.attach(page.screenshot(), "用例失败截图", allure.attachment_type.PNG)
            test_log.error("登录失败测试不通过")
            test_log.debug("预期结果：登录不成功并提示账户名或密码错误")
            test_log.exception(e)
            pytest.fail("预期结果：登录不成功并提示账户名或密码错误")

    #@pytest.mark.login
    @allure.story("登录成功的用例")
    @allure.description('''
    1.登录页面输入正确的账号和密码并点击登录
    2.用户管理页面等待全局配置菜单元素可见
    3.输出测试通过或不通过日志
    ''')
    def test_login_pass(self,page:Page):
        loginPage = LoginPage(page)
        try:
            #loginPage.login("zhengchunxing","axing_2010")
            loginPage.login("zhengchunxing", "axing_2010")
            userManagementPage = UserManagement(page)
            # 等待是否跳转成功
            userManagementPage.global_configuration.wait_for()
            test_log.info("登录成功测试通过")
        except Exception as e:
            allure.attach(page.screenshot(),"用例失败截图",allure.attachment_type.PNG)
            test_log.error("登录成功测试不通过")
            test_log.debug("预期结果：登录成功并跳转用户管理")
            test_log.exception(e)
            pytest.fail("预期结果：登录成功并跳转用户管理页")



