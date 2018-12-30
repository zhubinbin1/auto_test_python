# coding=utf-8
# ----------
# 通用工具封装
# ----------
import re
import time
import datetime
from src.common.GetAppDriver import GetAppDriver
from src.utils.FileUtil import img_file_path


# ----------
# 常用工具
# ----------
class Tools:
    # 截取图片,并保存在images文件夹
    _PNG = '.png'

    @staticmethod
    def get_current_time():  # 获取当前时间
        return time.strftime('%Y%m%d_%H.%M.%S', time.localtime(time.time()))

    @staticmethod
    def get_images():
        driver = GetAppDriver().driver
        # 定义路径
        # (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y%m%d_%H.%M.%S')
        nowtime = Tools.get_current_time()
        # 定义图片名称
        img_name = nowtime + Tools._PNG
        # 截图
        driver.get_screenshot_as_file('%s%s' % (img_file_path, img_name))
        print('screenshot:', nowtime, Tools._PNG)

    # 元素未找到截图,并保存在images文件夹
    @staticmethod
    def get_element_error_images():
        driver = GetAppDriver().driver
        # 定义路径
        png_file = "../TestReport/images/"
        # 获取当前时间，且days-1，以展示在报告截图最下方
        nowtime = Tools.get_current_time()
        # 定义图片名称
        img_name = nowtime + Tools._PNG
        # 截图
        driver.get_screenshot_as_file('%s%s' % (png_file, img_name))
        print('screenshot:', nowtime, Tools._PNG)

    # 动态元素转换
    @staticmethod
    def FindSource(Source_ID):
        global ReadMappingTable
        try:
            ReadMappingTable = open("../bin/resource_mapping.txt", "r")
            Result_ID = re.findall("R.id." + "(.*)""'", re.findall(
                "R.id." + Source_ID + " -> " + "(.*)", ReadMappingTable.read()).__str__())[0]
            return Result_ID
        except:
            return Source_ID
        finally:
            if ReadMappingTable:
                ReadMappingTable.close()


# ----------
# 页面元素校验
# ----------
# 提取该页面同一类型下的所有元素text
class Page_Element_Verification(object):
    def __init__(self):
        self.driver = GetAppDriver().driver
        time.sleep(5)

    # 适用进入页面时校验页面元素加载正确，且这些元素具备同ID/Class或其他
    def PEV_IDS(self, IDS, TextList):
        Pe = self.driver.find_elements_by_id(IDS)
        ExpectText = TextList
        TextList = []
        for index in range(len(Pe)):
            TextList.append(Pe[index].text)
            time.sleep(2)
        if ExpectText == TextList:
            return True
        else:
            LessThanExpected = [i for i in ExpectText if i not in TextList]
            MoreThanExpected = [i for i in TextList if i not in ExpectText]
            # 比预期少了
            if LessThanExpected:
                return False, LessThanExpected
            # 比预期多了
            elif MoreThanExpected:
                return False, MoreThanExpected
            # 排序不正确或未取到
            else:
                print("预期结果:", ExpectText)
                print("实际结果:", TextList)
                return False

    def PEV_ClaS(self, ClaS, TextList):
        Pe = self.driver.find_elements_by_class_name(ClaS)
        ExpectText = TextList
        TextList = []
        for index in range(len(Pe)):
            TextList.append(Pe[index].text)
            time.sleep(2)
        if ExpectText == TextList:
            return True
        else:
            LessThanExpected = [i for i in ExpectText if i not in TextList]
            MoreThanExpected = [i for i in TextList if i not in ExpectText]
            # 比预期少了
            if LessThanExpected:
                return False, LessThanExpected
            # 比预期多了
            elif MoreThanExpected:
                return False, MoreThanExpected
            # 排序不正确或未取到
            else:
                print("预期结果:", ExpectText)
                print("实际结果:", TextList)
                return False


