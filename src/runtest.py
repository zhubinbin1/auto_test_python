# coding:utf-8

'''
description:执行测试
'''
import unittest, time
from src.common import HTMLTestRunner
from src.common import SendEmail
from src.Utils.FileUtil import test_case_path, report_file_name
from config.GlobalParameter import pattern

import os

# 构建测试集,包含src/test_case目录下的所有以test开头的.py文件
suite = unittest.defaultTestLoader.discover(start_dir=test_case_path(), pattern=pattern)

# 执行测试
if __name__ == "__main__":
    report = report_file_name() + "Report.html"
    fb = open(report, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fb,
        title=u'startMaker 自动化测试报告',
        description=u'项目描述：python脚本自动化 生成测试报告--by zhubin'
    )
    runner.run(suite)
    fb.close()
    print("测试报告成功，准备发送邮件")
    # 发送邮件
    # time.sleep(10)  # 设置睡眠时间，等待测试报告生成完毕
    # email = send_email.send_email()

    # email.sendReport()
