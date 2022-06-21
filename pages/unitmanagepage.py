"""机构管理页"""
from playwright.async_api import Page


class UnitManage:
    def __init__(self,page:Page):
        self.page = page

        # 新增机构按钮
        self.new_unit_button = self.page.locator("//*[@id=\"app\"]/section/div/section/main/div[2]/div/button")
        # 操作列中的机构管理按钮
        self.edit_unit_button = self.page.locator("//*[@id=\"app\"]/section/div/section/main/div[2]/div/div/div[3]/table/tbody/tr/td[6]/div/button")
        # 机构列表中机构名称是“擎盾大学勿删”的机构对应的机构管理按钮
        self.qd_unit_edit_button = self.page.locator("//div[text()=\'擎盾大学勿删\']//ancestor::tr/td[6]//button")
        # 编辑机构对话框中的取消按钮
        self.dialog_cancel_button = self.page.locator("button:has-text(\"取 消\")")
        # 编辑机构对话框中的确定按钮
        self.dialog_confirm_button = self.page.locator("button:has-text(\"确 定\")")
        # 编辑机构对话框中机器人id选择输入区
        self.dialog_robot_id_dropdown_list_input = self.page.locator("//div[@class=\"el-dialog__body\"]/form[1]/div[4]//input[@class=\"el-select__input is-medium\"]")
        # 编辑机构对话框中机器人id选择项
        self.robot_id_option_20220621201 = self.page.locator("//div[@class=\"el-select-dropdown el-popper is-multiple\"]//ul[@class=\"el-scrollbar__view el-select-dropdown__list\"]/li[text()=\'20220621201\']")
        # 机器人id输入框中某个id值上右侧删除按钮
        self.robot_id_20220621201_close = self.page.locator("//span[@class=\"el-select__tags-text\"][text()=\'20220621201\']/following-sibling::i")
        # 机器人管理菜单
        self.equipment_manage_menu = self.page.locator("text=机器人管理")  # 机器人管理菜单
        # 保存更新成功提示语
        self.save_success_alert = self.page.locator("div[role=\"alert\"]:has-text(\"成功:修改机构并更新机构id到设备表成功\")")



    def assertVisible(self,element):
        visible = self.page.is_visible(element)
        assert visible