# ----------
# 屏幕处理工具
# ----------
class Screen(object):
    def __init__(self):
        self.driver = GetAppDriver().driver
        # 获取屏幕的size
        self.size = self.driver.get_window_size()
        print(self.size)
        # 获取屏幕宽度 width
        self.width = self.size['width']
        # 获取屏幕高度 height
        self.height = self.size['height']

    # 计算百分比(传参：本机屏幕上的x，y轴坐标；返回：该坐标的百分比)
    def CalculatedPercentage(self, x1N, y1N):
        x1P = x1N / self.width
        print("x1N:", x1N, "y1N:", y1N)
        y1P = y1N / self.height
        print("x1P:", x1P, "y1P:", y1P)
        return x1P, y1P

    # 滑动打开通知栏
    def SwipeOpen_NoticeBoard(self):
        # 执行滑屏操作,向下滑动(下拉),打开通知栏
        x1 = self.width * 0.5
        y1 = self.height * 0.01
        y2 = self.height * 0.5
        time.sleep(2)
        self.driver.swipe(x1, y1, x1, y2)

    # 滑动收起通知栏
    def SwipeClose_NoticeBoard(self):
        # 执行滑屏操作,向上滑动(收起)，收起通知栏
        x1 = self.width * 0.5
        y1 = self.height * 0.5
        y2 = self.height * 0.01
        time.sleep(2)
        self.driver.swipe(x1, y1, x1, y2)

    # 向上滑动1/2屏
    def SWipeUp_Half(self):
        # 执行滑屏操作,向上滑动1/2屏
        x = self.width * 0.5
        y1 = self.height * 0.6
        y2 = self.height * 0.1
        time.sleep(2)
        self.driver.swipe(x, y1, x, y2)

    # 向上滑动1/4屏
    def SWipeUp_Quarter(self):
        # 执行滑屏操作,向上滑动1/4屏
        x = self.width * 0.5
        y1 = self.height * 0.75
        y2 = self.height * 0.5
        time.sleep(2)
        self.driver.swipe(x, y1, x, y2)

    # 根据传值百分比，自定义滑动操作(传参：百分比)
    def DIYSwipe_Percentage(self, x1P, y1P, x2P, y2P, t):
        # 执行滑屏操作,接收参数(四个百分比+时间),运算后滑动
        x1 = self.width * x1P
        y1 = self.height * y1P
        x2 = self.width * x2P
        y2 = self.height * y2P
        time.sleep(2)
        self.driver.swipe(x1, y1, x2, y2, t)

    # 根据屏幕百分比，自定义点击操作(传参：百分比)
    def AccurateClicks_Percentage(self, x1P, y1P, t):
        # 执行滑屏操作,接收参数(两个百分比+时间),运算后滑动
        # 时间:点击(500)/长按3s(3000)
        x1 = self.width * x1P
        y1 = self.height * y1P
        time.sleep(2)
        self.driver.tap([(x1, y1)], t)

    # 多点触控(最多支持五点触控)
    def Multi_Touch_Percentage(self, x1P, y1P, x2P, y2P, x3P, y3P, x4P, y4P, x5P, y5P, t):
        # 执行滑屏操作,接收参数(最多十个百分比+时间),运算后滑动
        # 时间:点击(500)/长按3s(3000)
        # 第一个点
        x1 = self.width * x1P
        y1 = self.height * y1P
        # 第二个点
        x2 = self.width * x2P
        y2 = self.height * y2P
        # 第三个点
        x3 = self.width * x3P
        y3 = self.height * y3P
        # 第四个点
        x4 = self.width * x4P
        y4 = self.height * y4P
        # 第五个点
        x5 = self.width * x5P
        y5 = self.height * y5P
        time.sleep(2)
        self.driver.tap([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], t)


# 区域滑动
class RegionalSliding(object):
    def __init__(self, elements):
        self.driver = GetAppDriver().driver
        ele = self.driver.find_element_by_id(elements)
        # 获取当前元素大小
        size = ele.size
        self.height = size.get("height")
        self.width = size.get("width")
        print(size)
        # 获取当前元素起始位置
        location = ele.location
        self.x = location.get("x")
        self.y = location.get("y")
        print(location)

    # 区域滑动——横向
    def Transverse(self):
        # 运算获得滑动前后位置
        height = self.height / 2
        width = self.width / 4
        x1 = int(self.x + width)
        y = int(self.y + height)
        x2 = int(self.x + width * 3)
        time.sleep(2)
        print(x1, y)
        print(x2, y)
        self.driver.swipe(x2, y, x1, y, 500)

    # 区域滑动——纵向
    def Longitudinal(self):
        # 运算获得滑动前后位置
        height = self.height / 4
        width = self.width / 2
        x = int(self.x + width)
        y1 = int(self.y + height)
        y2 = int(self.y + height * 3)
        time.sleep(2)
        print(x, y1)
        print(x, y2)
        self.driver.swipe(x, y2, x, y1, 500)


# 区域点击(针对NAF=true的元素进行点击)
class RegionalClick(object):
    def __init__(self, elements):
        self.driver = GetAppDriver().driver
        # 获取当前元素bounds
        bounds = self.driver.find_element_by_id(elements).get_attribute("bounds")
        time.sleep(2)
        # 提取bounds中坐标值
        Bounds = re.findall(r"\[(.+?)\]", bounds)
        self.x1 = re.findall(r".+"",", Bounds[0])[0].strip().strip(",")
        self.y1 = re.findall(r","".+", Bounds[0])[0].strip().strip(",")
        self.x2 = re.findall(r".+"",", Bounds[1])[0].strip().strip(",")
        self.y2 = re.findall(r","".+", Bounds[1])[0].strip().strip(",")

    # 元素中心点击
    def CoreClick(self):
        x = int(self.x1) + (int(self.x2) - int(self.x1)) / 2
        y = int(self.y1) + (int(self.y2) - int(self.y1)) / 2
        self.driver.tap([(x, y)], 500)

# if __name__ == '__main__':
# Screen().CalculatedPercentage(1300, 2450)
# A = Tools.FindSource("btn_post")
# print(A)
