# coding=utf-8
from appium import webdriver
from src.common.Common import singleton
from src.common import driver_configure
from src.common.driver_configure import VirtualDeviceParameter
from src.Utils.DevicesInfo import DevicesInfo


@singleton
class GetAppDriver:
    def __init__(self):
        device_info = DevicesInfo()
        if device_info.isOnlyOneDevice():
            # self.__driver = webdriver.Remote(driver_configure.desired_IP, DeviceParameter().get_desired_caps())
            self.__driver = webdriver.Remote(driver_configure.desired_IP, VirtualDeviceParameter().get_desired())
        else:
            self.__driver = webdriver.Remote(driver_configure.desired_IP, VirtualDeviceParameter().get_desired())

    def get_driver(self):
        return self.__driver
