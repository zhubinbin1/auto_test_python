# coding:utf-8
import subprocess
from src.utils.DevicesInfo import DevicesInfo
import time, sys, os
import subprocess
import threading

sys.path.append(os.path.abspath('..'))
import re


def station_cmd(cmd):
    return subprocess.check_call(cmd, shell=True)


def start_single_server():
    print(station_cmd("appium -a 127.0.0.1 -p 4723"))


def kill_all_appium_server():
    print(station_cmd("killall node"))


'''appium 服务
https://testerhome.com/topics/6471
'''


class AppIumServer:
    # def __init__(self):
    #     self.deviceInfo = DevicesInfo()

    def __init__(self):
        # 多个设备信息的list
        # self.deviceInfo = DevicesInfo()
        self.machine_datas = {}  # 从文件读取出来的多个设备信息list
        self.log_path = os.path.abspath('../test_log/appium.log')

    def start_appium(self, ip, port, bp_port, udid, log_path):
        '启动appium服务'
        print(u'devices:{} start appium...'.format(udid))
        args1 = 'netstat -ano|findstr "{}"'.format(port)
        with subprocess.Popen(args1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) as p1:
            p1.wait()
            data = p1.stdout.read().decode('utf-8').strip('\r\n')
        port_list = re.findall(r":(\d{4,6}).*\s(\d{1,8})", data)  # 搜索端口和PID
        if port_list:
            # 停服务
            # 排除进程为0的并转为dict去重
            [port_list.remove(i) for i in port_list if i[1] == '0']
            port_pid = dict(port_list)
            for k in port_pid.keys():
                print(u'port:{0} is used,kill pid:{1}'.format(k, port_pid[k]))
                args3 = "taskkill -PID {} -F".format(port_pid[k])
                with subprocess.Popen(args3, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) as p3:
                    p3.wait()
                    print(p3.stdout.read().decode('gbk'))
                    print(p3.stderr.read().decode('gbk'))
        # 启服务
        args2 = "start /b appium -a {0} -p {1} -bp {2} -U {3} -g {4} --no-reset".format(ip, port, bp_port, udid,
                                                                                        log_path)
        with subprocess.Popen(args2, stdout=open(log_path, 'a'), stderr=subprocess.PIPE, shell=True) as p2:
            p2.wait()
            time.sleep(4)
            print(u'devices:{} appium server start  completed !'.format(udid))

    def multi_startappium(self):
        '批量启动appium服务'
        try:
            if self.machine_datas:
                for single_machine in self.machine_datas:
                    self.start_appium(single_machine['ip'], single_machine['port'], single_machine['bp_port'],
                                      single_machine['udid'], self.log_path)
            else:
                print(u'no machine info,please check')
        except Exception as e:
            print(e)
            raise e


'''多设备测试'''


class MultiDeviceTest:
    def __init__(self):
        self.deviceInfo = DevicesInfo()


'''多app测试'''


class MultiAppTest:
    def __init__(self):
        self.deviceInfo = DevicesInfo()
