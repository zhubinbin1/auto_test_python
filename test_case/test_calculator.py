# coding=utf-8

from src.common.GetAppDriver import GetAppDriver
from src.utils.DevicesInfo import DevicesInfo
import unittest
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
        # ctx = cls.driver.context
        # ctxs = cls.driver.contexts
        # print(ctx, ctxs)
        cls.foo = list(range(10))
        print('+' * 30)
        print("TestCal  setUpClass")

    def test_1calcLogin(self):
        test()

    def test_4calcLogin(self):
        test()
        # print("TestCal  test_01login")

    @classmethod
    def tearDownClass(cls):
        print("=" * 30)
        # cls.driver.quit()

    def test_2st(self):
        self.assertEqual(self.foo.pop(), 9)
        # print(self.foo)
        print("+" * 30, "test_2nd")

    def test_3nd(self):
        # self.assertEqual(self.foo.pop(), 18)
        print(self.foo, "test_3nd")
        # print(3/0)

    # def setUp(self):
    #     self.foo = list(range(10))
    #     print(self.foo)
    #     print("=" * 30)


if __name__ == '__main__':
    unittest.main()
