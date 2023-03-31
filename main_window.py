import itertools
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QMovie
from PyQt5.QtWidgets import QLabel, QMessageBox, QFileDialog
import calculateParameters
import threading
import generateMap
import dynamicAnalysis
import os
import sensordeploymentoptions
import eventscenariooptions


##GLOBALS INITIATED BY ARBITRARY VALUES
temp_sensor_coord = []
temp_cumulative_sensor = []
cum_sensor_coord = []
last_sensor_float = []
last_sensor_coord = []
temp_launch_coord = []
temp_cumulative_launch = []
cum_launch_coord = []
last_launch_float = []
last_launch_coord = []
temp_impact_coord = []
temp_cumulative_impact = []
cum_impact_coord = []
last_impact_float = []
last_impact_coord = []
sensor_file_name = ''
event_file_name = ''
sensor_file_names = []
event_file_names = []
k1 = []
compared_sensors = []
compared_events = []
available_sensors_coord = []
available_sensors_name = []
available_events = []
imported_sensor_names = []
imported_sensor_coords = []
imported_events = []
tab_number = 0
list_value = 150
list_value2 = 150
sensor_option_signal = 0
event_option_signal = 0
state_1 = 0
element_signal = 0

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Networked CASTLE MST (Mission Simulation Tool)")
        MainWindow.setWindowTitle("Networked CASTLE MST (Mission Simulation Tool ver_1.0.0)")
        MainWindow.setMinimumSize(1600, 900)
        MainWindow.setStyleSheet("background-color: rgb(232, 232, 224);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QLabel(MainWindow)
        self.label1.setPixmap(self.pixmap1)
        self.label1.resize(self.pixmap1.width(), self.pixmap1.height())
        self.label1.move(30, 30)
        self.mainMenu = QtWidgets.QMenuBar(MainWindow)
        self.mainMenu.setGeometry(QtCore.QRect(0,0,800,26))
        self.mainMenu.setObjectName('mainMenu')
        self.fileMenu = self.mainMenu.addMenu('File')
        self.fileMenu.setObjectName('fileMenu')
        self.viewMenu = self.mainMenu.addMenu('View')
        self.viewMenu.setObjectName('viewMenu')
        self.settingsMenu = self.mainMenu.addMenu('Settings')
        self.settingsMenu.setObjectName('settingsMenu')
        self.toolsMenu = self.mainMenu.addMenu('Tools')
        self.toolsMenu.setObjectName('toolsMenu')
        self.helpMenu = self.mainMenu.addMenu('Help')
        self.helpMenu.setObjectName('helpMenu')
        self.open = self.fileMenu.addMenu('Open')
        self.open.setObjectName('open')
        self.importMission = self.fileMenu.addMenu('Import')
        self.importMission.setObjectName('importMenu')
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.askSensorDeploymentOption())
        self.pushButton.setGeometry(QtCore.QRect(70, 100, 211, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: #FFE4BB")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("marker.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.askEventScenarioOption())
        self.pushButton_2.setGeometry(QtCore.QRect(70, 150, 211, 41))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background-color: #FFE4BB")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("event.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.analysisPrimer())
        self.pushButton_3.setGeometry(QtCore.QRect(70, 250, 211, 41))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: #FFE4BB")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("analyze.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(70, 300, 211, 41))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("background-color: #FFE4BB")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("compare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_4.setObjectName("pushButton_4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(70, 410, 211, 391))
        self.frame.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 10, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame, clicked=lambda: self.resetAll())
        self.pushButton_6.setGeometry(QtCore.QRect(20, 340, 171, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setObjectName("pushButton_6")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(10, 50, 191, 81))
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(self.frame)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 160, 191, 81))
        self.listWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listWidget_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget_2.setObjectName("listWidget_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame, clicked=lambda: self.selectList())
        self.pushButton_7.setGeometry(QtCore.QRect(20, 300, 171, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_7.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("trashcan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon5)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame, clicked=lambda: self.addComparison())
        self.pushButton_9.setGeometry(QtCore.QRect(20, 260, 171, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_9.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("addscenario.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon6)
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(10, 140, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(70, 200, 211, 41))
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_8.setStyleSheet("background-color: #FFE4BB")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon7)
        self.pushButton_8.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_8.setAutoDefault(False)
        self.pushButton_8.setDefault(False)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 350, 211, 41))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("background-color: #FFE4BB")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("animation.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon8)
        self.pushButton_5.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_5.setObjectName("pushButton_5")
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(310, 80, 1191, 741))
        self.frame_2.setStyleSheet("background-color: rgb(56, 56, 56);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(2, 2, 1211, 751))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        generateMap.createMainMap(self.horizontalLayout)
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_10.setGeometry(QtCore.QRect(17, 79, 26, 26))
        self.pushButton_10.setStyleSheet("background-color: rgba(0, 0, 0, 50);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_0 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_0.setGeometry(QtCore.QRect(0, 0, 1200, 750))
        self.pushButton_0.setStyleSheet("background-color: rgba(0, 0, 0, 100);")
        self.pushButton_0.setObjectName("pushButton_0")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(110, 100, 111, 51))
        self.label_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_10.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_10.setLineWidth(2)
        self.label_10.setMidLineWidth(1)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(225, 100, 111, 71))
        self.label_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_11.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_11.setLineWidth(2)
        self.label_11.setMidLineWidth(1)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(340, 100, 99, 110))
        self.label_12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_12.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_12.setLineWidth(2)
        self.label_12.setMidLineWidth(1)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(330, 190, 99, 70))
        self.label_13.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_13.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_13.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_13.setLineWidth(2)
        self.label_13.setMidLineWidth(1)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_14.setGeometry(QtCore.QRect(40, 65, 80, 80))
        self.pushButton_14.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_14.setIcon(icon3)
        self.pushButton_14.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_14.setFlat(True)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_19 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_19.setGeometry(QtCore.QRect(1135, 82, 40, 40))
        self.pushButton_19.setStyleSheet("background-color: #ffffff;")
        self.pushButton_19.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pushButton_19.setAutoFillBackground(True)
        self.pushButton_19.setText("")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_19.setIcon(icon18)
        self.pushButton_19.setAutoDefault(False)
        self.pushButton_19.setFlat(False)
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_19.setToolTip('Save Sensor Deployment')
        self.pushButton_20 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_20.setGeometry(QtCore.QRect(1135, 135, 40, 40))
        self.pushButton_20.setStyleSheet("background-color: #ffffff;")
        self.pushButton_20.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pushButton_20.setAutoFillBackground(True)
        self.pushButton_20.setText("")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_20.setIcon(icon19)
        self.pushButton_20.setAutoDefault(False)
        self.pushButton_20.setFlat(False)
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_20.setToolTip('Save Event File')
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(-195, 160, 231, 451))
        self.frame_3.setStyleSheet("background: transparent")
        self.frame_3.setObjectName("frame_3")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 231, 451))
        self.label_5.setText("")
        self.label_5.setStyleSheet('background: transparent')
        self.label_5.setPixmap(QtGui.QPixmap("slidingmenu1.png"))
        self.label_5.setObjectName("label_5")
        self.pushButton_21 = QtWidgets.QPushButton(self.frame_3, clicked=lambda: self.slideOptions())
        self.pushButton_21.setGeometry(QtCore.QRect(190, 200, 31, 61))
        self.pushButton_21.setStyleSheet("background: transparent")
        self.pushButton_21.setObjectName("listWidget")
        self.pushButton_21.setToolTip('Click to expand more options')
        self.pushButton_21.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listWidget_3 = QtWidgets.QListWidget(self.frame_3)
        self.listWidget_3.setGeometry(QtCore.QRect(25, 290, 131, 111))
        self.listWidget_3.setStyleSheet("background-color: #ffffff;")
        self.listWidget_3.setObjectName("listWidget_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit.setGeometry(QtCore.QRect(35, 30, 113, 20))
        self.lineEdit.setStyleSheet("background-color: #ffffff;")
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(35, 12, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background:transparent")
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(35, 70, 61, 15))
        self.lineEdit_2.setStyleSheet("background-color: #ffffff;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(35, 85, 61, 15))
        self.lineEdit_4.setStyleSheet("background-color: #ffffff;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(99, 70, 21, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background:transparent")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(99, 84, 21, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background:transparent")
        self.label_9.setObjectName("label_6")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(35, 52, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background:transparent")
        self.label_6.setObjectName("label_6")
        self.pushButton_22 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_22.setGeometry(QtCore.QRect(35, 260, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton_22.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_22.setStyleSheet("background-color: #ffffff;")
        self.pushButton_22.setIcon(icon7)
        self.pushButton_22.setIconSize(QtCore.QSize(12, 12))
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.frame_3, clicked=lambda: self.finishDeployment())
        self.pushButton_23.setGeometry(QtCore.QRect(35, 230, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton_23.setFont(font)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("finish.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_23.setStyleSheet("background-color: #ffffff;")
        self.pushButton_23.setIcon(icon8)
        self.pushButton_23.setIconSize(QtCore.QSize(12, 12))
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_24.setGeometry(QtCore.QRect(35, 410, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton_24.setStyleSheet("background-color: #ffffff;")
        self.pushButton_24.setFont(font)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("trash2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_24.setIcon(icon9)
        self.pushButton_24.setIconSize(QtCore.QSize(12, 12))
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.frame_3, clicked=lambda: self.getInfoElement())
        self.pushButton_25.setGeometry(QtCore.QRect(125, 70, 21, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton_25.setStyleSheet("background-color: #ffffff;")
        self.pushButton_25.setFont(font)
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.frame_3, clicked=lambda: self.locateElement())
        self.pushButton_26.setGeometry(QtCore.QRect(35, 105, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton_26.setStyleSheet("background-color: #ffffff;")
        self.pushButton_26.setFont(font)
        self.pushButton_26.setObjectName("pushButton_26")
        self.radioButton = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton.setGeometry(QtCore.QRect(35, 130, 70, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("background:transparent")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_2.setGeometry(QtCore.QRect(93, 130, 65, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("background:transparent")
        self.radioButton_2.setObjectName("radioButton_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(35, 167, 111, 16))
        self.lineEdit_5.setStyleSheet("background-color: #ffffff;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(35, 205, 111, 16))
        self.lineEdit_6.setStyleSheet("background-color: #ffffff;")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_14 = QtWidgets.QLabel(self.frame_3)
        self.label_14.setGeometry(QtCore.QRect(35, 149, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background:transparent")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_3)
        self.label_15.setGeometry(QtCore.QRect(35, 187, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background:transparent")
        self.label_15.setObjectName("label_15")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(310, 57, 1190, 21))
        self.tabs.setObjectName("tabs")
        self.tabs.setTabsClosable(True)
        self.lineEdit_2.setDisabled(True)
        self.lineEdit_4.setDisabled(True)
        self.lineEdit.setDisabled(True)
        self.lineEdit_5.setDisabled(True)
        self.lineEdit_6.setDisabled(True)
        self.radioButton_2.setDisabled(True)
        self.radioButton.setDisabled(True)
        self.pushButton_25.setDisabled(True)
        self.pushButton_24.setDisabled(True)
        self.pushButton_23.setDisabled(True)
        self.pushButton_22.setDisabled(True)
        self.pushButton_26.setDisabled(True)
        self.pushButton_19.hide()
        self.pushButton_20.hide()
        self.label_10.hide()
        self.label_11.hide()
        self.label_12.hide()
        self.pushButton_19.setDisabled(True)
        # self.pushButton_3.setDisabled(True)
        self.pushButton_4.setDisabled(True)
        self.pushButton_5.setDisabled(True)
        self.pushButton_8.setDisabled(True)
        self.pushButton_14.hide()
        self.label_13.hide()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.movie = QMovie("mousecircle.gif")
        self.label_12.setMovie(self.movie)
        self.movie.start()
        self.lineEdit.textChanged.connect(self.lineActivity)
        self.lineEdit_2.textChanged.connect(self.lineActivity_2)
        self.lineEdit_4.textChanged.connect(self.lineActivity_2)
        self.lineEdit_5.textChanged.connect(self.lineActivity_3)
        self.lineEdit_6.textChanged.connect(self.lineActivity_4)
        self.radioButton.clicked.connect(self.selectLaunchImpact)
        self.radioButton_2.clicked.connect(self.selectLaunchImpact)
        self.tabs.currentChanged.connect(self.clickedTab)
        self.tabs.tabCloseRequested.connect(self.closeCurrentTab)
        self.listWidget.currentRowChanged.connect(self.listValue)
        self.listWidget_2.currentRowChanged.connect(self.listValue_2)

    def analysisPrimer(self):
        for i in range(0, len(imported_sensor_names)):
            calculateParameters.calculate(imported_events, imported_sensor_coords[i], imported_sensor_names[i])
        dynamicAnalysis.createTable()

    def addComparison(self):
        global compared_sensors, compared_events, available_sensors_coord, available_events, available_sensors_name
        file_name = self.tabs.tabText(self.tabs.currentIndex())
        file_name = file_name.replace('<', '[')
        file_name = file_name.replace('>', ']')
        if file_name[1] == 's':
            if file_name in compared_sensors:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('This deployment was already added to the comparison list!')
                msg.setWindowTitle("Error")
                msg.exec_()
            else:
                compared_sensors.append(file_name)
                self.listWidget.addItem(file_name)
                available_sensors_coord.append(calculateParameters.actual_sensor_coord)
                available_sensors_name.append(calculateParameters.name_sensor)
        elif file_name[1] == 'e':
            if file_name in compared_events:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('This event was already added to the comparison list!')
                msg.setWindowTitle("Error")
                msg.exec_()
            else:
                compared_events.append(file_name)
                self.listWidget_2.addItem(file_name)
                available_events.append(calculateParameters.event_array)
        if self.listWidget_2.count() > 0 and self.listWidget.count() > 0:
            self.pushButton_3.setEnabled(True)
        elif self.listWidget.count() == 0 or self.listWidget_2.count() == 0:
            self.pushButton_3.setDisabled(True)

    def listValue(self, row):
        global list_value, list_value2
        list_value = row
        list_value2 = 100

    def listValue_2(self, row_1):
        global list_value2, list_value
        list_value2 = row_1
        list_value = 100

    def removeSensorComparison(self):
        global list_value, list_value2, compared_sensors
        try:
            sensor = list_value
            self.listWidget.takeItem(sensor)
            compared_sensors.pop(sensor)
        except IndexError:
            self.listWidget.takeItem(sensor)

    def removeEventComparison(self):
        global list_value2, list_value, compared_events
        try:
            event = list_value2
            self.listWidget_2.takeItem(event)
            compared_events.pop(event)
        except IndexError:
            self.listWidget_2.takeItem(event)

    def selectList(self):
        if list_value == 100:
            self.removeEventComparison()
        elif list_value2 == 100:
            self.removeSensorComparison()

    def clickedTab(self):
        calculateParameters.resetAll()
        self.listWidget_3.clear()
        file_name = self.tabs.tabText(self.tabs.currentIndex())
        file_name = file_name.replace('<', '[')
        file_name = file_name.replace('>', ']')
        file_name = file_name + '.txt'
        if file_name[1] == 's':
            try:
                with open(file_name) as f:
                    lines = f.readlines()
                i = 0
                for line in lines:

                    line = line.replace(']', '')
                    line = line.replace('[', '')
                    line = line.replace("'", '')
                    line = line.replace('\n', '')
                    if i == 0:
                        calculateParameters.name_sensor = list(line.split(", "))
                    elif i == 1:
                        temp_s = list(line.split(", "))
                        t_s = []
                        t_ss = []
                        for s in temp_s:
                            s = float(s)
                            t_s.append(s)
                        while True:
                            t_ss.append(t_s[0])
                            t_ss.append(t_s[1])
                            calculateParameters.actual_sensor_coord.append(t_ss)
                            t_s.pop(0)
                            t_s.pop(0)
                            t_ss = []
                            if len(t_s) == 0:
                                break
                    i = i + 1

                for j in reversed(range(self.horizontalLayout.count())):
                    self.horizontalLayout.itemAt(j).widget().deleteLater()
                generateMap.updateSeconder(self.horizontalLayout)
                self.pushButton_0.hide()
                # self.pushButton_3.setDisabled(True)
                self.pushButton_8.setEnabled(True)
            except FileNotFoundError:
                pass
            for k in calculateParameters.name_sensor:
                if len(calculateParameters.actual_sensor_coord) > 0:
                    self.listWidget_3.addItem(k + '  ' + str(
                        calculateParameters.actual_sensor_coord[calculateParameters.name_sensor.index(k)]))
                else:
                    pass
        elif file_name[1] == 'e':
            a = []
            b = []
            c = []
            d = []
            try:
                with open(file_name) as f:
                    lines = f.read().splitlines()

                for line, i in zip(lines, range(0, len(lines))):
                    if i % 9 == 1 or i % 9 == 3:
                        line = line.replace('[', '')
                        line = line.replace(']', '')
                        b = line.split(', ')
                        for j in b:
                            a.append(float(j))
                        c.append(a)
                        a = []
                        b = []

                    elif i % 9 == 4 or i % 9 == 6:
                        c.append(float(line))
                    elif i % 9 == 0:
                        c = []
                        c.append(line)
                    else:
                        c.append(line)
                    d.append(c)
                for i in d:
                    if i not in calculateParameters.event_array:
                        calculateParameters.event_array.append(i)
                for k in calculateParameters.event_array:
                    calculateParameters.actual_launch_coord.append(k[1])
                    calculateParameters.actual_impact_coord.append(k[3])
                    calculateParameters.name_launch.append(k[0])
                    calculateParameters.name_impact.append(k[2])
                calculateParameters.event_array[-1].insert(4, 1)
                calculateParameters.event_array[-1].insert(6, 1)
                calculateParameters.event_array[-1].insert(8, '330')
                calculateParameters.event_array[-1][5] = str(calculateParameters.event_array[-1][5])

                for j in reversed(range(self.horizontalLayout.count())):
                    self.horizontalLayout.itemAt(j).widget().deleteLater()
                generateMap.updateImpactMap(self.horizontalLayout)
            except FileNotFoundError:
                pass
            for i in calculateParameters.event_array:
                self.listWidget_3.addItem(str(i))

    def addNewTab(self):
        global tab_number
        tab_number = tab_number + 1
        self.tab = QtWidgets.QWidget()
        if element_signal == 1:
            i = self.tabs.addTab(self.tab, ('<sensor>' + str(sensor_file_name).removesuffix('.txt')))
        elif element_signal == 2:
            i = self.tabs.addTab(self.tab, ('<event>' + str(event_file_name).removesuffix('.txt')))
        self.tabs.setCurrentIndex(i)

    def closeCurrentTab(self):
        global tab_number
        i = self.tabs.currentIndex()
        self.tabs.removeTab(i)
        tab_number = tab_number - 1

    def locateElement(self):
        self.pushButton_0.hide()
        self.pushButton_10.hide()
        self.label_10.show()
        self.label_11.show()
        self.label_12.show()
        self.pushButton_14.show()
        self.lineEdit_2.clear()
        self.lineEdit_4.clear()
        self.lineEdit_2.setDisabled(True)
        self.lineEdit_4.setDisabled(True)
        self.pushButton_25.setDisabled(True)
        self.pushButton_26.setDisabled(True)
        t1 = threading.Thread(target=self.ifClicked)
        t1.start()

    def ifClicked(self):
        a = len(generateMap.temp_cumulative)
        while True:
            if len(generateMap.temp_cumulative) > a:
                self.lineEdit_2.setText(str(generateMap.lat_temp))
                self.lineEdit_4.setText(str(generateMap.long_temp))
                self.pushButton_10.show()
                break
            else:
                self.pushButton_10.hide()
                pass
        self.label_10.hide()
        self.label_11.hide()
        self.label_12.hide()
        self.pushButton_14.hide()

    def getInfoElement(self):
        global last_sensor_coord, last_launch_coord, last_impact_coord, k1
        self.pushButton_23.setEnabled(True)
        if element_signal == 1:
            temp_sensor_coord.append(float(self.lineEdit_2.text()))
            temp_sensor_coord.append(float(self.lineEdit_4.text()))
            temp_cumulative_sensor.append(temp_sensor_coord)
            cum_sensor_coord.append(str(temp_cumulative_sensor[-1]))
            j = 0
            for k in cum_sensor_coord:
                a = cum_sensor_coord[j].split(', ')
                a[0] = float(a[0].replace('[', ''))
                a[-1] = float(a[-1].replace(']', ''))
                last_sensor_float.append(a)
                j = j + 1
            last_sensor_coord = list(
                last_sensor_float for last_sensor_float,
                                      _ in itertools.groupby(last_sensor_float))
            temp_sensor_coord.pop(-1)
            temp_sensor_coord.pop(0)
            calculateParameters.actual_sensor_coord.append(last_sensor_coord[-1])
            calculateParameters.actual_sensor_coord = list(
                calculateParameters.actual_sensor_coord for calculateParameters.actual_sensor_coord,
                                                            _ in
                itertools.groupby(calculateParameters.actual_sensor_coord))
            calculateParameters.name_sensor.append(str(self.lineEdit.text()))
            self.listWidget_3.clear()
            for i in calculateParameters.name_sensor:
                self.listWidget_3.addItem(i + '  ' + str(
                    calculateParameters.actual_sensor_coord[calculateParameters.name_sensor.index(i)]))
            for j in reversed(range(self.horizontalLayout.count())):
                self.horizontalLayout.itemAt(j).widget().deleteLater()
            generateMap.updateSeconder(self.horizontalLayout)
            self.pushButton_0.hide()
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_4.clear()
            self.pushButton_26.setDisabled(True)
            self.pushButton_23.setEnabled(True)
        elif element_signal == 2:
            if self.radioButton.isChecked() == True:
                temp_launch_coord.append(float(self.lineEdit_2.text()))
                temp_launch_coord.append(float(self.lineEdit_4.text()))
                temp_cumulative_launch.append(temp_launch_coord)
                cum_launch_coord.append(str(temp_cumulative_launch[-1]))
                j = 0
                for k in cum_launch_coord:
                    a = cum_launch_coord[j].split(', ')
                    a[0] = float(a[0].replace('[', ''))
                    a[-1] = float(a[-1].replace(']', ''))
                    last_launch_float.append(a)
                    j = j + 1
                last_launch_coord = list(
                    last_launch_float for last_launch_float,
                                          _ in itertools.groupby(last_launch_float))
                temp_launch_coord.pop(-1)
                temp_launch_coord.pop(0)
                calculateParameters.actual_launch_coord.append(last_launch_coord[-1])
                calculateParameters.actual_launch_coord = list(
                    calculateParameters.actual_launch_coord for calculateParameters.actual_launch_coord,
                                                                _ in
                    itertools.groupby(calculateParameters.actual_launch_coord))
                calculateParameters.name_launch.append(str(self.lineEdit.text()))
                k1.append(self.lineEdit.text())
                k1.append(calculateParameters.actual_launch_coord[-1])
                k1.append('a')
                k1.append('b')
                k1.append(float(self.lineEdit_5.text()))
                k1.append(float(self.lineEdit_6.text()))
                self.listWidget_3.clear()
                self.listWidget_3.addItem(str(k1[0]))
                self.listWidget_3.addItem(str(k1[1]))
                self.listWidget_3.addItem(str(k1[4]))
                self.listWidget_3.addItem(str(k1[5]))
                for j in reversed(range(self.horizontalLayout.count())):
                    self.horizontalLayout.itemAt(j).widget().deleteLater()
                generateMap.updateLaunchMap(self.horizontalLayout)
                self.pushButton_0.hide()
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.lineEdit_4.clear()
                self.radioButton_2.setChecked(True)
                self.radioButton_2.setEnabled(True)
                self.radioButton.setDisabled(True)
                self.lineEdit_5.clear()
                self.lineEdit_6.clear()
            elif self.radioButton_2.isChecked() == True:
                temp_impact_coord.append(float(self.lineEdit_2.text()))
                temp_impact_coord.append(float(self.lineEdit_4.text()))
                temp_cumulative_impact.append(temp_impact_coord)
                cum_impact_coord.append(str(temp_cumulative_impact[-1]))
                j = 0
                for k in cum_impact_coord:
                    a = cum_impact_coord[j].split(', ')
                    a[0] = float(a[0].replace('[', ''))
                    a[-1] = float(a[-1].replace(']', ''))
                    last_impact_float.append(a)
                    j = j + 1
                last_impact_coord = list(
                    last_impact_float for last_impact_float,
                                          _ in itertools.groupby(last_impact_float))
                temp_impact_coord.pop(-1)
                temp_impact_coord.pop(0)
                calculateParameters.actual_impact_coord.append(last_impact_coord[-1])
                calculateParameters.actual_impact_coord = list(
                    calculateParameters.actual_impact_coord for calculateParameters.actual_impact_coord,
                                                                _ in
                    itertools.groupby(calculateParameters.actual_impact_coord))
                calculateParameters.name_impact.append(str(self.lineEdit.text()))
                self.listWidget_3.clear()
                k1 = k1[:(k1.index('a'))] + [self.lineEdit.text()] + k1[(k1.index('a') + 1):]
                k1 = k1[:(k1.index('b'))] + [last_impact_coord[-1]] + k1[(k1.index('b') + 1):]
                for i in k1:
                    self.listWidget_3.addItem(str(i))
                for j in reversed(range(self.horizontalLayout.count())):
                    self.horizontalLayout.itemAt(j).widget().deleteLater()
                generateMap.updateImpactMap(self.horizontalLayout)
                self.pushButton_0.hide()
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.lineEdit_4.clear()
                self.pushButton_23.setEnabled(True)
                calculateParameters.event_array = k1

    def updateMap(self):
        for i in reversed(range(self.horizontalLayout.count())):
            self.horizontalLayout.itemAt(i).widget().deleteLater()
        generateMap.createUpdatedMap(self.horizontalLayout)

    def selectLaunchImpact(self):
        if self.radioButton.isChecked() == True:
            self.lineEdit_5.setDisabled(True)
            self.lineEdit_6.setDisabled(True)
        elif self.radioButton_2.isChecked() == True:
            self.lineEdit_5.setEnabled(True)
            self.lineEdit_6.setEnabled(True)
        else:
            pass

    def lineActivity(self, text):
        if len(text) >= 1:
            if element_signal == 1:
                self.lineEdit_2.setEnabled(True)
                self.lineEdit_4.setEnabled(True)
                self.lineEdit_5.setDisabled(True)
                self.lineEdit_6.setDisabled(True)
                self.radioButton_2.setDisabled(True)
                self.radioButton.setDisabled(True)
                self.pushButton_25.setEnabled(True)
                self.pushButton_24.setDisabled(True)
                self.pushButton_23.setDisabled(True)
                self.pushButton_22.setDisabled(True)
                self.pushButton_26.setEnabled(True)
            elif element_signal == 2:
                self.lineEdit_2.setEnabled(True)
                self.lineEdit_4.setEnabled(True)
                self.lineEdit_5.setDisabled(True)
                self.lineEdit_6.setDisabled(True)
                self.pushButton_25.setDisabled(True)
                self.pushButton_24.setDisabled(True)
                self.pushButton_23.setDisabled(True)
                self.pushButton_22.setDisabled(True)
                self.pushButton_26.setEnabled(True)
            else:
                pass
        else:
            self.lineEdit_2.setDisabled(True)
            self.lineEdit_4.setDisabled(True)
            self.lineEdit_5.setDisabled(True)
            self.lineEdit_6.setDisabled(True)
            self.pushButton_25.setDisabled(True)
            self.pushButton_24.setDisabled(True)
            self.pushButton_23.setDisabled(True)
            self.pushButton_22.setDisabled(True)
            self.pushButton_26.setDisabled(True)

    def lineActivity_2(self, text):
        if len(text) >= 1:
            if element_signal == 1:
                self.lineEdit_5.setDisabled(True)
                self.lineEdit_6.setDisabled(True)
                self.radioButton_2.setDisabled(True)
                self.radioButton.setDisabled(True)
                self.pushButton_25.setEnabled(True)
                self.pushButton_24.setDisabled(True)
                self.pushButton_23.setDisabled(True)
                self.pushButton_22.setDisabled(True)
                self.pushButton_26.setDisabled(True)
            elif element_signal == 2:
                self.pushButton_24.setDisabled(True)
                self.pushButton_23.setDisabled(True)
                self.pushButton_22.setDisabled(True)
                self.pushButton_26.setDisabled(True)
                if self.radioButton_2.isChecked() == True:
                    self.pushButton_25.setEnabled(True)
                    self.lineEdit_5.setDisabled(True)
                    self.lineEdit_6.setDisabled(True)
                elif self.radioButton.isChecked() == True:
                    self.pushButton_25.setDisabled(True)
                    self.lineEdit_5.setEnabled(True)
                    self.lineEdit_6.setEnabled(True)
            else:
                pass
        else:
            self.lineEdit_5.setDisabled(True)
            self.lineEdit_6.setDisabled(True)
            self.radioButton.setDisabled(True)
            self.pushButton_25.setDisabled(True)
            self.pushButton_24.setDisabled(True)
            self.pushButton_23.setDisabled(True)
            self.pushButton_22.setDisabled(True)
            self.pushButton_26.setEnabled(True)

    def lineActivity_3(self, text):
        if len(text) >= 1:
            self.lineEdit_6.setEnabled(True)
        else:
            self.lineEdit_6.setDisabled(True)

    def lineActivity_4(self, text):
        if len(text) >= 1:
            self.pushButton_25.setEnabled(True)
        else:
            self.pushButton_25.setDisabled(True)

    def askSensorDeploymentOption(self):
        global state_1, element_signal
        element_signal = 1
        sensordeploymentoptions.showSensorDeployment()
        if sensor_option_signal == 1:
            calculateParameters.resetAll()
            self.addNewTab()
            self.lineEdit.setEnabled(True)
            self.pushButton_0.hide()
            for i in reversed(range(self.horizontalLayout.count())):
                self.horizontalLayout.itemAt(i).widget().deleteLater()
            generateMap.createMainMap(self.horizontalLayout)
            if state_1 % 2 == 0:
                self.slideOptions()
            else:
                pass
        elif sensor_option_signal == 2:
            self.lineEdit.setDisabled(True)
            try:
                self.importSensorDeployment()
            except IndexError:
                pass
        else:
            pass

    def askEventScenarioOption(self):
        global state_1, element_signal, k1
        element_signal = 2
        k1 = []
        eventscenariooptions.showEventOptions()
        self.radioButton.setChecked(True)
        self.radioButton.setEnabled(True)
        calculateParameters.resetAll()
        if event_option_signal == 1:
            self.addNewTab()
            self.lineEdit.setEnabled(True)
            self.pushButton_0.hide()
            for i in reversed(range(self.horizontalLayout.count())):
                self.horizontalLayout.itemAt(i).widget().deleteLater()
            generateMap.createMainMap(self.horizontalLayout)
            if state_1 % 2 == 0:
                self.slideOptions()
            else:
                pass
        elif event_option_signal == 2:
            self.lineEdit.setDisabled(True)
            try:
                self.importEventScenario()
            except IndexError:
                pass
        else:
            pass

    def openMapMission(self):
        calculateParameters.resetAll()
        self.pushButton_0.hide()
        self.pushButton_20.setDisabled(True)

    def finishDeployment(self):
        self.pushButton_23.setDisabled(True)
        self.pushButton_26.setDisabled(True)
        if element_signal == 1:
            with open('[sensor]' + sensor_file_name + '.txt', 'w') as f:
                f.writelines(str(calculateParameters.name_sensor) + '\n' + str(calculateParameters.actual_sensor_coord))
            sensor_file_names.append(('[sensor]' + sensor_file_name + '.txt'))
            self.clickedTab()
            self.listWidget_3.clear()
        elif element_signal == 2:
            with open('[event]' + event_file_name + '.txt', 'w') as f:
                for i in calculateParameters.event_array:
                    f.writelines(str(i) + '\n')
            event_file_names.append(('[event]' + event_file_name + '.txt'))
            self.clickedTab()
            self.listWidget_3.clear()
        else:
            pass

    def importSensorDeployment(self):
        global sensor_file_name
        calculateParameters.resetAll()
        file_filter = 'Text File (*.txt)'
        response = QFileDialog.getOpenFileName(
            parent=None,
            caption='Select a data file',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='Text File (*.txt)',
        )
        sensor_file_name = str(list(response[0].split("/"))[-1])
        sensor_file_name = str(list(sensor_file_name.split("]"))[-1])
        sensor_file_names.append(sensor_file_name)
        try:
            with open(response[0]) as f:
                lines = f.readlines()
            i = 0
            for line in lines:
                line = line.replace(']', '')
                line = line.replace('[', '')
                line = line.replace("'", '')
                line = line.replace('\n', '')
                if i == 0:
                    calculateParameters.name_sensor = list(line.split(", "))
                elif i == 1:
                    temp_s = list(line.split(", "))
                    t_s = []
                    t_ss = []
                    for s in temp_s:
                        s = float(s)
                        t_s.append(s)
                    while True:
                        t_ss.append(t_s[0])
                        t_ss.append(t_s[1])
                        calculateParameters.actual_sensor_coord.append(t_ss)
                        t_s.pop(0)
                        t_s.pop(0)
                        t_ss = []
                        if len(t_s) == 0:
                            break
                i = i + 1

            if calculateParameters.name_sensor not in imported_sensor_names:
                imported_sensor_names.append(calculateParameters.name_sensor)
            tmp = []
            for k in calculateParameters.actual_sensor_coord:
                if k not in tmp:
                    tmp.append(k)
            if tmp not in imported_sensor_coords:
                imported_sensor_coords.append(tmp)
        except FileNotFoundError:
            pass
        if len(calculateParameters.actual_sensor_coord) > 0:
            for k in calculateParameters.name_sensor:
                self.listWidget_3.addItem(
                    k + '  ' + str(calculateParameters.actual_sensor_coord[calculateParameters.name_sensor.index(k)]))
            self.addNewTab()

            for j in reversed(range(self.horizontalLayout.count())):
                self.horizontalLayout.itemAt(j).widget().deleteLater()
            generateMap.updateSeconder(self.horizontalLayout)
            self.pushButton_0.hide()
            # self.pushButton_3.setDisabled(True)
            self.pushButton_8.setEnabled(True)
        else:
            pass


    def importEventScenario(self):
        global event_file_name
        calculateParameters.resetAll()
        file_filter = 'Text File (*.txt)'
        response = QFileDialog.getOpenFileName(
            parent=None,
            caption='Select a data file',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='Text File (*.txt)'
        )
        a = []
        b = []
        c = []
        d = []
        event_file_name = str(list(response[0].split("/"))[-1])
        event_file_name = str(list(event_file_name.split("]"))[-1])
        event_file_names.append(event_file_name)
        try:
            with open(response[0]) as f:
                lines = f.read().splitlines()

            for line, i in zip(lines, range(0, len(lines))):
                if i % 9 == 1 or i % 9 == 3:
                    line = line.replace('[', '')
                    line = line.replace(']', '')
                    b = line.split(', ')
                    for j in b:
                        a.append(float(j))
                    c.append(a)
                    a = []
                    b = []

                elif i % 9 == 4 or i % 9 == 6:
                    c.append(float(line))
                elif i % 9 == 0:
                    c = []
                    c.append(line)
                else:
                    c.append(line)
                d.append(c)
            for i in d:
                if i not in calculateParameters.event_array:
                    calculateParameters.event_array.append(i)
            for k in calculateParameters.event_array:
                calculateParameters.actual_launch_coord.append(k[1])
                calculateParameters.actual_impact_coord.append(k[3])
                calculateParameters.name_launch.append(k[0])
                calculateParameters.name_impact.append(k[2])

            for j in reversed(range(self.horizontalLayout.count())):
                self.horizontalLayout.itemAt(j).widget().deleteLater()
            generateMap.updateImpactMap(self.horizontalLayout)
        except FileNotFoundError:
            pass
        if len(calculateParameters.actual_launch_coord) > 0:
            for i in calculateParameters.event_array:
                self.listWidget_3.addItem(str(i))
            self.addNewTab()
            for j in calculateParameters.event_array:
                if j not in imported_events:
                    imported_events.append(j)
            self.pushButton_0.hide()
        else:
            pass

    def slideOptions(self):
        global state_1
        if state_1 % 2 == 0:
            self.anima = QtCore.QPropertyAnimation(self.frame_3, b'geometry')
            self.anima.setDuration(500)
            self.anima.setStartValue(QtCore.QRect(-195, 160, 231, 451))
            self.anima.setEndValue(QtCore.QRect(-8, 160, 231, 451))
            self.anima.start()
            self.frame_3.show()
            state_1 = state_1 + 1
        else:
            self.anima = QtCore.QPropertyAnimation(self.frame_3, b'geometry')
            self.anima.setDuration(500)
            self.anima.setStartValue(QtCore.QRect(-9, 160, 231, 451))
            self.anima.setEndValue(QtCore.QRect(-195, 160, 231, 451))
            self.anima.start()
            self.frame_3.show()
            state_1 = state_1 + 1

    def resetAll(self):
        calculateParameters.resetAll()
        calculateParameters.joker_constant = 0
        self.pushButton_10.show()
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        # self.pushButton_3.setDisabled(True)
        self.pushButton_14.hide()
        self.label_10.hide()
        self.label_11.hide()
        self.label_12.hide()
        self.pushButton_4.setDisabled(True)
        self.pushButton_5.setDisabled(True)
        self.pushButton_19.setDisabled(True)
        self.pushButton_20.setEnabled(True)
        self.pushButton_20.show()
        self.pushButton_19.show()
        self.pushButton_10.show()
        self.pushButton_4.setDisabled(True)
        self.pushButton_5.setDisabled(True)
        self.pushButton_0.show()
        self.listWidget.show()
        self.listWidget.clear()
        generateMap.last_list.clear()
        generateMap.last_list_float.clear()
        generateMap.cumulative_coordinates.clear()
        generateMap.temp_coordinates.clear()
        generateMap.temp_cumulative.clear()
        self.lineEdit.clear()
        self.lineEdit.setDisabled(True)
        if state_1 % 2 == 1:
            self.slideOptions()
        else:
            pass
        for i in reversed(range(self.horizontalLayout.count())):
            self.horizontalLayout.itemAt(i).widget().deleteLater()
        generateMap.createMainMap(self.horizontalLayout)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Networked CASTLE MST (Mission Simulation Tool ver_0.0.1)"))
        self.pushButton.setText(_translate("MainWindow", "  Create New Sensor Deployment"))
        self.pushButton_2.setText(_translate("MainWindow", "  Create New Event Scenario"))
        self.pushButton_3.setText(_translate("MainWindow", "  Analyze Listed Scenarios"))
        self.pushButton_4.setText(_translate("MainWindow", "  Compare Deployments"))
        self.label.setText(_translate("MainWindow", "Missions to be compared"))
        self.pushButton_6.setText(_translate("MainWindow", "  Reset Mission"))
        self.pushButton_7.setText(_translate("MainWindow", "  Discard Selected"))
        self.pushButton_9.setText(_translate("MainWindow", " Add Event / Deployment"))
        self.label_3.setText(_translate("MainWindow", "Sensor Deployments Added"))
        self.label_7.setText(_translate("MainWindow", "Event Scenarios Added"))
        self.pushButton_8.setText(_translate("MainWindow", "  Edit Current Tab"))
        self.pushButton_5.setText(_translate("MainWindow", "  Animate Scenario"))
        self.pushButton_10.setText(_translate("MainWindow", ""))
        self.label_10.setText(_translate("Form", "<CLICK> this icon to mark the coordinate"))
        self.label_11.setText(_translate("Form", "After placing circle marker, please <CLICK> on the circle icon "
                                         "that is replaced into the map"))
        self.label_13.setText(
            _translate("Form", "<CLICK> this button to verify and visualize the selected coordinates"))
        self.pushButton_22.setText(_translate("MainWindow", " Save Deployment"))
        self.pushButton_23.setText(_translate("MainWindow", "Finish Deployment"))
        self.pushButton_24.setText(_translate("MainWindow", " Discard Selected"))
        self.pushButton_25.setText(_translate("MainWindow", "+"))
        self.pushButton_26.setText(_translate("MainWindow", "Select on the Map"))
        self.radioButton_2.setText(_translate("MainWindow", "Impact"))
        self.radioButton.setText(_translate("MainWindow", "Launch"))
        self.label_4.setText(_translate("MainWindow", "Assign Name:"))
        self.label_6.setText(_translate("MainWindow", "Enter Coordinate:"))
        self.label_8.setText(_translate("MainWindow", "Lat."))
        self.label_9.setText(_translate("MainWindow", "Lon."))
        self.label_14.setText(_translate("MainWindow", "Time of start:"))
        self.label_15.setText(_translate("MainWindow", "Time of flight:"))

