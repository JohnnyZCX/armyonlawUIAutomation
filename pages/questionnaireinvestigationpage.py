"""问卷调查管理页"""
from playwright.async_api import Page


class QuestionnaireInvestigation:
    def __init__(self,page:Page):
        self.page = page
        self.title_search_input = self.page.locator("//form[@class=\"el-form el-form--inline\"]/div[1]//input")
        self.date_icon = self.page.locator("//i[@class=\"el-input__icon el-range__icon el-icon-date\"]")
        self.date_table_today = self.page.locator("//td[@class=\"available today\"]")
        self.date_table_end_date = self.page.locator("//div[@class=\"el-picker-panel__content el-date-range-picker__content is-right\"]//tr[4]//td[@class=\"available\"][1]")
        self.search_button = self.page.locator("//div[@class=\"el-form-item__content\"]/button[1]") #查询按钮
        self.all_questionnaire_button = self.page.locator("//div[@class=\"el-button-group\"]/button[1]") #全部问卷tab
        self.template_questionnaire_button = self.page.locator("//div[@class=\"el-button-group\"]/button[2]") #模板文件tab
        self.published_questionnaire_button = self.page.locator("//div[@class=\"el-button-group\"]/button[2]") #发布问卷tab
        self.add_questionnaire_button = self.page.locator("//div[@class=\"questionnaire-list\"]//div[@class=\"add-questionnaire\"]") #新增问卷按钮

    def assertVisible(self,element):
        visible = self.page.is_visible(element)
        assert visible

    def assertText(self,element,text_value):
        text = self.page.inner_text(element)
        assert text ==  text_value
