# coding:utf-8

'''
description:邮件发送最新的测试报告
'''
import os, smtplib, os.path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from src.utils.FileUtil import report_file_path
from src.utils.FileUtil import read_email_user, read_file_by_read, email_title_p

# 设置发送测试报告的公共邮箱、用户名和密码
# https://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=1001256
#  password :  hhntpsqaangwjaib
smtp_sever = 'smtp.qq.com'  # 邮箱SMTP服务，各大运营商的smtp服务可以在网上找，然后可以在foxmail这些工具中验正
email_name = "1415095526@qq.com"  # 发件人名称
email_password = "hhntpsqaangwjaib"  # 发件人登录密码
email_To = read_email_user()  # 收件人


class SendEmail:
    # 定义邮件内容
    @staticmethod
    def email_init(report, report_name):
        with open(report, 'rb')as f:
            mail_body = f.read()

        # 创建一个带附件的邮件实例
        msg = MIMEMultipart()
        # 以测试报告作为邮件正文
        msg.attach(MIMEText(mail_body, 'html', 'utf-8'))
        report_file = MIMEText(mail_body, 'html', 'utf-8')
        # 定义附件名称（附件的名称可以随便定义，你写的是什么邮件里面显示的就是什么）
        report_file["Content-Disposition"] = 'attachment;filename=' + report_name
        msg.attach(report_file)  # 添加附件
        msg['Subject'] = read_file_by_read(email_title_p()) + report_name  # 邮件标题
        msg['From'] = email_name  # 发件人
        msg['To'] = ";".join(email_To)  # 收件人列表
        try:
            server = smtplib.SMTP(smtp_sever)
            server.login(email_name, email_password)
            server.sendmail(msg['From'], email_To, msg.as_string())
            server.quit()
        except smtplib.SMTPException as e:
            print(e)
            print(u'邮件发送测试报告失败 at' + __file__)

    def send_report(self):
        # 找到最新的测试报告
        report_list = os.listdir(report_file_path())
        report_list.sort(
            key=lambda fn: os.path.getmtime(report_file_path() + fn) if not os.path.isdir(
                report_file_path() + fn) else 0)
        new_report = os.path.join(report_file_path(), report_list[-1])
        # 发送邮件
        self.email_init(new_report, report_list[-1])
