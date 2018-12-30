# coding:utf-8

'''
description:登录页
'''
from src.page import BasePage
from appium.webdriver.common import mobileby


class LoginPage(BasePage.BasePage):
    by = mobileby.MobileBy()
    # etUser_loc = (by.ID, "com.xsteach.appedu:id/etUser")
    # etPws_loc = (by.ID, "com.xsteach.appedu:id/etPwd")
    # btnLogin_loc = (by.ID, "com.xsteach.appedu:id/btnLogin")

    def input_user(self, username):
        pass
        # self.send_keys(username, *self.etUser_loc)

    def input_pws(self, password):
        pass
        # self.send_keys(password, *self.etPws_loc)

    def click_btn_login(self):
        pass
        self.find_element(*self.btnLogin_loc).click()





   # @classmethod
   #  def setUpClass(cls):
   #      driver = GetAppDriver()
   #      cls.driver = driver.get_driver()
   #      # ctx = cls.driver.context
   #      # ctxs = cls.driver.contexts
   #      # print(ctx, ctxs)
   #      cls.foo = list(range(10))
   #      print('+' * 30)
   #      print("TestCal  setUpClass")
   #
   #  def test_1calcLogin(self):
   #      test()
   #
   #  def test_4calcLogin(self):
   #      test()
   #      # print("TestCal  test_01login")
   #
   #  @classmethod
   #  def tearDownClass(cls):
   #      print("=" * 30)
   #      # cls.driver.quit()
   #
   #  def test_2st(self):
   #      self.assertEqual(self.foo.pop(), 9)
   #      # print(self.foo)
   #      print("+" * 30, "test_2nd")
   #
   #  def test_3nd(self):
   #      # self.assertEqual(self.foo.pop(), 18)
   #      print(self.foo, "test_3nd")
   #      # print(3/0)

