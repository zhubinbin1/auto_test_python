# coding:utf-8
from src.page.BasePage import BasePage
from appium.webdriver.common import mobileby

'''计算器模拟'''


class CalucPage(BasePage):
    by = mobileby.MobileBy
    btnClick = (by.ID, "com.xsteach.appedu:id/btnLogin")

    def click_btn(self):
        self.find_element(*self.btnClick).click()
