# coding=utf-8
from appium import webdriver
from src.Utils.Common import singleton
from config import driver_configure
from config.driver_configure import DeviceParameter


@singleton
class GetAppDriver:
    def __init__(self):
        self.__driver = webdriver.Remote(driver_configure.desired_IP, DeviceParameter().get_desired_caps())

    def get_driver(self):
        return self.__driver
