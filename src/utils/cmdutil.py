# coding:utf-8
import subprocess
import io
import os


def subprocess_cmd(cmd):
    # subprocess.check_output(cmd, shell=True)
    subprocess.Popen(cmd, shell=True)
    # os.popen()


'''启动ui mator'''


def uiautomatorviewer():
    print(subprocess.check_output("uiautomatorviewer", shell=True))


# uiautomatorviewer()
