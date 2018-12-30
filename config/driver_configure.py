# coding=utf-8

from config import Globalparameter
from src.Utils.GetDevicesInfo import GetDevicesInfo

# IP/端口
desired_IP = "http://127.0.0.1:4723/wd/hub"


class DeviceParameter(object):
    # 配置信息
    platformVersion = ""
    PlatformName = "Android"
    AutomationName = "Appium"
    AutoGrantPermissions = True
    UnicodeKeyboard = True  # 是否支持unicode的键盘。如果需要输入中文，要设置为“true”
    ResetKeyboard = True  # 是否在测试结束后将键盘重轩为系统默认的输入法。
    NoReset = True  # true:不重新安装APP，false:重新安装app
    appActivity = "com.ushowmedia.starmaker.activity.SplashActivity"
    package_name = "com.starmakerinteractive.thevoice"  # GetDevicesInfo().GetPackages()#
    device_name = "emulator-5554"

    def get_desired_caps(self):
        try:
            self.desired_caps = {}
            # 调试使用
            self.desired_caps["platformVersion"] = "9"
            # self.desired_caps["device"] = "emulator-5554"
            self.desired_caps["deviceName"] = self.device_name  # 手机ID
            # 系统信息
            self.desired_caps["platformName"] = self.PlatformName
            # 待测包信息
            self.desired_caps["appPackage"] = self.package_name  # APK包名
            self.desired_caps["appActivity"] = self.appActivity  # 被测程序启动时的Activity
            # 其他
            self.desired_caps["unicodeKeyboard"] = self.UnicodeKeyboard
            self.desired_caps["resetKeyboard"] = self.ResetKeyboard
            self.desired_caps["automationName"] = self.AutomationName
            self.desired_caps["autoGrantPermissions"] = self.AutoGrantPermissions
            # self.desired_caps['app'] = 'apk路径'   # 指向.apk文件，如果设置appPackage和appActivity，那么这项会被忽略
            self.desired_caps['newCommandTimeout'] = '120'  # Appium服务器待appium客户端发送新消息的时间。默认为60秒
            # self.desired_caps['deviceName'] = '612QKBQD225A2'  # 手机ID
            # noReset决定是否清除app数据
            self.desired_caps["noReset"] = self.NoReset
        except:
            raise Exception

        return self.desired_caps

# # 真机设备
# class RealDeviceParameter(DeviceParameter):
#     @staticmethod
#     def get_desired_caps():
#         desired_caps = DeviceParameter.get_desired_caps()
#         desired_caps["appPackage"] = "com.android.calculator2"
#         desired_caps["appActivity"] = ".Calculator"
#         desired_caps["device"] = Globalparameter.device_name
#         desired_caps["deviceName"] = Globalparameter.device_name
#         desired_caps["platformVersion"] = Globalparameter.device_version
#         return desired_caps
#
#     @staticmethod
#     def get_device_parameter(app_package=DeviceParameter.package_name,
#                              app_activity=DeviceParameter.appActivity,
#                              device_name=Globalparameter.device_name, platform_version=Globalparameter.device_version
#                              ):
#         desired_caps = DeviceParameter.get_desired_caps()
#         desired_caps["appPackage"] = app_package
#         desired_caps["appActivity"] = app_activity
#         desired_caps["device"] = device_name
#         desired_caps["deviceName"] = Globalparameter.device_name
#         desired_caps["platformVersion"] = platform_version
#         return desired_caps
#
#
# # 虚拟设备
# class VirtualDeviceParameter(DeviceParameter):
#     @staticmethod
#     def get_desired_caps():
#         desired_caps = DeviceParameter.get_desired_caps()
#         desired_caps["appPackage"] = "com.android.calculator2"
#         desired_caps["appActivity"] = ".Calculator"
#         desired_caps["device"] = Globalparameter.device_name
#         desired_caps["deviceName"] = Globalparameter.device_name
#         desired_caps["platformVersion"] = Globalparameter.device_version
#         return desired_caps
#
#     @staticmethod
#     def set_device_parameter(app_package="com.android.calculator2", app_activity=".Calculator",
#                              device_name=Globalparameter.device_name, platform_version=Globalparameter.device_version
#                              ):
#         desired_caps = DeviceParameter.get_desired_caps()
#         desired_caps["appPackage"] = app_package
#         desired_caps["appActivity"] = app_activity
#         desired_caps["device"] = device_name
#         desired_caps["deviceName"] = Globalparameter.device_name
#         desired_caps["platformVersion"] = platform_version
#         return desired_caps
