# coding:utf-8

'''
description:执行测试
'''
import unittest, time
from lib import HTMLTestRunner
from config.Globalparameter import test_case_path, report_name
from src.common import send_email
import os

# 构建测试集,包含src/test_case目录下的所有以test开头的.py文件
suite = unittest.defaultTestLoader.discover(start_dir=test_case_path, pattern='test*.py')


def create_report_path(path):
    path_name = os.path.dirname(path)
    if not os.path.exists(path_name):
        os.makedirs(path_name)


# 执行测试
if __name__ == "__main__":
    create_report_path(report_name)
    report = report_name + "Report.html"
    fb = open(report, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fb,
        title=u'startMaker 自动化测试报告',
        description=u'项目描述：生产环境'
    )
    runner.run(suite)
    fb.close()
    # 发送邮件
    time.sleep(10)  # 设置睡眠时间，等待测试报告生成完毕（这里被坑了＝＝）
    email = send_email.send_email()
    print("测试报告成功，准备发送邮件")
    # email.sendReport()
