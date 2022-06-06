import pytest
from playwright.async_api import Page
from playwright.sync_api import Playwright

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
        userManagementPage.global_configuration.wait_for() #等待是否跳转成功
        test_log.info("登录成功测试通过")
    except Exception as e:
        test_log.error("登录成功测试不通过")
        test_log.debug("预期结果：登录成功并跳转")
        test_log.exception(e)

data = [{'userName':"zhengchunxing",'password':"axing_2010"}]
ids = ['user_login']
@pytest.fixture(params=data,ids=ids)
def login(page: Page,request):
    loginPage = LoginPage(page)
    loginPage.login(request.param['userName'], request.param['password'])
    userManagementPage = UserManagement(page)
    yield
    userManagementPage.logout_button.click()
    userManagementPage.delete_confirm_button.click()
    loginPage.page.context.close()
    loginPage.page.close()
    userManagementPage.page.context.close()
    userManagementPage.page.close()



