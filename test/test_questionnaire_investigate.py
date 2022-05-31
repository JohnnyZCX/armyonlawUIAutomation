from playwright.async_api import Page

from common.handle_logging import test_log
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
    addQuestionnairePage.title_input.fill("擎盾大学问卷（一）")
    addQuestionnairePage.subhead_input.fill("这是综合知识测试题，如感兴趣请抽出5分钟时间参与回答！")
    addQuestionnairePage.single_choice_button.click()
    addQuestionnairePage.first_question_title_input.fill("香港与祖国内地的主要联系铁路是：")
    addQuestionnairePage.first_question_option1_input.fill("京沪线")
    addQuestionnairePage.first_question_option2_input.fill("京广线")
    addQuestionnairePage.first_question_add_option.click()
    addQuestionnairePage.first_question_option3_input.fill("京九线")
    addQuestionnairePage.first_question_add_option.click()
    addQuestionnairePage.first_question_option4_input.fill("广深线")
    addQuestionnairePage.multiple_choice_button.click()
    addQuestionnairePage.second_question_title_input.fill("我国四大发明有哪些？")
    addQuestionnairePage.second_question_option1_input.fill("造纸术")
    addQuestionnairePage.second_question_option2_input.fill("炼丹炉")
    addQuestionnairePage.second_question_add_option.click()
    addQuestionnairePage.second_question_option3_input.fill("火药")
    addQuestionnairePage.second_question_add_option.click()
    addQuestionnairePage.second_question_option4_input.fill("印刷术")
    addQuestionnairePage.second_question_add_option.click()
    addQuestionnairePage.second_question_option5_input.fill("指南针")
    addQuestionnairePage.picture_choice_button.click()
    addQuestionnairePage.third_question_title_input.fill("请选择以下包含军人的图片：")
    addQuestionnairePage.third_question_delete_button.click()
    addQuestionnairePage.dialog_confirm_button.click()

    addQuestionnairePage.publish_button.click()
    questionnaireListPage.title_search_input.fill("擎盾大学问卷（一）")
    questionnaireListPage.date_icon.click()
    questionnaireListPage.date_table_today.click()
    questionnaireListPage.date_table_end_date.click()
    questionnaireListPage.search_button.click()

    questionnaireListPage.published_questionnaire_button.click()
    try:
        questionnaireListPage.assertText("//span[@class=\"el-pagination__total\"]", "共 1 条")
    except AssertionError as e:
        test_log.error('问卷查询列表显示的问卷数量不通过')
        test_log.debug('预期结果：页面上查询出一条问卷数据')
        test_log.exception(e)

    else:
        test_log.info('问卷列表查询测试通过')


    #eles=page.query_selector_all('.questionnaire-box div:nth-child(2)')
    #print("4.---->",eles, len(eles))
    #eles[-1].hover(timeout=3000,force=True)
    try:
        questionnaireListPage.page.locator("//div[@class=\"questionnaire-item\"][2]/div[@class=\"questionnaire-bottom data\"]/div/div[2]").hover(timeout=3000,force=True)
        questionnaireListPage.page.locator("//p[text()=\"删除项目\"]").click()
        questionnaireListPage.dialog_confirm_button.click()
        questionnaireListPage.delete_success_alert.wait_for()
    except Exception as e:
        test_log.error('问卷删除测试不通过')
        test_log.debug('预期结果：问卷删除成功并出现提示语句')
        test_log.exception(e)
    else:
        test_log.info('问卷创建和删除测试通过')






















