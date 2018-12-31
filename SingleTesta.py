# coding:utf-8
# li = ["1", "2", "4", "6"]
# print(li[1])
import calendar
import subprocess
import os
import time
from src.utils.Tools import Tools

# ca = calendar.month(2019, 1)
# p = subprocess.check_output("adb devices")
Tools.get_element_error_images()
# f = subprocess.call(['adb','devices'])
# print(f)
# f2 = os.popen(r"adb devices","r")
#
# print(f2)
# sub = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
# res = subprocess.call('ls')
# res = subprocess.check_output('adb devices',stderr = subprocess.STDOUT,shell = True)
# res2 = subprocess.check_output("adb devices",shell=True).decode("utf-8", "ignore").split("\n")
# print(res)
# print(res2[1])

import re

# string = "a  a  b  c  d  e  f  r"
# regex = re.compile("((\w+)\s+\w+)")
# print(regex.findall(string))
#
# regex1 = re.compile("(\w+)\s+\w+")
# print(regex1.findall(string))
# regex2 = re.compile("\w+\s+\w+")
# print(regex2.findall(string))
# deviceInfo = subprocess.check_output("adb devices -l",shell=True).decode("utf-8", "ignore")
# deviceName = re.findall(r"device product:(.*)\smodel", deviceInfo, re.S)[0]
# deviceModel = re.findall(r"model:(.*)\sdevice", deviceInfo, re.S)[0]
# print(deviceName)
# print(deviceModel)
#
# all_packages = subprocess.check_output("adb shell pm list packages",shell=True).decode("utf-8", "ignore")
# list_packages = re.findall(r"package:(.*)", all_packages, re.S)[0]
# our_packages = ["com.starmakerinteractive.starmaker", "com.starmakerinteractive.thevoice",
#                                 "com.horadrim.android.sargam", "com.windforce.android.suaraku"]
# f = [c for c in our_packages if c in list_packages]
# if len(f):
#     print(f)


# b'List of devices attached\nemulator-5554\tdevice\n\n'
# ['List of devices attached\nemulator-5554\tdevice\n\n']

# shuchu = f.read()
# f.close()
# s = shuchu.split("\n")
# print("====%s",s)
# new = [x for x in s if x != '']  # 去掉空''
# print(new)
# devices = []  # 获取设备名称
# for i in new:
#     dev = i.split('\tdevice')
#     if len(dev)>=2:
#         devices.append(dev[0])
# if not devices:
#     print("手机没连上")
# else:
#     print("当前手机设备:%s"%str(devices))
#
#
# deviceInfo = os.popen(r"adb devices","r").read().split("\r\n")
# print("==w==%s",deviceInfo[0])


# sub = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
# sub.wait()
# subprocess.check_output(str(os.system("adb shell cat /system/build.prop"))).decode()
# subprocess.check_output("adb devices").decode("utf-8", "ignore")
# x = subprocess.check_output(("echo", "Headsadsorld!"))
# dev = subprocess.Popen('adb shell',stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
# print(dev)
# print(ca)
# a = time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
# print(a)
# b = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# print(b)
# print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))
import os
import sys
import re
import shutil
import glob
import random
import math
from datetime import date

from urllib.request import urlopen

# cwd = os.getcwd()
# print(cwd)
# os.system("mkdir aa")
# help(os)
# shutil.copy()
# glob.glob("*")
# print(sys.argv)
# for line in urlopen('http://www.baidu.com'):
#     line = line.decode('utf-8')
#     if 'html' in line or 'body' in line:
#         print(line)
# print(line)
# now = date.today()
# print(now)
# now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
# print(now)

# import random
#
# i = 1
# a = random.randint(0, 100)
# b = int(input('请输入0-100中的一个数字\n然后查看是否与电脑一样：'))
# while a != b:
#     if a > b:
#         print('你第%d输入的数字小于电脑随机数字' % i)
#         b = int(input('请再次输入数字:'))
#     else:
#         print('你第%d输入的数字大于电脑随机数字' % i)
#         b = int(input('请再次输入数字:'))
#     i += 1
# else:
#     print('恭喜你，你第%d次输入的数字与电脑的随机数字%d一样' % (i, b))
