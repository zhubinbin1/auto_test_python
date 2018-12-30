# coding:utf-8
__author__ = 'Helen'
'''
description:测试登录和退出功能
'''
import unittest

# from src.pages import index_page, myInfo_page, login_page, relative_page
from src.common import gesture_mainpulation
from src.common.GetAppDriver import GetAppDriver
from src.page import Login_page


class test_appium(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        driver = GetAppDriver()
        cls.driver = driver.get_driver()
        # cls.driver.quit()
        cls.GM = gesture_mainpulation.gesture_mainpulation()

    def test_01login(self):
        '''测试登录功能'''
        # 主页面
        # self.index_page = index_page.index_page(self.driver)
        # self.index_page.click_btnCancel()
        # self.GM.swipe_down(self.driver)
        # self.index_page.click_inXSTeach()
        # self.myInfo_page = myInfo_page.myInfo_page(self.driver)
        # self.myInfo_page.click_login_btn()
        # 登录页
        self.login_page = Login_page.login_page(self.driver)
        self.login_page.input_user("lihailing@xsteqach.com")
        self.login_page.input_Pws("123456")
        self.login_page.click_btnLogin()
        # self.assertEqual(u'签到', self.myInfo_page.getText_signHint())

    # def test_02loginOut(self):
    #     '''测试退出功能'''
    #     self.myInfo_page = myInfo_page.myInfo_page(self.driver)
    #     self.myInfo_page.click_relative()
    #     self.relative = relative_page.relative_page(self.driver)
    #     self.relative.click_tvLoginOut()
    #     self.relative.click_btnYes()
    #     self.assertEqual(u'点击登录', self.myInfo_page.getText_login())

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
