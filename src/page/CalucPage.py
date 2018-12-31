# coding:utf-8
from src.page.BasePage import BasePage
from appium.webdriver.common.mobileby import MobileBy as by
from src.utils.FindElement import find_element

'''计算器模拟'''


class CalucPage(BasePage):
    def click_text(self, text):
        self.find_e_by_text(text).click()
