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
    img_file = "../report/images/"
    create_current_path(img_file)
    return img_file


def project_path():
    return os.path.abspath(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]), '.'))


def report_file_path():
    report_path = project_path() + "/report/"
    create_current_path(report_path)
    return report_path


def report_file_name():
    return report_file_path() + time.strftime('%Y%m%d%H%S', time.localtime())


def test_case_path():
    test_case_path = project_path() + "/src/test_case"
    create_current_path(test_case_path)
    return test_case_path
