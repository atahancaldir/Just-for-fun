# -*- coding: utf-8 -*-

#Alternatif Çözüm Takımı - Alternatif Bank Hackathon Yarışması

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1092, 582)
        Form.setMinimumSize(QtCore.QSize(1092, 582))
        Form.setMaximumSize(QtCore.QSize(1092, 582))
        Form.setStyleSheet("background:#CACEC7;")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 0, 391, 241))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("/home/atahan/Desktop/Hackathon/Python/logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.paraTutari = QtWidgets.QLineEdit(Form)
        self.paraTutari.setGeometry(QtCore.QRect(60, 230, 421, 91))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setItalic(True)
        self.paraTutari.setFont(font)
        self.paraTutari.setStyleSheet("background:white;")
        self.paraTutari.setText("")
        self.paraTutari.setObjectName("paraTutari")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(500, 250, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(34)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.odemeAl = QtWidgets.QPushButton(Form)
        self.odemeAl.setGeometry(QtCore.QRect(610, 230, 391, 91))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setItalic(True)
        self.odemeAl.setFont(font)
        self.odemeAl.setStyleSheet("background:#81C641;\n"
"color:white;")
        self.odemeAl.setObjectName("odemeAl")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(870, 30, 161, 161))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("/home/atahan/Desktop/Hackathon/Python/temassiz.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(260, 380, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.kartDurumu = QtWidgets.QLabel(Form)
        self.kartDurumu.setGeometry(QtCore.QRect(490, 380, 531, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setItalic(True)
        self.kartDurumu.setFont(font)
        self.kartDurumu.setObjectName("kartDurumu")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 460, 550, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background:orange;\n"
"color:white;\n"
"border-radius:25px;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(560, 460, 510, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background:orange;\n"
"color:white;\n"
"border-radius:25px;")
        self.label_6.setObjectName("label_6")
        self.sure = QtWidgets.QLCDNumber(Form)
        self.sure.setGeometry(QtCore.QRect(510, 460, 70, 61))
        self.sure.setStyleSheet("background:orange;\n"
"color:white;"
"border-radius:0px;")
        self.sure.setObjectName("sure")
        self.sure.setDigitCount(2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Alternatif POS"))
        self.paraTutari.setPlaceholderText(_translate("Form", "Para Tutarı"))
        self.label_2.setText(_translate("Form", "₺"))
        self.odemeAl.setText(_translate("Form", "Ödeme Al"))
        self.label_4.setText(_translate("Form", "Kart Durumu:"))
        self.kartDurumu.setText(_translate("Form", "İşlem Bekleniyor"))
        self.label_5.setText(_translate("Form", " Lütfen onaylamak için kartınızı "))
        self.label_6.setText(_translate("Form", "     saniye içinde tekrar gösteriniz"))
        self.sure.display(10)
