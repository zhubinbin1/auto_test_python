# coding:utf-8

'''
description:登录页
'''
from src.page import BasePage
from appium.webdriver.common import mobileby


class LoginData:
    btn_login_id = "id/btnLogin"


class LoginPage(BasePage.BasePage):
    # by = mobileby.MobileBy()

    def input_user(self, username):
        self.find_e_by_id(LoginData.btn_login_id).send_keys(username)

    def input_pws(self, password):
        pass

    def click_btn_login(self):
        pass
