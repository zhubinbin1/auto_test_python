# coding=utf-8

from appium import webdriver
from config import driver_configure
from src.common.GetAppDriver import GetAppDriver
from src.Utils.GetDevicesInfo import GetDevicesInfo
import unittest
import time
from src.Utils.Tools import Tools

# GetAppDriver().get_driver()
print(GetDevicesInfo().GetPackages())


class CalTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = GetAppDriver().get_driver()
        time.sleep(5)

    def setUp(self):
        time.sleep(2)

    def tearDown(self):
        # 截图
        Tools().get_images()

    @classmethod
    def tearDownClass(cls):
        pass

# webdriver.Remote(DeviceParameter.desired_IP, VirtualDeviceParameter().get_desired_caps())
