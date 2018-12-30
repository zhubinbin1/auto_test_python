# coding:utf-8
import os
import time
import string


def create_parent_path(path):
    path_name = os.path.dirname(path)
    if not os.path.exists(path_name):
        os.makedirs(path_name)


def create_current_path(path):
    if not os.path.exists(path):
        os.makedirs(path)


def img_file_path():
    img_file = os.path.abspath(os.path.dirname(project_path())) + "/report/images/"
    create_current_path(img_file)
    return img_file


# src 目录
def project_path():
    return os.path.abspath(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]), '.'))


def project_parent_path():
    return os.path.abspath(os.path.dirname(project_path()))


def report_file_path():
    report_path = project_parent_path() + "/report/"
    create_current_path(report_path)
    return report_path


def report_file_name():
    return report_file_path() + time.strftime('%Y%m%d%H%S', time.localtime())


def email_title_p():
    title = project_parent_path() + '/email_title'
    create_parent_path(title)
    return title


def email_user_p():
    e_user = project_parent_path() + '/email_user'
    create_parent_path(e_user)
    return e_user


def email_content_p():
    email_path = project_parent_path() + '/email_content'
    create_parent_path(email_path)
    return email_path


# src/test_case目录下
def test_case_path():
    test_case_path = project_parent_path()
    create_current_path(test_case_path)
    return test_case_path


def read_file_by_read(path_name):
    create_parent_path(path_name)
    with open(path_name, 'r') as f:
        return f.read()


def read_file_by_read_line(path_name):
    create_parent_path(path_name)
    with open(path_name, 'r') as f:
        return f.readline()


def read_file_by_read_lines(path_name):
    create_parent_path(path_name)
    with open(path_name, 'r') as f:
        return f.readlines()


# 读取发送者信息
def read_email_user():
    import re
    email_user_list = []
    tail = "@ushow.media"
    _at = '@'
    users = [user for user in read_file_by_read_lines(email_user_p()) if
             re.sub("\s", "", user) != ""]
    for user in users:
        out = re.sub("\s", "", user)
        if out.find(_at) <= 0:
            email_user_list.append(out + tail)
        else:
            email_user_list.append(out)
    # print(";".join(email_user_list))
    return email_user_list


read_email_user()
# read_file_by_read_lines(project_parent_path() + '/email_title')
# /Users/binbin/WORK/PY_WORKSPACE/start_maker_auto_test/src/.
# /Users/binbin/WORK/PY_WORKSPACE/start_maker_auto_test/src
# ('/Users/binbin/WORK/PY_WORKSPACE/start_maker_auto_test/src/utils', 'FileUtil.py')
# print(os.path.abspath(os.path.dirname(project_path())))

# print(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]), '.'))
# print(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]))
# print(os.path.split(os.path.realpath(__file__)))
