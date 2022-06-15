"""
问卷调查管理模块新增问卷/保存为模板/编辑问卷/发布问卷
/设为推荐/查看统计数据/删除问卷等操作
"""
import time

import allure
import pytest
from playwright.async_api import Page

from common.handle_logging import test_log
from pages.addquestionnairepage import AddQuestionnaire
from test.conftest import login
from pages.questionnairedatapage import QuestionnaireData
from pages.questionnaireinvestigationpage import QuestionnaireInvestigation
from pages.usermanagementpage import UserManagement
@allure.feature("问卷调查管理页面")
class TestQuesitionnaireInvestigate():
    @allure.story("新增问卷/问卷保存为模板/查询问卷/编辑和发布问卷/设置推荐/查看统计数据/删除问卷的用例")
    @allure.description('''
        1.登录后校验全局配置菜单是否可见
        2.点击左侧导航栏菜单“全局配置>问卷调查管理”打开问卷调查管理页，并校验指定元素是否可见
        3.问卷管理列表中点击新增问卷按钮进入创建问卷页面，并校验指定元素是否可见
        4.分别添加单选题/多选题/图片选择题和填空题，依次为题目添加选项
        5.题目添加完成后点击【存为模板】按钮
        6.在问卷调查管理页中输入问卷调查标题并点击查询按钮校验查询结果条数是否正确
        7.点击编辑操作，后在编辑问卷页点击取消按钮
        8.在问卷列表上点击发布操作，确认是否发布提示中点击【确定】按钮
        9.按照问卷调查标题，问卷发布日期和已发布状态查询问卷，并校验查询结果条数是否1条
        10.在问卷上点击数据按钮跳转问卷数据统计页面并校验问卷标题是否正确
        11.在问卷上点击设为推荐并校验是否出现推荐成功的提示语
        12.在问卷上点击删除项目，在确认删除提示中点击确定，后校验删除成功提示语
        ''')
    def test_questionnaire_investigate(self,page:Page,login):
        userManagementPage = login
        # 等待是否跳转成功
        userManagementPage.global_configuration.wait_for()
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

        addQuestionnairePage.save_as_template_button.click()
        questionnaireListPage.title_search_input.fill("擎盾大学问卷（一）")
        questionnaireListPage.search_button.click()

        questionnaireListPage.template_questionnaire_button.click()
        try:
            questionnaireListPage.assertText("//span[@class=\"el-pagination__total\"]", "共 1 条")
            test_log.info('新增问卷并存为模板测试通过/查询问卷测试通过')
        except AssertionError as e:
            allure.attach(page.screenshot(), "用例失败截图", allure.attachment_type.PNG)
            test_log.error('问卷查询列表显示的问卷数量不通过')
            test_log.debug('预期结果：页面上查询出一条问卷数据')
            test_log.exception(e)
            pytest.fail("预期结果：页面上查询出一条问卷数据（问卷标题：擎盾大学问卷（一））")

        questionnaireListPage.page.locator("//div[@class=\"questionnaire-item\"][2]/div[@class=\"questionnaire-bottom data\"]/div/div[2]").hover(timeout=3000, force=True)
        # 点击编辑
        questionnaireListPage.page.locator("//div[@class=\"questionnaire-item\"][2]/div[@class=\"questionnaire-bottom\"]//span[@class=\"edit\"]").click()
        addQuestionnairePage.cancel_button.click()
        time.sleep(2)
        questionnaireListPage.page.locator("//div[@class=\"questionnaire-item\"][2]/div[@class=\"questionnaire-bottom data\"]/div/div[2]").hover(timeout=3000, force=True)
        # 点击发布
        questionnaireListPage.page.locator("//div[@class=\"questionnaire-item\"][2]/div[@class=\"questionnaire-bottom\"]//span[@class=\"release\"]").click()
        questionnaireListPage.dialog_confirm_button.click()
        time.sleep(2)
        questionnaireListPage.title_search_input.fill("擎盾大学问卷（一）")
        questionnaireListPage.date_icon.click()
        questionnaireListPage.date_table_today.click()
        questionnaireListPage.date_table_end_date.click()
        questionnaireListPage.search_button.click()
        questionnaireListPage.published_questionnaire_button.click()
        try:
            questionnaireListPage.assertText("//span[@class=\"el-pagination__total\"]", "共 1 条")
            test_log.info('发布问卷测试通过')
        except AssertionError as e:
            allure.attach(page.screenshot(), "用例失败截图", allure.attachment_type.PNG)
            test_log.error('问卷查询列表显示的发布问卷数量不通过')
            test_log.debug('预期结果：页面上查询出一条问卷数据')
            test_log.exception(e)
            pytest.fail("预期结果：页面上查询出一条问卷数据")

        try:
            time.sleep(2)
            questionnaireListPage.page.locator("//div[@class=\"questionnaire-item\"][2]/div[@class=\"questionnaire-bottom data\"]/div/div[2]").hover(timeout=3000, force=True)
            # 点击数据按钮
            questionnaireListPage.page.locator("//div[@class=\"questionnaire-item\"][2]/div[@class=\"questionnaire-bottom\"]//span[@class=\"data\"]").click()
            questionnaireDataPage = QuestionnaireData(page)
            time.sleep(2)
            questionnaireDataPage.assertText("//h1[@class=\"title\"]","擎盾大学问卷（一）")
            questionnaireDataPage.back_button.click()
            test_log.info("点击数据按钮跳转问卷数据页面测试通过")
        except Exception as e:
            allure.attach(page.screenshot(), "用例失败截图", allure.attachment_type.PNG)
            test_log.error("点击数据按钮跳转问卷数据页面测试不通过")
            test_log.debug("预期结果：点击问卷底部数据按钮能跳转问卷数据统计页面")
            test_log.exception(e)
            pytest.fail("预期结果：点击问卷底部数据按钮能跳转问卷数据统计页面且问卷标题显示正确")

        try:
            time.sleep(2)
            questionnaireListPage.page.locator("//div[@class=\"questionnaire-item\"][2]/div[@class=\"questionnaire-bottom data\"]/div/div[2]").hover(timeout=3000, force=True)
            # 设为推荐
            questionnaireListPage.page.locator("//div[@class=\"questionnaire-item\"][2]/div[@class=\"questionnaire-bottom\"]//span[@class=\"recommend\"]").click()

            questionnaireListPage.operate_success_alert.wait_for()
            test_log.info('问卷设置推荐测试通过')
        except Exception as e:
            allure.attach(page.screenshot(), "用例失败截图", allure.attachment_type.PNG)
            test_log.error('问卷设置推荐测试不通过')
            test_log.debug("预期结果：点击设置推荐能设置成功")
            test_log.exception(e)
            pytest.fail("预期结果：点击设置推荐能设置成功并出现提示语")

        #eles=page.query_selector_all('.questionnaire-box div:nth-child(2)')
        #print("4.---->",eles, len(eles))
        #eles[-1].hover(timeout=3000,force=True)
        questionnaireListPage.title_search_input.fill("擎盾大学问卷（一）")
        questionnaireListPage.search_button.click()
        try:
            time.sleep(2)
            questionnaireListPage.page.locator("//div[@class=\"questionnaire-item\"][2]/div[@class=\"questionnaire-bottom data\"]/div/div[2]").hover(timeout=3000,force=True)
            questionnaireListPage.page.locator("//div[@class=\"questionnaire-item\"][2]/div[@class=\"questionnaire-bottom\"]//p[4]").click()
            questionnaireListPage.dialog_confirm_button.click()
            questionnaireListPage.operate_success_alert.wait_for()
            test_log.info('问卷删除测试通过')
        except Exception as e:
            allure.attach(page.screenshot(), "用例失败截图", allure.attachment_type.PNG)
            test_log.error('问卷删除测试不通过')
            test_log.debug('预期结果：问卷删除成功并出现提示语句')
            test_log.exception(e)
            pytest.fail("预期结果：问卷删除成功并出现提示语句")






















