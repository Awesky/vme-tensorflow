# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginForm.ui'
#
# Created: Fri Aug 11 09:47:12 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(QtGui.QWidget):

    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        shadow = QtGui.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10);
        shadow.setColor(QtCore.Qt.black);
        shadow.setOffset(2);
        self.setGraphicsEffect(shadow);
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground);
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(768, 340)
        Form.setMinimumSize(QtCore.QSize(768, 340))
        Form.setMaximumSize(QtCore.QSize(768, 340))
       # Form.setStyleSheet("border-radius: 5px;")
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 751, 321))
        self.widget.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 751, 321))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget_2 = QtGui.QWidget(self.horizontalLayoutWidget)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.widget_3 = QtGui.QWidget(self.widget_2)
        self.widget_3.setGeometry(QtCore.QRect(0, 0, 371, 321))
        self.widget_3.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.label = QtGui.QLabel(self.widget_3)
        self.label.setGeometry(QtCore.QRect(150, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.widget_3)
        self.label_2.setGeometry(QtCore.QRect(50, 70, 51, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.widget_3)
        self.label_3.setGeometry(QtCore.QRect(50, 120, 51, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.nameEdit = QtGui.QLineEdit(self.widget_3)
        self.nameEdit.setGeometry(QtCore.QRect(100, 70, 211, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(16)
        self.nameEdit.setFont(font)
        self.nameEdit.setObjectName(_fromUtf8("nameEdit"))
        self.nameEdit.setPlaceholderText(u'用户名/手机号')
        self.pwdEdit = QtGui.QLineEdit(self.widget_3)
        self.pwdEdit.setGeometry(QtCore.QRect(100, 120, 211, 31))
        self.pwdEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.pwdEdit.setPlaceholderText(u'登录密码')
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(16)
        self.pwdEdit.setFont(font)
        self.pwdEdit.setObjectName(_fromUtf8("pwdEdit"))
        self.loginBtn = QtGui.QPushButton(self.widget_3)
        self.loginBtn.setGeometry(QtCore.QRect(20, 240, 321, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.loginBtn.setFont(font)
        self.loginBtn.setStyleSheet(_fromUtf8("background-color: rgb(85, 170, 255);"))
        self.loginBtn.setObjectName(_fromUtf8("loginBtn"))
        self.codeEdit = QtGui.QLineEdit(self.widget_3)
        self.codeEdit.setGeometry(QtCore.QRect(110, 170, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(16)
        self.codeEdit.setFont(font)
        self.codeEdit.setObjectName(_fromUtf8("codeEdit"))
        self.codeEdit.setPlaceholderText(u'验证码')
        self.label_4 = QtGui.QLabel(self.widget_3)
        self.label_4.setGeometry(QtCore.QRect(30, 170, 71, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.getCodeBtn = QtGui.QPushButton(self.widget_3)
        self.getCodeBtn.setGeometry(QtCore.QRect(240, 170, 75, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(16)
        self.getCodeBtn.setFont(font)
        self.getCodeBtn.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 127);"))
        self.getCodeBtn.setObjectName(_fromUtf8("getCodeBtn"))
        self.remCheckBox = QtGui.QCheckBox(self.widget_3)
        self.remCheckBox.setGeometry(QtCore.QRect(30, 210, 101, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(14)
        self.remCheckBox.setFont(font)
        self.remCheckBox.setObjectName(_fromUtf8("remCheckBox"))
        self.msgTip = QtGui.QLabel(self.widget_3)
        self.msgTip.setGeometry(QtCore.QRect(63, 290, 261, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(12)
        self.msgTip.setFont(font)
        self.msgTip.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.msgTip.setObjectName(_fromUtf8("msgTip"))
        self.widget_4 = QtGui.QWidget(self.widget_2)
        self.widget_4.setGeometry(QtCore.QRect(370, 0, 381, 321))
        self.widget_4.setStyleSheet(_fromUtf8("background-image: url(:/img/image-3.jpg);"))
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.exitBtn = QtGui.QPushButton(self.widget_4)
        self.exitBtn.setGeometry(QtCore.QRect(352, 0, 28, 28))
        self.exitBtn.setMinimumSize(QtCore.QSize(28, 28))
        self.exitBtn.setMaximumSize(QtCore.QSize(28, 28))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.exitBtn.setFont(font)
        self.exitBtn.setStyleSheet(_fromUtf8("font: 75 18pt \"Agency FB\";\n"
"background-color: rgb(0, 255, 255);\n"
"color: rgb(255, 0, 0);"))
        self.exitBtn.setIconSize(QtCore.QSize(38, 38))
        self.exitBtn.setObjectName(_fromUtf8("exitBtn"))
        self.minBtn = QtGui.QPushButton(self.widget_4)
        self.minBtn.setGeometry(QtCore.QRect(325, 0, 28, 28))
        self.minBtn.setMinimumSize(QtCore.QSize(25, 25))
        self.minBtn.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.minBtn.setFont(font)
        self.minBtn.setStyleSheet(_fromUtf8("font: 75 18pt \"Agency FB\";\n"
"background-color: rgb(0, 255, 255);\n"
"color: rgb(255, 0, 0);"))
        self.minBtn.setIconSize(QtCore.QSize(38, 38))
        self.minBtn.setObjectName(_fromUtf8("minBtn"))
        self.horizontalLayout.addWidget(self.widget_2)
        self.exitBtn.clicked.connect(self.exit_clicked)
        self.minBtn.clicked.connect(self.showmin_clicked)
        self.z = QtCore.QPoint()
        self.timer = QtCore.QTimer(self)  # 初始化一个定时器
        self.timer.timeout.connect(self.flashImage)  # 计时结束调用operate()方法
        self.timer.start(5000)  # 设置计时间隔并启动
        self.k = 0
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Helper", None))
        self.label.setText(_translate("Form", "登  录", None))
        self.label_2.setText(_translate("Form", "账号:", None))
        self.label_3.setText(_translate("Form", "密码:", None))
        self.loginBtn.setText(_translate("Form", "立 即 登 录", None))
        self.label_4.setText(_translate("Form", "验证码:", None))
        self.getCodeBtn.setText(_translate("Form", "获取", None))
        self.remCheckBox.setText(_translate("Form", "记住登录", None))
        self.msgTip.setText(_translate("Form", "账号或密码错误!", None))
        self.exitBtn.setText(_translate("Form", "×", None))
        self.minBtn.setText(_translate("Form", "-", None))

    def flashImage(self):

        if self.k == 0:
            self.widget_4.setStyleSheet(_fromUtf8("background-image: url(:/img/image-1.jpg);"))
            self.k = 1
        else:
            self.widget_4.setStyleSheet(_fromUtf8("background-image: url(:/img/image-3.jpg);"))
            self.k = 0

    def exit_clicked(self):
        self.close()

    def showmin_clicked(self):
        self.showMinimized()

    def mouseMoveEvent(self, QMouseEvent):
        if self.z == QtCore.QPoint(): return
        y = QMouseEvent.globalPos()
        x = y - self.z
        self.move(x)

    def mousePressEvent(self, QMouseEvent):
        #鼠标相对于桌面左上角的位置
        y = QMouseEvent.globalPos()
        #窗口左上角相对于桌面左上角的位置
        x = self.geometry().topLeft()
        #z为定值
        self.z = y - x

    def mouseReleaseEvent(self, QMouseEvent):
        self.z = QtCore.QPoint()

#import res
