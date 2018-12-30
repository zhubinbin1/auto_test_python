# coding=utf-8
import re
import subprocess
from src.Utils.Common import singleton

# ----------
# 设备信息
# ----------
NO = "no"
YES = "yes"


@singleton
class DevicesInfo(object):
    # sm所包含的测试包
    our_packages = ["com.starmakerinteractive.starmaker", "com.starmakerinteractive.thevoice",
                    "com.horadrim.android.sargam", "com.windforce.android.suaraku"]

    # 检查设备是否连接成功，如果成功返回True，否则返回False
    def __init__(self):
        # 检查设备连接状态
        try:
            # 获取设备列表信息，并将比特流类型转为str类型：decode，并用‘\r\n’拆分,
            self.deviceInfo = self.__adb_cmd("adb devices").split("\n")
            # 如果没有连接设备或设备读取失败，则第二个元素为空
            new = [x for x in self.deviceInfo if x != '']  # 去掉空''
            if self.deviceInfo[0] is not None:
                # self.device_name = self.deviceInfo[1]
                # print(self.device_name)
                self.hasDevice = True
            else:
                self.hasDevice = False
        # 捕获异常
        except Exception as e:
            self.hasDevice = False
            self.__not_connect()
            print("Device Connect Fail:", e)

    # 获取系统、设备信息 (权限被限制)
    def get_android_version(self):
        try:
            if self.hasDevice:
                # 获取系统设备信息，并将比特流类型转为str类型：decode
                # sysInfo = subprocess.check_output(str(os.system("adb shell cat /system/build.prop"))).decode()
                sys_info = self.__adb_cmd("adb shell cat /system/build.prop")
                # 获取Android版本号
                android_version = re.findall("version.release=(\d\.\d)", sys_info, re.S)[0]
                return android_version
            else:
                self.__not_connect()
                return NO
        # 捕获异常
        except Exception as e:
            print("Get Android Version:", e)

    # adb shell getprop ro.build.version.release
    def get_build_version(self):
        if self.hasDevice:
            try:
                build_version = self.__adb_cmd("adb shell getprop ro.build.version.release")
                # print(build_version)
                return build_version
            except Exception as e:
                print(e)

    def get_api_version(self):
        if self.hasDevice:
            api_version = self.__adb_cmd("adb shell getprop ro.build.version.sdk")
            return api_version

    # 获取设备名
    def get_device_name(self):
        try:
            if self.hasDevice:
                # 获取设备名
                # deviceInfo = subprocess.check_output(str(os.system("adb devices -l"))).decode("utf-8", "ignore")
                device_info = self.__adb_cmd("adb devices -l")
                device_name = re.findall(r"device product:(.*)\smodel", device_info, re.S)[0]
                return device_name
            else:
                self.__not_connect()
                return NO
        # 捕获异常
        except Exception as e:
            print("Get Device Name:", e)

    # 获取设备型号，用于报告中描述问题来源
    def get_device_model(self):
        try:
            if self.hasDevice:
                # 获取Android版本号
                device_info = self.__adb_cmd("adb devices -l")
                device_model = re.findall(r"model:(.*)\sdevice", device_info, re.S)[0]
                return device_model
            else:
                self.__not_connect()
                return NO
        # 捕获异常
        except Exception as e:
            print("Get Device:", e)

    def get_devices(self):
        new = [x for x in self.deviceInfo if x != '']  # 去掉空''
        # print("====%s", new)
        devices = []  # 获取设备名称
        for i in new:
            dev = i.split('\tdevice')
            if len(dev) >= 2:
                devices.append(dev[0])
        if not devices:
            self.__not_connect()
        else:
            # print("当前手机设备集合:%s" % str(devices))
            return devices

    # 如果设备大于1，取第一个设备序列号
    def get_first_device(self):
        return self.get_devices()[0]

    def get_all_sm_package(self):
        # sm:com.starmakerinteractive.starmaker
        # tvp:com.starmakerinteractive.thevoice
        # sa:com.horadrim.android.sargam
        # su:com.windforce.android.suaraku
        sm_packages = []
        try:
            if self.hasDevice:
                all_packages = self.__adb_cmd("adb shell pm list packages")
                list_packages = re.findall(r"package:(.*)", all_packages, re.S)[0]
                f = [c for c in self.our_packages if c in list_packages]
                if len(f):
                    sm_packages.append(f[0])  # AppPackage = "com.starmakerinteractive.starmaker"
            else:
                self.__not_connect()
            return sm_packages
        except Exception as e:
            print("GetPackages exception:", e)

    @staticmethod
    def __not_connect():
        print("........手机没连上.......")

    @staticmethod
    def __notice(notice):
        print(notice)

    @staticmethod
    def __adb_cmd(cmd):
        return subprocess.check_output(cmd, shell=True).decode("utf-8", "ignore")

    # 获取当前设备已安装包名
    def get_package(self):
        sm_pag = self.get_all_sm_package()
        if sm_pag:
            return str(self.get_all_sm_package()[0])
        else:
            return self.__notice("........请配置好app_path 安装应用包.......")

    def isOnlyOneDevice(self):
        if len(self.get_devices()) > 1:
            self.__notice("设备大于1，请仅连接一个设备")
            return False
        else:
            return True

    def get_serialno(self):
        return self.__adb_cmd("adb get-serialno")
        # print(serialno)

    @staticmethod
    def print_device_info():
        device_info = DevicesInfo()
        print("当前设备：", device_info.get_serialno() +
              "\n测试的包：", device_info.get_package() +
              "\n版本号码：", device_info.get_build_version())
