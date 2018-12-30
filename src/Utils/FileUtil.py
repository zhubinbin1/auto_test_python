# coding:utf-8
import os
import time


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


# src/test_case目录下
def test_case_path():
    test_case_path = project_parent_path()
    create_current_path(test_case_path)
    return test_case_path

# /Users/binbin/WORK/PY_WORKSPACE/start_maker_auto_test/src/.
# /Users/binbin/WORK/PY_WORKSPACE/start_maker_auto_test/src
# ('/Users/binbin/WORK/PY_WORKSPACE/start_maker_auto_test/src/Utils', 'FileUtil.py')
# print(os.path.abspath(os.path.dirname(project_path())))

# print(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]), '.'))
# print(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]))
# print(os.path.split(os.path.realpath(__file__)))
