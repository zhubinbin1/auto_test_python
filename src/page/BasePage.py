# coding:utf-8


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from src.utils.FindElement import find_element
from appium.webdriver.common.mobileby import MobileBy as by
from appium.webdriver.common import mobileby

'''
description:UI页面公共类
'''


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.get_element = find_element()
        # by = mobileby.MobileBy()
        # baseId = (by.ID, "id/etUser")

    def find_e(self, *loc):
        # 重写find_element方法，显式等待
        try:
            WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            raise e

    def send_keys(self, value, *loc):
        try:
            self.find_e(*loc).clear()
            self.find_e(*loc).send_keys(value)
        except AttributeError as e:
            raise e

    def find_e_by_xpath(self, xpath):
        # btn = (by.XPATH, xpath)
        # self.find_element(*btn).click()
        try:
            return self.get_element.Xpa(xpath)
        except Exception as e:
            raise e

    def find_e_by_id(self, res_id):
        # btn = (by.ID, ids)
        # self.find_element(*btn)
        try:
            return self.get_element.ID(res_id)
        except Exception as e:
            raise e

    def find_e_by_text(self, text):
        try:
            '''注意字符转译'''
            # self.driver.find_element_by_xpath("//*[@text='+']").click()
            return self.find_e_by_xpath("//*[@text=\"" + text + "\"]")
        except Exception as e:
            raise e

    def find_e_by_cla(self, cla):
        try:
            # self.driver.find_element_by_android_uiautomator('new UiSelector().className(\"'+au+'\")')
            # self.driver.find_element_by_xpath("//*[@class='android.widget.EditText']").click()
            return self.get_element.Cla(cla)
        except Exception as e:
            raise e

    def find_e_by_android_uiautomator(self, AU):
        try:
            return self.get_element.AU(AU)
        except Exception as e:
            raise e

    def find_e_text_by_au(self, au):
        try:
            '''注意字符转译'''
            # new UiSelector().resourceIdMatches(".+id/title")  UiSelector方法很多，可以网上找
            # self.driver.find_element_by_android_uiautomator('new UiSelector().className(\"'+au+'\")')
            # return self.driver.find_element_by_android_uiautomator('new UiSelector().text("+")')
            au_f = 'new UiSelector().text(\"' + au + '\")'
            return self.get_element.AU(au_f)
        except Exception as e:
            raise e
