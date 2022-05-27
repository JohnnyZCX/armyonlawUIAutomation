import pytest
from playwright.async_api import Page
from pages.loginpage import LoginPage
from pages.usermanagementpage import UserManagement


@pytest.mark.login
def test_login_fail(page:Page):
    loginPage = LoginPage(page)
    loginPage.login("zhengchunxing_11", "123456")
    loginPage.assertVisible('text=登录失败，账户名或密码错误')

@pytest.mark.login
@pytest.mark.dependency()
def test_login_pass(page: Page):
    loginPage = LoginPage(page)
    loginPage.login("zhengchunxing", "axing_2010")
    userManagementPage = UserManagement(page)
    userManagementPage.global_configuration.wait_for() #等待是否跳转成功


