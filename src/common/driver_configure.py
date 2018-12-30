# coding=utf-8

from config import Globalparameter
from src.Utils.DevicesInfo import DevicesInfo

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
    waitActivity = "com.ushowmedia.starmaker.activity.MainActivity"
    package_name = "com.starmakerinteractive.thevoice"  # GetDevicesInfo().GetPackages()#

    def get_desired_caps(self):
        try:
            self.desired_caps = {}
            device_info = DevicesInfo()
            # 调试使用
            self.desired_caps["platformVersion"] = device_info.get_build_version()
            self.desired_caps["device"] = device_info.get_serialno()  # emulator-5558
            self.desired_caps["deviceName"] = device_info.get_serialno()  # emulator-5558
            # 系统信息
            self.desired_caps["platformName"] = self.PlatformName  # android
            # 待测包信息
            self.desired_caps["appPackage"] = device_info.get_package()  # self.package_name  # APK包名
            self.desired_caps["appActivity"] = self.appActivity  # 被测程序启动时的Activity
            self.desired_caps["appWaitActivity"] = self.waitActivity
            # 其他
            self.desired_caps["unicodeKeyboard"] = self.UnicodeKeyboard
            self.desired_caps["resetKeyboard"] = self.ResetKeyboard
            self.desired_caps["automationName"] = self.AutomationName
            self.desired_caps["autoGrantPermissions"] = self.AutoGrantPermissions
            self.desired_caps['app'] = Globalparameter.app_path  # 指向.apk文件，如果设置appPackage和appActivity，那么这项会被忽略
            self.desired_caps['newCommandTimeout'] = '120'  # Appium服务器待appium客户端发送新消息的时间。默认为60秒
            # noReset决定是否清除app数据
            self.desired_caps["noReset"] = self.NoReset
        except Exception as e:
            print(e)
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
class VirtualDeviceParameter(DeviceParameter):
    @staticmethod
    def get_desired():
        desired_caps = {}
        # 调试使用
        desired_caps["platformVersion"] = "9"
        # self.desired_caps["device"] = "emulator-5554"
        desired_caps["deviceName"] = 9  # 手机ID
        # 系统信息
        desired_caps["platformName"] = DeviceParameter.PlatformName  # android
        # 其他
        desired_caps["unicodeKeyboard"] = DeviceParameter.UnicodeKeyboard
        desired_caps["resetKeyboard"] = DeviceParameter.ResetKeyboard
        desired_caps["automationName"] = DeviceParameter.AutomationName
        desired_caps["autoGrantPermissions"] = DeviceParameter.AutoGrantPermissions
        # desired_caps['app'] = Globalparameter.app_path  # 指向.apk文件，如果设置appPackage和appActivity，那么这项会被忽略
        desired_caps['newCommandTimeout'] = '120'  # Appium服务器待appium客户端发送新消息的时间。默认为60秒
        # noReset决定是否清除app数据
        desired_caps["noReset"] = DeviceParameter.NoReset
        desired_caps["appPackage"] = "com.android.calculator2"
        # DeviceParameter.package_name  # "com.android.calculator2"
        desired_caps["appActivity"] = ".Calculator"  # DeviceParameter.appActivity  # ".Calculator"
        desired_caps["device"] = Globalparameter.device_name
        desired_caps["deviceName"] = Globalparameter.device_name
        desired_caps["platformVersion"] = Globalparameter.device_version
        return desired_caps
