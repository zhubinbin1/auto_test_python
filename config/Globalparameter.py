# coding:utf-8
import os
import time

# 配置信息

device_name = "emulator-5554"
device_version = "9"
app_package = "com.android.calculator2"
app_activity = ".Calculator"
app_path = "/Users/binbin/Desktop/thevoiceDebug-minApi17-x86.apk"

project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]), '.'))
test_case_path = project_path + "/src/test_case"
report_path = project_path + "/report/"
report_name = report_path + time.strftime('%Y%m%d%H%S', time.localtime())
# 设置发送测试报告的公共邮箱、用户名和密码
smtp_sever = 'smtp.exmail.qq.com'  # 邮箱SMTP服务，各大运营商的smtp服务可以在网上找，然后可以在foxmail这些工具中验正
email_name = "1415095526@qq.com"  # 发件人名称
email_password = "zhubinbin123"  # 发件人登录密码
email_To = '1415095526@qq.com'  # 收件人
