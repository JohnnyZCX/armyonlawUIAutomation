from playwright.async_api import Page
"""
用户管理>新增用户
"""

class AddUser:
    def __init__(self,page:Page):
        self.page = page
        self.save_button = self.page.locator("button:has-text(\"保存\")")
        self.account_input = self.page.locator("[placeholder=\"请输入小于20个字符的账号！\"]")
        self.nick_name_input = self.page.locator("[placeholder=\"请输入小于20个字的昵称！\"]")
        self.name_input = self.page.locator("[placeholder=\"请输入小于20个字的姓名！\"]")
        self.password_input = self.page.locator("[placeholder=\"请输入6-16位的字母数字下划线\"] >> nth=0")
        self.confirm_password_input = self.page.locator("[placeholder=\"请输入6-16位的字母数字下划线\"] >> nth=1")
        self.local_configure_checkbox = self.page.locator(".el-checkbox__inner >> nth=0")
        self.upload_photo_alert = self.page.locator("text=请上传上传人脸识别的头像！")
        self.upload_face_photo = self.page.locator("//*[@id=\"app\"]/section/div/section/main/div[2]/div/div[1]/form/div[1]/div[1]/div/input") #上传人脸头像的input标签
        self.upload_head_photo = self.page.locator("//*[@id=\"app\"]/section/div/section/main/div[2]/div/div[1]/form/div[1]/div[2]/div/input") #上传头像的input标签



    def assertContent(self,element,content_value):
        content = self.page.text_content(element)
        assert content == content_value

    def assertText(self,element,text_value):
        text = self.page.inner_text(element)
        assert text ==  text_value





