from src.common.GetAppDriver import GetAppDriver
import time


# ----------
# 弹窗处理工具
# ----------
class PopupProcessing(object):
    def __init__(self):
        self.driver = GetAppDriver().driver
        time.sleep(5)

    # 查找弹窗，如果存在则返回True
    def Popup_GeneralMethod(self, **elements):
        # **为可传项；如果该元素有text属性，传入**text时会判断精确符合。
        for key in elements:
            global element
            element = elements.get(key)
            if key == "ID":
                if PopupProcessing().ID():
                    return True
            elif key == "IDS":
                if PopupProcessing().IDS():
                    return True
            elif key == "Cla":
                if PopupProcessing().Cla():
                    return True
            elif key == "ClaS":
                if PopupProcessing().ClaS():
                    return True
            elif key == "AID":
                if PopupProcessing().AID():
                    return True
            elif key == "AIDS":
                if PopupProcessing().AIDS():
                    return True
            elif key == "AU":
                if PopupProcessing().AU():
                    return True
            elif key == "AUS":
                if PopupProcessing().AUS():
                    return True
            elif key == "Xpa":
                if PopupProcessing().Xpa():
                    return True
            elif key == "XpaS":
                if PopupProcessing().XpaS():
                    return True
            else:
                print(key)
                return False

    # 1.ID = [ID, **text]
    def ID(self):
        # 提取键值
        ID = element
        # 如果值是字符串
        if isinstance(ID, str):
            # 提取值
            element_id = ID
            # 查找元素，存在返回True
            try:
                self.driver.find_element_by_id(element_id)
                return True
            # 否则返回False
            except:
                print("弹窗未找到:", ID)
                return False
        # 如果值是列表
        elif isinstance(ID, list):
            # 提取值
            element_id = ID[0]
            element_id_text = ID[1]
            # 查找元素，存在且文案相符返回True
            try:
                Ele_text = self.driver.find_element_by_id(element_id).text
                # 精准匹配，如果文案相符
                if Ele_text == element_id_text:
                    return True
                # 否则返回当前文案
                else:
                    print(Ele_text)
                    return False
            # 否则返回False
            except:
                print("弹窗未找到:", element_id)
                return False
        # 否则返回值的属性
        else:
            print(type(ID))
            return False

    # 2.IDS = [IDS, index, **text]
    def IDS(self):
        # 提取键值
        IDS = element
        # 如果值是列表
        if isinstance(IDS, list):
            # 且有两个值
            if len(IDS) == 2:
                # 提取值
                element_ids = IDS[0]
                element_ids_number = IDS[1]
                # 查找元素，存在则返回True
                try:
                    Ele_text = self.driver.find_elements_by_id(element_ids)[element_ids_number].text
                    print(Ele_text)
                    return True
                # 否则返回False
                except:
                    print("弹窗未找到:", IDS)
                    return False
            # 或有三个值
            elif len(IDS) == 3:
                # 提取值
                element_ids = IDS[0]
                element_ids_number = IDS[1]
                element_ids_text = IDS[2]
                # 查找元素，存在且文案相符返回True
                try:
                    Ele_text = self.driver.find_elements_by_id(element_ids)[element_ids_number].text
                    # 精准匹配，如果文案相符
                    if Ele_text == element_ids_text:
                        return True
                    # 否则返回当前文案
                    else:
                        print(Ele_text)
                        return False
                # 否则返回False
                except:
                    print("弹窗未找到:", IDS)
                    return False
            # 否则返回值个数
            else:
                print(len(IDS))
                return False
        # 否则返回值类型
        else:
            print(type(IDS))
            return False

    # 3.Cla = [Cla, **text]
    def Cla(self):
        # 提取键值
        Cla = element
        # 如果值是字符串
        if isinstance(Cla, str):
            # 提取值
            element_cla = Cla
            # 查找元素，存在则返回True
            try:
                self.driver.find_element_by_class_name(element_cla)
                return True
            # 否则返回False
            except:
                print("弹窗未找到:", Cla)
                return False
        # 如果值是列表
        elif isinstance(Cla, list):
            # 提取值
            element_cla = Cla[0]
            element_cla_text = Cla[1]
            # 查找元素，存在则返回True
            try:
                Ele_text = self.driver.find_element_by_class_name(element_cla).text
                if Ele_text == element_cla_text:
                    return True
                # 否则返回当前文案
                else:
                    print(Ele_text)
                    return False
            # 否则返回False
            except:
                print("弹窗未找到:", Cla)
                return False
        # 否则返回值类型
        else:
            print(type(Cla))
            return False

    # 4.ClaS = [ClaS, index, **text]
    def ClaS(self):
        # 提取键值
        ClaS = element
        # 如果值是列表
        if isinstance(ClaS, list):
            # 且有两个值
            if len(ClaS) == 2:
                # 提取值
                element_clas = ClaS[0]
                element_clas_number = ClaS[1]
                # 查找元素，存在则返回True
                try:
                    Ele_text = self.driver.find_elements_by_class_name(element_clas)[element_clas_number].text
                    print(Ele_text)
                    return True
                # 否则返回False
                except:
                    print("弹窗未找到:", ClaS)
                    return False
            # 或有三个值
            elif len(ClaS) == 3:
                # 提取值
                element_clas = ClaS[0]
                element_clas_number = ClaS[1]
                element_clas_text = ClaS[2]
                # 查找元素，存在且文案相符返回True
                try:
                    Ele_text = self.driver.find_elements_by_class_name(element_clas)[element_clas_number].text
                    # 精准匹配，如果文案相符
                    if Ele_text == element_clas_text:
                        return True
                    # 否则返回当前文案
                    else:
                        print(Ele_text)
                        return False
                # 否则返回False
                except:
                    print("弹窗未找到:", ClaS)
                    return False
            # 否则返回值个数
            else:
                print(len(ClaS))
                return False
        # 否则返回值类型
        else:
            print(type(ClaS))
            return False

    # 5.AID = [AID, **text]
    def AID(self):
        # 提取键值
        AID = element
        # 如果值是字符串
        if isinstance(AID, str):
            # 提取值
            element_aid = AID
            # 查找元素，存在返回True
            try:
                self.driver.find_element_by_accessibility_id(element_aid)
                return True
            # 否则返回False
            except:
                print("弹窗未找到:", AID)
                return False
        # 如果值是列表
        elif isinstance(AID, list):
            # 提取值
            element_aid = AID[0]
            element_aid_text = AID[1]
            # 查找元素，存在且文案相符返回True
            try:
                Ele_text = self.driver.find_element_by_accessibility_id(element_aid).text
                # 精准匹配，如果文案相符
                if Ele_text == element_aid_text:
                    return True
                # 否则返回当前文案
                else:
                    print(Ele_text)
                    return False
            # 否则返回False
            except:
                print("弹窗未找到:", AID)
                return False
        # 否则返回值的属性
        else:
            print(type(AID))
            return False

    # 6.AIDS = [AIDS, index, **text]
    def AIDS(self):
        # 提取键值
        AIDS = element
        # 如果值是列表
        if isinstance(AIDS, list):
            # 且有两个值
            if len(AIDS) == 2:
                # 提取值
                element_aids = AIDS[0]
                element_aids_number = AIDS[1]
                # 查找元素，存在则返回True
                try:
                    Ele_text = self.driver.find_elements_by_accessibility_id(element_aids)[element_aids_number].text
                    print(Ele_text)
                    return True
                # 否则返回False
                except:
                    print("弹窗未找到:", AIDS)
                    return False
            # 或有三个值
            elif len(AIDS) == 3:
                # 提取值
                element_aids = AIDS[0]
                element_aids_number = AIDS[1]
                element_aids_text = AIDS[2]
                # 查找元素，存在且文案相符返回True
                try:
                    Ele_text = self.driver.find_elements_by_accessibility_id(element_aids)[element_aids_number].text
                    # 精准匹配，如果文案相符
                    if Ele_text == element_aids_text:
                        return True
                    # 否则返回当前文案
                    else:
                        print(Ele_text)
                        return False
                # 否则返回False
                except:
                    print("弹窗未找到:", AIDS)
                    return False
            # 否则返回值个数
            else:
                print(len(AIDS))
                return False
        # 否则返回值类型
        else:
            print(type(AIDS))
            return False

    # 7.AU = [AU, **text]
    def AU(self):
        # 提取键值
        AU = element
        # 如果值是字符串
        if isinstance(AU, str):
            # 提取值
            element_au = AU
            # 查找元素，存在返回True
            try:
                self.driver.find_element_by_android_uiautomator(element_au)
                return True
            # 否则返回False
            except:
                print("弹窗未找到:", AU)
                return False
        # 如果值是列表
        elif isinstance(AU, list):
            # 提取值
            element_au = AU[0]
            element_au_text = AU[1]
            # 查找元素，存在且文案相符返回True
            try:
                Ele_text = self.driver.find_element_by_android_uiautomator(element_au).text
                # 精准匹配，如果文案相符
                if Ele_text == element_au_text:
                    return True
                # 否则返回当前文案
                else:
                    print(Ele_text)
                    return False
            # 否则返回False
            except:
                print("弹窗未找到:", AU)
                return False
        # 否则返回值的属性
        else:
            print(type(AU))
            return False

    # 8.AUS = [AUS, index, **text]
    def AUS(self):
        # 提取键值
        AUS = element
        # 如果值是列表
        if isinstance(AUS, list):
            # 且有两个值
            if len(AUS) == 2:
                # 提取值
                element_aus = AUS[0]
                element_aus_number = AUS[1]
                # 查找元素，存在则返回True
                try:
                    Ele_text = self.driver.find_elements_by_android_uiautomator(element_aus)[element_aus_number].text
                    print(Ele_text)
                    return True
                # 否则返回False
                except:
                    print("弹窗未找到:", AUS)
                    return False
            # 或有三个值
            elif len(AUS) == 3:
                # 提取值
                element_aus = AUS[0]
                element_aus_number = AUS[1]
                element_aus_text = AUS[2]
                # 查找元素，存在且文案相符返回True
                try:
                    Ele_text = self.driver.find_elements_by_android_uiautomator(element_aus)[element_aus_number].text
                    # 精准匹配，如果文案相符
                    if Ele_text == element_aus_text:
                        return True
                    # 否则返回当前文案
                    else:
                        print(Ele_text)
                        return False
                # 否则返回False
                except:
                    print("弹窗未找到:", AUS)
                    return False
            # 否则返回值个数
            else:
                print(len(AUS))
                return False
        # 否则返回值类型
        else:
            print(type(AUS))
            return False

    # 9.Xpa = [Xpa, **text]
    def Xpa(self):
        # 提取键值
        Xpa = element
        # 如果值是字符串
        if isinstance(Xpa, str):
            # 提取值
            element_xpa = Xpa
            # 查找元素，存在返回True
            try:
                self.driver.find_element_by_xpath(element_xpa)
                return True
            # 否则返回False
            except:
                print("弹窗未找到:", Xpa)
                return False
        # 如果值是列表
        elif isinstance(Xpa, list):
            # 提取值
            element_xpa = Xpa[0]
            element_xpa_text = Xpa[1]
            # 查找元素，存在且文案相符返回True
            try:
                Ele_text = self.driver.find_element_by_xpath(element_xpa).text
                # 精准匹配，如果文案相符
                if Ele_text == element_xpa_text:
                    return True
                # 否则返回当前文案
                else:
                    print(Ele_text)
                    return False
            # 否则返回False
            except:
                print("弹窗未找到:", Xpa)
                return False
        # 否则返回值的属性
        else:
            print(type(Xpa))
            return False

    # 10.XpaS = [XpaS, index, **text]
    def XpaS(self):
        # 提取键值
        Xpas = element
        # 如果值是列表
        if isinstance(Xpas, list):
            # 且有两个值
            if len(Xpas) == 2:
                # 提取值
                element_xpas = Xpas[0]
                element_xpas_number = Xpas[1]
                # 查找元素，存在则返回True
                try:
                    Ele_text = self.driver.find_elements_by_xpath(element_xpas)[element_xpas_number].text
                    print(Ele_text)
                    return True
                # 否则返回False
                except:
                    print("弹窗未找到:", Xpas)
                    return False
            # 或有三个值
            elif len(Xpas) == 3:
                # 提取值
                element_xpas = Xpas[0]
                element_xpas_number = Xpas[1]
                element_xpas_text = Xpas[2]
                # 查找元素，存在且文案相符返回True
                try:
                    Ele_text = self.driver.find_elements_by_xpath(element_xpas)[element_xpas_number].text
                    # 精准匹配，如果文案相符
                    if Ele_text == element_xpas_text:
                        return True
                    # 否则返回当前文案
                    else:
                        print(Ele_text)
                        return False
                # 否则返回False
                except:
                    print("弹窗未找到:", Xpas)
                    return False
            # 否则返回值个数
            else:
                print(len(Xpas))
                return False
        # 否则返回值类型
        else:
            print(type(Xpas))
            return False
