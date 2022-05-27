from playwright.async_api import Page

from pages.addquestionnairepage import AddQuestionnaire
from pages.loginpage import LoginPage
from pages.questionnaireinvestigationpage import QuestionnaireInvestigation
from pages.usermanagementpage import UserManagement


def test_questionnaire_investigate(page:Page):
    loginPage = LoginPage(page)
    loginPage.login("zhengchunxing", "axing_2010")
    userManagementPage = UserManagement(page)
    userManagementPage.global_configuration.wait_for()  # 等待是否跳转成功
    userManagementPage.global_configuration.click()
    userManagementPage.questionnaire_manage_menu.click()
    questionnaireListPage = QuestionnaireInvestigation(page)
    questionnaireListPage.assertVisible("//label[@class=\"el-form-item__label\"]")
    questionnaireListPage.add_questionnaire_button.click()
    addQuestionnairePage = AddQuestionnaire(page)
    addQuestionnairePage.assertVisible("//textarea[@placeholder=\"示例问卷标题\"]")
    addQuestionnairePage.single_choice_button.click()
    addQuestionnairePage.assertVisible("//div[@class=\"choice-question-item\"][1]")
    addQuestionnairePage.multiple_choice_button.click()
    addQuestionnairePage.assertVisible("//div[@class=\"choice-question-item\"][2]")
    addQuestionnairePage.picture_choice_button.click()
    addQuestionnairePage.assertVisible("//div[@class=\"choice-question-item\"][3]")
    addQuestionnairePage.fill_blank_button.click()
    addQuestionnairePage.assertVisible("//div[@class=\"choice-question-item\"][4]")
    addQuestionnairePage.title_input.fill("擎盾大学问卷（一）")
    addQuestionnairePage.subhead_input.fill("这是性格分析测试题，如感兴趣请抽出5分钟时间参与回答！")
    addQuestionnairePage.cancel_button.click()
    questionnaireListPage.title_search_input.fill("擎盾大学问卷（一）")
    questionnaireListPage.date_icon.click()
    questionnaireListPage.date_table_today.click()
    questionnaireListPage.date_table_end_date.click()
    questionnaireListPage.search_button.click()
    questionnaireListPage.assertText("//span[@class=\"el-pagination__total\"]","共 0 条")
    questionnaireListPage.add_questionnaire_button.click()



