# coding=utf-8

from src.common.GetAppDriver import GetAppDriver
from src.utils.DevicesInfo import DevicesInfo
import unittest
from src.utils.FindElement import find_element
from selenium.webdriver.common.by import By
from src.page.CalucPage import CalucPage
import time
from src.utils.Tools import Tools


# from public.logger import Logger


def test():
    device_info = DevicesInfo()
    device_info.get_serialno()
    device_info.print_device_info()
    driver = GetAppDriver().get_driver()
    print(driver.page_source)


class TestCal(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        driver = GetAppDriver()
        cls.driver = driver.get_driver()
        cls.page = CalucPage(cls.driver)
        print('+' * 30 + "start\n")

    def test_1(self):
        print("*" * 30 + "test_1\n")
        self.page.click_text("7")
        self.page.click_text("8")
        # self.driver.find_elements_by_android_uiautomator()
        time.sleep(1)
        # self.page.click_text("+")
        # self.page.click_text("DEL")
        time.sleep(1)
        self.page.click_text("9")
        # self.page.click_text("=")
        print("输出：== ")

    def test_2(self):
        pass
        # test()
        # print("TestCal  test_01login")

    @classmethod
    def tearDownClass(cls):
        print('=' * 30 + "end\n")
        ss = cls.driver.find_elements_by_class_name("android.widget.Button")
        for key in ss:
            print(key.get_attribute("text"))
        # print("=" * 30)
        # cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
