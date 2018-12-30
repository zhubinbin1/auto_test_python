# coding:utf-8
__author__ = 'Helen'
'''
description:登录页
'''
from src.page import BasePage
from appium.webdriver.common import mobileby


class LoginPage(BasePage.BasePage):
    by = mobileby.MobileBy()
    etUser_loc = (by.ID, "com.xsteach.appedu:id/etUser")
    etPws_loc = (by.ID, "com.xsteach.appedu:id/etPwd")
    btnLogin_loc = (by.ID, "com.xsteach.appedu:id/btnLogin")

    def input_user(self, username):
        pass
        # self.send_keys(username, *self.etUser_loc)

    def input_pws(self, password):
        pass
        # self.send_keys(password, *self.etPws_loc)

    def click_btn_login(self):
        pass
        # self.find_element(*self.btnLogin_loc).click()
