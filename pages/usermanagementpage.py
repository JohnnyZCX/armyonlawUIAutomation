"""
全局配置>用户管理页
"""
from playwright.async_api import Page


class UserManagement:
    def __init__(self,page:Page):
        self.page = page
        self.global_configuration = self.page.locator("ul[role=\"menubar\"] div:has-text(\"全局配置\")")
        self.unit_manage_menu = self.page.locator("text=机构管理") #机构管理菜单
        self.questionnaire_manage_menu = self.page.locator("//*[@id=\"app\"]/section/div/section/aside/ul/li[1]/ul/li[3]") #问卷调查管理菜单
        self.switch_institution = self.page.locator("//*[@id=\"app\"]/section/header/div/div[2]/div[1]/div/div[1]/input")
        self.switch_institution_again = self.page.locator("//*[@id=\"app\"]/section/header/div/div[2]/div[1]/div/div/input")
        self.institution_list_qd = self.page.locator("span:has-text(\"擎盾大学勿删\")") #选择机构列表的选项
        self.institution_list_xa = self.page.locator("span:has-text(\"国防科技大学-西安校区\")")  #选择机构列表的选项
        self.card_tab = self.page.locator("text=卡片展示")
        self.list_tab = self.page.locator("text=列表展示")
        self.account_input = self.page.locator("text=邀请码/账号: 注册日期: - 全部用户类型: 临时用户正式管理员专家用户全部注册来源: 门户网机器人后台查询 重置 新增批量导入下载模板 >> input[type=\"text\"] >> nth=0")
        # #全部用户类型（值设为'专家用户'）选择器封装
        #self.user_type_selector = self.page.query_selector("//ul/li[4]/span")
        self.search_button = self.page.locator("button:has-text(\"查询\")")
        self.check_details_button = self.page.locator("button:has-text(\"查看详情\")")
        self.edit_account_button = self.page.locator("button:has-text(\"编辑\")")
        self.delete_account_button = self.page.locator("button:has-text(\"删除\")")
        self.add_user_button = self.page.locator("button:has-text(\"新增\")")
        self.save_success_alert = self.page.locator("div[role=\"alert\"]:has-text(\"保存成功！\")")
        self.delete_confirm_button = self.page.locator("button:has-text(\"确定\")")


    def assertVisible(self,element):
        visible = self.page.is_visible(element)
        assert visible

    def assertText(self,element,text_value):
        text = self.page.inner_text(element)
        assert text ==  text_value

    def assertContent(self,element,content_value):
        content = self.page.text_content(element)
        assert content == content_value

