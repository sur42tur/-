import sys
import configparser
import random
import time

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Ui_untitled import *
import res_rc
import ast

# 抽卡概率
prob_7 = ""
prob_6 = ""
prob_5 = ""
prob_4 = ""
# 卡池列表
list_3 = ""
list_4_1 = ""
list_4_2 = ""
list_4_3 = ""
list_5_1 = ""
list_5_2 = ""
list_5_3 = ""
list_6_1 = ""
list_6_2 = ""
list_6_3 = ""
list_7_1 = ""
list_7_2 = ""
list_7_3 = ""
# 保底数
luck_4 = 0
luck_5 = 0
luck_6 = 0


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # 添加字体
        fontDb = QFontDatabase()
        fontID = fontDb.addApplicationFont(":/font/res/zh-cn.ttf")
        fontFamilies = fontDb.applicationFontFamilies(fontID)
        print(fontFamilies)
        self.setFont(QFont("SDK_SC_Web"))
        # 初始化窗口
        self.setupUi(self)
        self.init()
        self.pushButton.mousePressEvent = self.danchou
        self.pushButton_2.mousePressEvent = self.shilian
        self.pushButton_3.mousePressEvent = self.goto_chongzhi
        self.pushButton_4.mousePressEvent = self.goto_chouka
        self.frame_17.mousePressEvent = self.fenqiu__goumai
        self.frame.mousePressEvent = self.yuanshi__goumai
        # 无边框窗口
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(
            QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)

    # 无边框窗口的移动
    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None

    def mouseMoveEvent(self, e: QMouseEvent):
        try:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)
        except:
            pass

    def init(self):
        self.init_ini()
        self.init_outputbox()

    def init_ini(self):
        # 确认配置文件是否存在
        try:
            f = open("setting.ini")
            f.close()
            print("找到配置文件\n")
        except IOError:
            # 创建配置
            config = configparser.ConfigParser()
            # 加载配置
            config["money"] = {
                "yuanshi": "160",
                "fenqiu": "160",
            }
            luck_4
            config["luck"] = {
                "luck_4": "0",
                "luck_5": "0",
                "luck_6": "0",

            }
            config["probability"] = {
                "prob_7": "0.005",
                "prob_6": "0.05",
                "prob_5": "0.8",
                "prob_4": "5.1",
            }
            config["pool"] = {
                 "list_3": [
                    "小学学霸",
                    "初中学霸",
                    "高中学霸",
                    "专业拧螺丝",
                    "专业踩缝纫机",
                    "专业送外卖",
                    "专业直播",
                    "能量饮料",
                    "优质草药",
                    "美容丸",
                    "初级好感光环",
                ],
                "list_4_1": [
                    "专业修电脑",
                    "专业做家务",
                    "专业调饮师",
                    "专业厨师",
                    "专业教师",
                    "大学学霸",
                    "精英硕士",
                ],
                "list_4_2": [
                    "好感光环",
                    "好运光环",

                ],
                "list_4_3": [
                    "超级草药",
                    "驻颜丹",
                    "大力丸",
                ],
                "list_5_1": [
                    "中华医术之圣",
                    "驾驶大师",
                    "超级黑客",
                    "烹饪大师",
                    "音乐大师",
                    "绘画大师",
                    "电竞大师",
                ],
                "list_5_2": [
                    "降智光环",
                    "智力光环",
                    "活力光环",
                    "魅力光环",
                    "幸运光环",
                ],
                "list_5_3": [
                    "随机百万级汽车",
                    "随机千万级别墅",
                    "随机百万级公务飞机",
                    "随机上市公司的最高股份",
                    "无限额度信用卡",
                    "储物背包",
                    "治疗灵药",
                    "琼肌玉肤丹",
                ],
                "list_6_1": [
                    "百万吨力量",
                    "超音速",
                    "鉴定",
                    "隐匿",
                    "兵王附身"
                ],
                "list_6_2": [
                    "无限额度信用卡",
                    "随机千万级豪车",
                    "随机亿级庄园别墅",
                    "随机百亿市值公司的最高股份",
                    "储物项链",
                    "神圣治疗灵药",
                ],
                "list_6_3": [
                    "减速光环",
                    "极速光环",
                    "顺从光环",
                    "真视光环",
                    "强运光环"
                ],
                "list_7_1": [
                    "时间",
                    "HEAL",
                    "混沌",
                    "元素",
                    "化身神灵"
                ],
                "list_7_2": [
                    "暴食光环",
                    "愤怒光环",
                    "怠惰光环",

                ],
                "list_7_3": [
                    "乾坤袋",
                    "九天延寿丹",
                    "轩辕剑",
                    "炼妖壶",
                    "神农鼎",
                    "东皇钟",
                    "昆仑镜"
                ]

            }
            # 创建ini文件
            with open("setting.ini", "w") as configfile:
                # 写入配置
                config.write(configfile)
            print("初始化应用配置完成！\n")

    def init_outputbox(self):
        # 读取配置文件
        config = configparser.ConfigParser()
        config.read("setting.ini", encoding="gbk")
        global prob_7, prob_6, prob_5, prob_4, list_3, list_4_1, list_4_2, list_4_3, \
        list_5_1, list_5_2, list_5_3, list_6_1, list_6_2, list_6_3, list_7_1, list_7_2, list_7_3, luck_4, luck_5, luck_6

        prob_7 = config.getfloat("probability", "prob_7")
        prob_6 = config.getfloat("probability", "prob_6")
        prob_5 = config.getfloat("probability", "prob_5")
        prob_4 = config.getfloat("probability", "prob_4")

        list_3 = ast.literal_eval(config.get("pool", "list_3"))
        list_4_1 = ast.literal_eval(config.get("pool", "list_4_1"))
        list_4_2 = ast.literal_eval(config.get("pool", "list_4_2"))
        list_4_3 = ast.literal_eval(config.get("pool", "list_4_3"))
        list_5_1 = ast.literal_eval(config.get("pool", "list_5_1"))
        list_5_2 = ast.literal_eval(config.get("pool", "list_5_2"))
        list_5_3 = ast.literal_eval(config.get("pool", "list_5_3"))
        list_6_1 = ast.literal_eval(config.get("pool", "list_6_1"))
        list_6_2 = ast.literal_eval(config.get("pool", "list_6_2"))
        list_6_2 = ast.literal_eval(config.get("pool", "list_6_3"))
        list_7_1 = ast.literal_eval(config.get("pool", "list_7_1"))
        list_7_2 = ast.literal_eval(config.get("pool", "list_7_2"))
        list_7_3 = ast.literal_eval(config.get("pool", "list_7_3"))


        luck_4 = config.get("luck", "luck_4")
        luck_5 = config.get("luck", "luck_5")
        luck_6 = config.get("luck", "luck_6")

        dict1 = dict(config.items("money"))
        # 设置显示金钱
        self.label_11.setText(dict1["yuanshi"])
        self.label_13.setText(dict1["fenqiu"])
        self.label_23.setText(dict1["yuanshi"])
        self.label_25.setText(dict1["fenqiu"])
        # 输出窗口
        self.plainTextEdit.setPlainText(
            "抽卡改变人生\n" + "-" * 24
        )

    def goto_chongzhi(self, event):
        # 进入充值界面
        self.stackedWidget.setCurrentIndex(1)
        config = configparser.ConfigParser()
        config.read("setting.ini", encoding="gbk")
        fenqiu = config.getint("money", "fenqiu")
        yuanshi = config.getint("money", "yuanshi")

        self.label_13.setText(str(fenqiu))
        self.label_25.setText(str(fenqiu))
        self.label_11.setText(str(yuanshi))
        self.label_23.setText(str(yuanshi))

    def goto_chouka(self, event):
        # 进入抽卡界面
        self.stackedWidget.setCurrentIndex(0)
        config = configparser.ConfigParser()
        config.read("setting.ini", encoding="gbk")
        fenqiu = config.getint("money", "fenqiu")
        yuanshi = config.getint("money", "yuanshi")

        self.label_13.setText(str(fenqiu))
        self.label_25.setText(str(fenqiu))
        self.label_11.setText(str(yuanshi))
        self.label_23.setText(str(yuanshi))

    def fenqiu_jian(self):
        # 纠缠之缘的减扣事件
        config = configparser.ConfigParser()
        config.read("setting.ini", encoding="gbk")
        fenqiu = config.getint("money", "fenqiu")
        fenqiu = fenqiu - 1
        config.set("money", "fenqiu", str(fenqiu))
        config.write(open("setting.ini", "w"))

        self.label_13.setText(str(fenqiu))
        self.label_25.setText(str(fenqiu))

    def fenqiu_jian_10(self):
        # 纠缠之缘的减扣事件 * 10
        config = configparser.ConfigParser()
        config.read("setting.ini", encoding="gbk")
        fenqiu = config.getint("money", "fenqiu")
        fenqiu = fenqiu - 10
        config.set("money", "fenqiu", str(fenqiu))
        config.write(open("setting.ini", "w"))

        self.label_13.setText(str(fenqiu))
        self.label_25.setText(str(fenqiu))

    def danchou(self, event):
        # 单抽函数
        config = configparser.ConfigParser()
        config.read("setting.ini", encoding="gbk")
        fenqiu = config.getint("money", "fenqiu")

        if fenqiu < 1:
            QMessageBox.information(self, "失败", "余额不足！")
        else:
            try:
                self.fenqiu_jian()
            except PermissionError:
                pass
            try:
                self.choujiang()
            except PermissionError:
                self.choujiang()
            default_format = QtGui.QTextCharFormat()
            self.plainTextEdit.setCurrentCharFormat(default_format)
            self.plainTextEdit.appendPlainText("-" * 24)

    def fenqiu__goumai(self, event):
        # 纠缠之缘的购买
        config = configparser.ConfigParser()
        config.read("setting.ini", encoding="gbk")
        fenqiu = config.getint("money", "fenqiu")
        yuanshi = config.getint("money", "yuanshi")

        if yuanshi < 1600:
            QMessageBox.information(self, "失败", "余额不足！")
        else:
            fenqiu = fenqiu + 10
            yuanshi = yuanshi - 1600

        config.set("money", "fenqiu", str(fenqiu))
        config.set("money", "yuanshi", str(yuanshi))
        config.write(open("setting.ini", "w"))

        self.label_13.setText(str(fenqiu))
        self.label_25.setText(str(fenqiu))
        self.label_11.setText(str(yuanshi))
        self.label_23.setText(str(yuanshi))

    def yuanshi__goumai(self, event):
        # 原石的购买
        config = configparser.ConfigParser()
        config.read("setting.ini", encoding="gbk")
        yuanshi = config.getint("money", "yuanshi")
        yuanshi = yuanshi + 6480
        config.set("money", "yuanshi", str(yuanshi))
        config.write(open("setting.ini", "w"))

        self.label_11.setText(str(yuanshi))
        self.label_23.setText(str(yuanshi))

    def shilian(self, event):
        # 十连
        config = configparser.ConfigParser()
        config.read("setting.ini", encoding="gbk")
        fenqiu = config.getint("money", "fenqiu")

        if fenqiu < 10:
            QMessageBox.information(self, "失败", "余额不足！")
        else:
            try:
                self.fenqiu_jian_10()
            except PermissionError:
                pass
            for i in range(10):
                try:
                    self.choujiang()
                except PermissionError:
                    self.choujiang()
            default_format = QtGui.QTextCharFormat()
            self.plainTextEdit.setCurrentCharFormat(default_format)
            self.plainTextEdit.appendPlainText("-" * 15)

    def choujiang(self):
        # 抽卡主要函数，概率等
        global luck_4, luck_5, luck_6
        config = configparser.ConfigParser()
        config.read("setting.ini", encoding="gbk")
        result_1 = random.randint(1, 100000)
        num = random.randint(0,2)

        luck_4 = int(config.get("luck", "luck_4"))
        luck_5 = int(config.get("luck", "luck_5"))
        luck_6 = int(config.get("luck", "luck_6"))

        # 稀有保底
        if luck_4 >= 10:
            luck_4 = 0
            luck_5 = luck_5 + 1
            luck_6 = luck_6 + 1
            if num == 0:
                ch_name = random.choice(list_4_1)
                result_2 = "[稀有]  " + ch_name
            elif num == 1:
                ch_name = random.choice(list_4_2)
                result_2 = "[稀有]  " + ch_name
            else:
                ch_name = random.choice(list_4_3)
                result_2 = "[稀有]  " + ch_name
        # 史诗保底
        elif luck_5 >= 100:
            luck_5 = 0
            luck_4 = luck_4 + 1
            luck_6 = luck_6 + 1
            if num == 0:
                ch_name = random.choice(list_5_1)
                result_2 = "[史诗]  " + ch_name
            elif num == 1:
                ch_name = random.choice(list_5_2)
                result_2 = "[史诗]  " + ch_name
            else:
                ch_name = random.choice(list_5_3)
                result_2 = "[史诗]  " + ch_name
        # 传说保底
        elif luck_6 >= 1000:
            luck_6 = 0
            luck_5 = luck_5 + 1
            luck_4 = luck_4 + 1
            if num == 0:
                ch_name = random.choice(list_6_1)
                result_2 = "[传说]" + ch_name

            elif num == 1:
                ch_name = random.choice(list_6_2)
                result_2 = "[传说]" + ch_name

            else:
                ch_name = random.choice(list_6_3)
                result_2 = "[传说]" + ch_name
        # 正常抽卡
        else:
            # 三星抽卡
            if 0 <= result_1 < 100000 - prob_4 * 1000 - prob_5 * 1000 - prob_6 * 1000 - prob_7 * 1000:
                luck_4 = luck_4 + 1
                luck_5 = luck_5 + 1
                luck_6 = luck_6 + 1
                ch_name = random.choice(list_3)
                result_2 = "[普通]  " + ch_name
            # 稀有抽卡
            elif 100000 - prob_4 * 1000 - prob_5 * 1000 - prob_6 * 1000 - prob_7 * 1000 <= result_1 < 100000 - prob_5 * 1000 - prob_6 * 1000 - prob_7 * 1000:
                luck_6 = luck_6 + 1
                luck_5 = luck_5 + 1
                luck_4 = 0
                if num == 0:
                    ch_name = random.choice(list_4_1)
                    result_2 = "[稀有]  " + ch_name
                elif num == 1:
                    ch_name = random.choice(list_4_2)
                    result_2 = "[稀有]  " + ch_name
                else:
                    ch_name = random.choice(list_4_3)
                    result_2 = "[稀有]  " + ch_name
            # 史诗抽卡
            elif 100000 - prob_5 * 1000 - prob_6 * 1000 - prob_7 * 1000 <= result_1 < 100000 - prob_6 * 1000 - prob_7 * 1000:
                luck_5 = 0
                luck_4 = luck_4 + 1
                luck_6 = luck_6 + 1
                if num == 0:
                    ch_name = random.choice(list_5_1)
                    result_2 = "[史诗]  " + ch_name
                elif num == 1:
                    ch_name = random.choice(list_5_2)
                    result_2 = "[史诗]  " + ch_name
                else:
                    ch_name = random.choice(list_5_3)
                    result_2 = "[史诗]  " + ch_name
            #传说抽卡
            elif 100000 - prob_6 * 1000 - prob_7 * 1000 <= result_1 < 100000 - prob_7 * 1000:
                luck_6 = 0
                luck_5 = luck_5 + 1
                luck_4 = luck_4 + 1
                if num == 0:
                    ch_name = random.choice(list_6_1)
                    result_2 = "[传说]  " + ch_name
                elif num == 1:
                    ch_name = random.choice(list_6_2)
                    result_2 = "[传说]  " + ch_name
                else:
                    ch_name = random.choice(list_6_3)
                    result_2 = "[传说]  " + ch_name
            #神话抽卡
            else:
                luck_6 = luck_6 + 1
                luck_5 = luck_5 + 1
                luck_4 = luck_4 + 1
                if num == 0:
                    ch_name = random.choice(list_7_1)
                    result_2 = "[神话]  " + ch_name
                elif num == 1:
                    ch_name = random.choice(list_7_2)
                    result_2 = "[神话]  " + ch_name
                else:
                    ch_name = random.choice(list_7_3)
                    result_2 = "[神话]  " + ch_name
            
        config.set("luck", "luck_4", str(luck_4))
        config.set("luck", "luck_5", str(luck_5))
        config.set("luck", "luck_6", str(luck_6))
        config.write(open("setting.ini", "w"))

        text_format = QTextCharFormat()

        if result_2.find("[普通]")!= -1:
            text = f"{result_2}"
            text_color = QColor("black")  # 黑色


        elif result_2.find("[稀有]")!= -1:
            text = f"{result_2}"
            text_color = QColor("blue")  # 蓝色

        elif result_2.find("[史诗]")!= -1:
            text = f"{result_2}"
            text_color = QColor("purple")  # 紫色


        elif result_2.find("[传说]")!= -1:
            text = f"{result_2}"
            text_color = QColor("gold")  # 金色

        else:
            # 神话
            text = f"{result_2}"
            text_color = QColor("red")  # 红色

        # 将格式化的文本追加到 plainTextEdit 控件中
        self.plainTextEdit.appendHtml(f'<span style="color: {text_color.name()};">{text}</span>')

        # 应用样式到最新追加的文本
        text_format.setForeground(text_color)
        self.plainTextEdit.setCurrentCharFormat(text_format)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = MainWindow()
    a.show()
    sys.exit(app.exec_())
