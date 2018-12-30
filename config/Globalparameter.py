# coding:utf-8
import os
import time

# 配置信息

device_name = "emulator-5554"
device_version = "9"
app_package = "com.android.calculator2"
app_activity = ".Calculator"
app_path = "/Users/binbin/Desktop/thevoiceDebug-minApi17-x86.apk"
pattern = "test*.py"

# 设置发送测试报告的公共邮箱、用户名和密码
# https://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=1001256
#  password :  hhntpsqaangwjaib
smtp_sever = 'smtp.qq.com'  # 邮箱SMTP服务，各大运营商的smtp服务可以在网上找，然后可以在foxmail这些工具中验正
email_name = "1415095526@qq.com"  # 发件人名称
email_password = "hhntpsqaangwjaib"  # 发件人登录密码
email_To = "binbin.zhu@ushow.media; 1415095526@qq.com"  # 收件人
