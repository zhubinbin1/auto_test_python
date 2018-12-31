# coding:utf-8

import logging
import time
import socket
import os
import traceback
from config.GlobalParameter import is_open_log_system
from src.utils.FileUtil import log_path

rq = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))

setting = {
    'logpath': log_path,
    'filename': 'star_maker_' + rq + '.log'
}


def pull_app_log():
    import subprocess
    subprocess.check_output("adb logcat adb logcat -v time > " + log_path + "autoTest.txt", shell=True)


class Logger(object):
    '''https://blog.csdn.net/qq_42758861/article/details/82593777'''

    def __init__(self, logger):
        if not is_open_log_system:
            return
        try:
            self.path = setting['logpath']
            self.filename = setting['filename']
            self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(threadName)s - %(name)s - %(message)s')
            self.logger = logging.getLogger(logger)
            # logging.basicConfig()
            self.name = socket.gethostbyname(socket.gethostname())  # 获取主机名称和IP
            ###########################################################################
            # self.logger = logging.getLogger(self.name)
            self.logger.setLevel(logging.DEBUG)
            # self.logger.setLevel(logging.basicConfig(level=logging.NOTSET))
            # self.fileHandler = logging.FileHandler(self.path + self.filename)
            ###########################################################################
            self.fileHandler = logging.FileHandler(self.path + self.filename)
            self.fileHandlerName = self.fileHandler.get_name()
            self.fileHandler.setFormatter(self.formatter)
            self.logger.addHandler(self.fileHandler)
        except FileNotFoundError as e:
            print(e)
            print("===========开启日志系统请在全局参数中配置正确的日志存放路径=============")
        except Exception as e:
            print(e)
        ###############
        # self.fileHandler.setLevel(logging.DEBUG)
        # self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(threadName)s - %(name)s - %(message)s')
        # self.fileHandler.setFormatter(self.formatter)
        # self.logger.addHandler(self.fileHandler)

    def close(self):
        if (hasattr(self, "fileHandlerName")) and rq != self.fileHandlerName:
            if self.fileHandler is not None:
                self.logger.removeHandler(self.fileHandler)
                # self.logger.addHandler(self.fh)
                # self.logger.addHandler(fh)
                # self.logger.removeHandler(self.fileHandler)

    ##############################################################################################################

    def _fmtInfo(self, msg):
        if len(msg) == 0:
            msg = traceback.format_exc()
            return msg
        else:
            _tmp = [msg[0]]
            _tmp.append(traceback.format_exc())
            return '\n**********\n'.join(_tmp)

    ###################################################################################3###########################

    # def notset(self, msg):
    #     self.logger.notset(msg)

    def debug(self, msg):
        if hasattr(self, 'logger'):
            self.logger.debug(msg)

    def info(self, msg):
        if hasattr(self, 'logger'):
            self.logger.info(msg)

    def warning(self, msg):
        if hasattr(self, 'logger'):
            self.logger.warning(msg)

    def error(self, msg):
        if hasattr(self, 'logger'):
            self.logger.error(msg)

    def critical(self, msg):
        if hasattr(self, 'logger'):
            self.logger.critical(msg)

    # def close(self):
    #     self.logger.addHandler(self.fh)
    #     self.logger.removeHandler(self.fh)

# if __name__ == "__main__":
#     logger = Logger("info")
#     logger.info(msg='warning')
# pull_app_log()
