# coding=utf-8

from src.common.GetAppDriver import GetAppDriver
from src.utils.DevicesInfo import DevicesInfo
import unittest
from src.utils.FindElement import find_element
from selenium.webdriver.common.by import By
from src.page.CalucPage import CalucPage
import time


class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # driver = GetAppDriver()
        # cls.driver = driver.get_driver()
        print('+' * 30 + "start\n")

    @classmethod
    def tearDownClass(cls):
        print('=' * 30 + "end\n")
        # print("=" * 30)
        # cls.driver.quit()
