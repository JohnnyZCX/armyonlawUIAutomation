"""
全局配置>用户管理页
"""
from playwright.async_api import Page


class UserManagement:
    def __init__(self,page:Page):
        self.page = page
        self.logout_button = self.page.locator("//div[@class=\"user-top\"]/img[2]")
        self.global_configuration = self.page.locator("ul[role=\"menubar\"] div:has-text(\"全局配置\")")
        self.logging_menu = self.page.locator("//ul[@role=\"menu\"]//i[@class=\"el-submenu__icon-arrow el-icon-arrow-down\"]") #日志记录菜单
        self.robot_log_menu = self.page.locator("//ul[@role=\"menu\"]/li[4]/ul[@role=\"menu\"]/li[1]") #机器人日志菜单
        self.cms_log_menu = self.page.locator("//ul[@role=\"menu\"]/li[4]/ul[@role=\"menu\"]/li[3]") #后台日志菜单
        self.unit_manage_menu = self.page.locator("text=机构管理") #机构管理菜单
        self.sensitive_word_warning_menu = self.page.locator("text=敏感词预警") #敏感词预警菜单
        self.feedback_manage_menu = self.page.locator("text=反馈管理") #反馈管理菜单
        self.questionnaire_manage_menu = self.page.locator("//*[@id=\"app\"]/section/div/section/aside/ul/li[1]/ul/li[3]") #问卷调查管理菜单
        self.equipment_manage_menu = self.page.locator("text=机器人管理") #机器人管理菜单
        self.switch_institution = self.page.locator("//*[@id=\"app\"]/section/header/div/div[2]/div[1]/div/div[1]/input") #选择机构框单选框
        self.switch_institution_again = self.page.locator("//*[@id=\"app\"]/section/header/div/div[2]/div[1]/div/div/input") #包含机构选项的选择机构单选框
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
        self.logout_confirm_button = self.page.locator("//div[@class=\"el-message-box\"]/div[@class=\"el-message-box__btns\"]/button[2]")


    def assertVisible(self,element):
        visible = self.page.is_visible(element)
        assert visible

    def assertText(self,element,text_value):
        text = self.page.inner_text(element)
        assert text ==  text_value

    def assertContent(self,element,content_value):
        content = self.page.text_content(element)
        assert content == content_value

