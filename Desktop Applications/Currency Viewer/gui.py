# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowOpacity(0.95)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowIcon(QtGui.QIcon('img/icon.png'))
        Form.resize(372, 259)
        Form.setMinimumSize(372, 259)
        Form.setMaximumSize(372, 259)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setStyleSheet("background:gray;\n"
"color:black;")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(18, 50, 60, 50))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/dollar.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 123, 50, 50))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("img/euro.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(130, 10, 67, 17))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(280, 10, 67, 17))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 190, 50, 60))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("img/gold.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.exit_but = QtWidgets.QPushButton(Form)
        self.exit_but.setGeometry(QtCore.QRect(20, 10, 51, 17))
        self.exit_but.setStyleSheet("background:white;\n"
"border-radius:5px;")
        self.exit_but.setText("x")
        self.exit_but.setObjectName("exit_but")
        self.dollar_buying = QtWidgets.QLabel(Form)
        self.dollar_buying.setGeometry(QtCore.QRect(130, 68, 67, 17))
        self.dollar_buying.setStyleSheet("color:white;")
        self.dollar_buying.setText("")
        self.dollar_buying.setAlignment(QtCore.Qt.AlignCenter)
        self.dollar_buying.setObjectName("dollar_buying")
        self.euro_buying = QtWidgets.QLabel(Form)
        self.euro_buying.setGeometry(QtCore.QRect(130, 140, 67, 17))
        self.euro_buying.setStyleSheet("color:white;")
        self.euro_buying.setText("")
        self.euro_buying.setAlignment(QtCore.Qt.AlignCenter)
        self.euro_buying.setObjectName("euro_buying")
        self.gold_buying = QtWidgets.QLabel(Form)
        self.gold_buying.setGeometry(QtCore.QRect(130, 210, 67, 17))
        self.gold_buying.setStyleSheet("color:white;")
        self.gold_buying.setText("")
        self.gold_buying.setAlignment(QtCore.Qt.AlignCenter)
        self.gold_buying.setObjectName("gold_buying")
        self.dollar_change = QtWidgets.QLabel(Form)
        self.dollar_change.setGeometry(QtCore.QRect(280, 68, 67, 17))
        self.dollar_change.setStyleSheet("color:white;")
        self.dollar_change.setText("")
        self.dollar_change.setAlignment(QtCore.Qt.AlignCenter)
        self.dollar_change.setObjectName("dollar_change")
        self.euro_change = QtWidgets.QLabel(Form)
        self.euro_change.setGeometry(QtCore.QRect(280, 140, 67, 17))
        self.euro_change.setStyleSheet("color:white;")
        self.euro_change.setText("")
        self.euro_change.setAlignment(QtCore.Qt.AlignCenter)
        self.euro_change.setObjectName("euro_change")
        self.gold_change = QtWidgets.QLabel(Form)
        self.gold_change.setGeometry(QtCore.QRect(280, 210, 67, 17))
        self.gold_change.setStyleSheet("color:white;")
        self.gold_change.setText("")
        self.gold_change.setAlignment(QtCore.Qt.AlignCenter)
        self.gold_change.setObjectName("gold_change")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ata Currency"))
        self.label_3.setText(_translate("Form", "value"))
        self.label_4.setText(_translate("Form", "change"))


    def center(self):
            qr = self.frameGeometry()
            cp = QtWidgets.QDesktopWidget().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QtCore.QPoint(event.globalPos() - self.oldPos)
        #print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()