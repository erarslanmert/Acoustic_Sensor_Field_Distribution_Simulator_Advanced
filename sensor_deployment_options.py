from PyQt5 import QtCore, QtGui, QtWidgets
import mainWindow


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(288, 217)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-120, 170, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 70, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(40, 120, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setToolTipDuration(2)
        self.radioButton.setStatusTip("")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(40, 140, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setToolTipDuration(2)
        self.radioButton_3.setStatusTip("")
        self.radioButton_3.setObjectName("radioButton_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(40, 40, 211, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")

        self.buttonBox.setDisabled(True)
        self.radioButton.setDisabled(True)
        self.retranslateUi(Dialog)

        self.radioButton.toggled.connect(self.statusButtonBox)
        self.radioButton_3.toggled.connect(self.statusButtonBox)
        self.buttonBox.accepted.connect(self.openSensorDeployment)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.lineEdit.textChanged.connect(self.lineActive)

    def statusButtonBox(self):
        self.buttonBox.setEnabled(True)

    def lineActive(self, text):
        if len(text) >= 1:
            self.radioButton.setEnabled(True)
            self.radioButton_3.setDisabled(True)
            if self.radioButton.isChecked()==True:
                self.buttonBox.setEnabled(True)
            else:
                self.radioButton.setChecked(True)
                pass
        else:
            self.radioButton.setDisabled(True)
            self.radioButton_3.setEnabled(True)
            self.radioButton_3.setChecked(True)
            self.buttonBox.setEnabled(True)

    def openSensorDeployment(self):
        if self.radioButton.isChecked() == True:
            mainWindow.sensor_option_signal = 1
            mainWindow.sensor_file_name = str(self.lineEdit.text())
        elif self.radioButton_3.isChecked() == True:
            mainWindow.sensor_option_signal = 2
        else:
            mainWindow.sensor_option_signal = 0

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sensor Deployment Options"))
        self.label.setText(_translate("Dialog", "Please select an option to create sensor post deployment configuration!"))
        self.radioButton.setText(_translate("Dialog", "Create custom deployment"))
        self.radioButton_3.setText(_translate("Dialog", "Import from directory"))
        self.label_2.setText(_translate("Dialog","Enter Deployment Name"))

def showSensorDeployment():
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    Dialog.exec_()
