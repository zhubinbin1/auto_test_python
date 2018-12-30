# coding:utf-8

'''
description:执行测试
'''
import unittest, time
from src.common import HTMLTestRunner
from src.common.SendEmail import SendEmail
from src.utils.FileUtil import test_case_path, report_file_name
from config.GlobalParameter import pattern
from  src.utils.FileUtil import read_file_by_read,email_title_p,email_content_p,read_file_by_read_lines
import unicodedata
import os

# 构建测试集,包含src/test_case目录下的所有以test开头的.py文件
suite = unittest.defaultTestLoader.discover(start_dir=test_case_path(), pattern=pattern)

# 执行测试
if __name__ == "__main__":
    report = report_file_name() + "Report.html"
    fb = open(report, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fb,
        title=read_file_by_read(email_title_p()),
        description=read_file_by_read(email_content_p())
    )
    runner.run(suite)
    fb.close()
    print("测试报告成功，准备发送邮件")
    # 发送邮件
    # time.sleep(5)  # 设置睡眠时间，等待测试报告生成完毕
    # SendEmail().send_report()
