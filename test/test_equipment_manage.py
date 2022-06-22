#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/21 16:15
# @Author : 郑春兴
# @Email : zhengchunxing@aegis-data.cn
# @File : test_equipment_manage.py
# @Project : PlaywrightProject
import time

import allure
import pytest
from playwright.async_api import Page

from common.handle_logging import test_log
from pages.equipmentmanage import EquipmentManage
from pages.unitmanagepage import UnitManage

@allure.feature("机器人管理页面")
class TestEquipmentManage:
    @allure.story("在机构管理列表中给指定机构添加指定的机器人然后机器人列表中查询是否存在被添加的机器人")
    @allure.description('''
                1.使用超级管理员账号登录成功，后打开全局配置下拉菜单，查看机构管理菜单是否可见
                2.点击机构管理菜单打开机构管理页
                2.在机构管理列表中找到单位名称是“擎盾大学勿删”的记录并点击对应的机构管理按钮打开编辑机构对话框
                3.在机器人id选择框中添加指定的机器人id，后点击确定按钮，保存添加机器人成功
                4.在左侧导航栏中点击机器人管理菜单打开“设备管理”页面
                5.输入机器人编号和机器人名称后点击【查询】按钮
                6.在机器人列表中校验查询出的结果的机器人编号和机器人名称值是否正确
                ''')
    def test_add_equipment_for_unit(self,page,superUserAmdin_login):
        userManagementPage = superUserAmdin_login
        userManagementPage.global_configuration.click()
        userManagementPage.unit_manage_menu.click()
        unitManagePage = UnitManage(page)
        unitManagePage.qd_unit_edit_button.click()
        time.sleep(1)
        try:
            unitManagePage.dialog_robot_id_dropdown_list_input.click()
            unitManagePage.robot_id_option_20220621201.click()
            unitManagePage.dialog_confirm_button.click()
            time.sleep(1.5)
            unitManagePage.save_success_alert.wait_for()
            unitManagePage.equipment_manage_menu.click()
            time.sleep(2)
            equipmentManagePage = EquipmentManage(page)
            equipmentManagePage.robot_number_input.wait_for()
            equipmentManagePage.robot_number_input.fill("20220621201")
            equipmentManagePage.robot_name_input.fill("修改已有的机器人")
            equipmentManagePage.search_button.click()
            time.sleep(2)
            equipmentManagePage.assertText("//table[@class=\"el-table__body\"]//tr[1]/td[2]/div","20220621201")
            equipmentManagePage.assertText("//table[@class=\"el-table__body\"]//tr[1]/td[3]/div","修改已有的机器人")
            test_log.info("机构管理添加机器人测试通过")
        except Exception as e:
            allure.attach(page.screenshot(), "用例失败截图", allure.attachment_type.PNG)
            test_log.error('机构管理添加机器人测试不通过')
            test_log.debug('预期结果：编辑机构弹窗添加机器人后查询该机器人测试通过')
            test_log.exception(e)
            pytest.fail("预期结果：编辑机构弹窗添加机器人后查询该机器人测试通过")

    @allure.story("在机构管理列表中给指定机构删除已添加的机器人然后机器人列表中查询是否存在已删除的机器人")
    @allure.description('''
                1.使用超级管理员账号登录成功，后打开全局配置下拉菜单，查看机构管理菜单是否可见
                2.点击机构管理菜单打开机构管理页
                2.在机构管理列表中找到单位名称是“擎盾大学勿删”的记录并点击对应的机构管理按钮打开编辑机构对话框
                3.在机器人id列表中删除指定的机器人id，后点击确定按钮，保存删除机器人成功
                4.在左侧导航栏中点击机器人管理菜单打开“设备管理”页面
                5.输入机器人编号和机器人名称后点击【查询】按钮
                6.在机器人列表中校验是否查询无数据
                ''')
    def test_delete_equipment_for_unit(self,page,superUserAmdin_login):
        userManagementPage = superUserAmdin_login
        userManagementPage.global_configuration.click()
        userManagementPage.unit_manage_menu.click()
        unitManagePage = UnitManage(page)
        unitManagePage.qd_unit_edit_button.click()
        time.sleep(2)
        try:
            unitManagePage.robot_id_20220621201_close.click()
            unitManagePage.dialog_confirm_button.click()
            time.sleep(1.5)
            unitManagePage.save_success_alert.wait_for()
            unitManagePage.equipment_manage_menu.click()
            equipmentManagePage = EquipmentManage(page)
            equipmentManagePage.robot_number_input.wait_for()
            equipmentManagePage.robot_number_input.fill("20220621201")
            equipmentManagePage.robot_name_input.fill("修改已有的机器人")
            equipmentManagePage.search_button.click()
            equipmentManagePage.assertText("//span[@class=\"el-table__empty-text\"]","暂无数据")
            test_log.info("机构管理删除机器人测试通过")
        except Exception as e:
            allure.attach(page.screenshot(), "用例失败截图", allure.attachment_type.PNG)
            test_log.error('机构管理删除机器人测试不通过')
            test_log.debug('预期结果：编辑机构弹窗删除机器人后查询该机器人测试通过')
            test_log.exception(e)
            pytest.fail("预期结果：编辑机构弹窗删除机器人后查询该机器人测试通过")









