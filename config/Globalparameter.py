# coding:utf-8
import os
import time
# IP/端口
desired_IP = "http://127.0.0.1:4723/wd/hub"

# 配置信息

device_name = "emulator-5554"
device_version = "9"
app_package = "com.android.calculator2"
app_activity = ".Calculator"


project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]), '.'))
test_case_path = project_path+"\\src\\test_case"
report_path = project_path + "\\report\\"
report_name = report_path+time.strftime('%Y%m%d%H%S', time.localtime())
# 设置发送测试报告的公共邮箱、用户名和密码
smtp_sever = 'smtp.exmail.qq.com'  # 邮箱SMTP服务，各大运营商的smtp服务可以在网上找，然后可以在foxmail这些工具中验正
email_name = "888@x88.com"  # 发件人名称
email_password = "*888"  # 发件人登录密码
email_To = '888@qq.com;88@88.com'  # 收件人