# coding=utf-8

from src.common.GetAppDriver import GetAppDriver
from src.Utils.DevicesInfo import DevicesInfo
import unittest
import time
from src.Utils.Tools import Tools


def test():
    device_info = DevicesInfo()
    device_info.get_serialno()
    # device_info.print_device_info()
    driver = GetAppDriver().get_driver()


test()


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
