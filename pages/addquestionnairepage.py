"""创建问卷页"""
from playwright.async_api import Page


class AddQuestionnaire:
    def __init__(self,page:Page):
        self.page = page
        self.single_choice_button = self.page.locator("//div[@class=\"question-type\"]/div[1]") #单选题按钮
        self.multiple_choice_button = self.page.locator("//div[@class=\"question-type\"]/div[2]") #多选按钮
        self.picture_choice_button = self.page.locator("//div[@class=\"question-type\"]/div[3]") #图片选择
        self.fill_blank_button = self.page.locator("//div[@class=\"question-type\"]/div[4]") #填空题
        self.title_input = self.page.locator("//textarea[@placeholder=\"示例问卷标题\"]") #问卷标题
        self.subhead_input = self.page.locator("//div[@class=\"questionnaire-description el-textarea el-input--medium\"]/textarea") #问卷副标题
        self.cancel_button = self.page.locator("//div[@class=\"btn-box\"]/button[1]")
        self.save_as_template_button = self.page.locator("//div[@class=\"btn-box\"]/button[2]")
        self.preview_button = self.page.locator("//div[@class=\"btn-box\"]/button[3]")
        self.publish_button = self.page.locator("//div[@class=\"btn-box\"]/button[4]")
        self.first_question_title_input = self.page.locator("//div[@class=\"choice-question-item\"][1]//textarea")
        self.second_question_title_input = self.page.locator("//div[@class=\"choice-question-item\"][2]//textarea")
        self.third_question_title_input = self.page.locator("//div[@class=\"choice-question-item\"][3]//textarea")
        self.forth_question_title_input = self.page.locator("//div[@class=\"choice-question-item\"][4]//textarea")
        self.first_question_option1_input = self.page.locator("//div[@class=\"choice-question-item\"][1]//div[@class=\"radio-box\"]/div[1]//input")
        self.first_question_option2_input = self.page.locator("//div[@class=\"choice-question-item\"][1]//div[@class=\"radio-box\"]/div[2]//input")
        self.first_question_add_option = self.page.locator("//div[@class=\"choice-question-item\"][1]//div[@class=\"radio-item-add\"]")
        self.first_question_option3_input = self.page.locator("//div[@class=\"choice-question-item\"][1]//div[@class=\"radio-box\"]/div[3]//input")
        self.second_question_delete_button = self.page.locator("//div[@class=\"choice-question-item\"][2]/div[@class=\"operation\"]/div[@class=\"drag del\"]")

    def assertVisible(self,element):
        visible = self.page.is_visible(element)
        assert visible
