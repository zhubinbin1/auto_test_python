# coding=utf-8

from src.common.GetAppDriver import GetAppDriver
from src.Utils.DevicesInfo import DevicesInfo
import unittest
import time
from src.Utils.Tools import Tools


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
        print("TestCal  setUpClass")

    def test_calcLogin(self):
        test()
        print("TestCal  test_01login")

    @classmethod
    def tearDownClass(cls):
        print("TestCal  tearDownClass")
        cls.driver.quit()

#
#
# class test_calculator(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = GetAppDriver().get_driver()
#         # test()
#         time.sleep(5)
#         print("CalTest =setUpClass")
#
#     def setUp(self):
#         time.sleep(2)
#         print("CalTest =setUp")
#
#     def tearDown(self):
#         time.sleep(2)
#         print("CalTest =tearDown")
#         # 截图
#         # Tools().get_images()
#
#     @classmethod
#     def tearDownClass(cls):
#         time.sleep(2)
#         cls.driver.quit()
#         print("CalTest =tearDownClass")
#         pass
#

# if __name__ == '__main__':
#     unittest.main()

# webdriver.Remote(DeviceParameter.desired_IP, VirtualDeviceParameter().get_desired_caps())
