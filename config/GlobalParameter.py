# coding:utf-8
import os
import time
from src.utils.FileUtil import get_sdk_app_file

# 配置信息


'''正则匹配，正常是在test_case目录下以test为开始的py文件都是进行测试的，如果单独测试，可以修改此pattern'''
pattern = "test_cal*.py"  # "test*.py"

'''
是否发送邮件-如果发送邮件，请在email_content,email_title,email_user三个文件中写内容，
分别代表内容，题目，发送的用户（发送的用户每行一个，如果是@ushow.media结尾可以不加@ushow.media）
'''
is_send_email = False

'''是否启动日志系统,如果启动日志，需要配置log_path'''
is_open_log_system = True
