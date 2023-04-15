# -*- coding: utf-8 -*-

# HoldMyRover takımı tarafından CodeMamak Hackathon'u için oluşturuldu!
# 17.05.2020

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_musteriEkrani(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, musteriEkrani):
        musteriEkrani.setObjectName("musteriEkrani")
        musteriEkrani.resize(943, 487)
        musteriEkrani.setMinimumSize(QtCore.QSize(943, 487))
        musteriEkrani.setMaximumSize(QtCore.QSize(943, 487))
        musteriEkrani.setStyleSheet("background:#492fb8;")
        self.label = QtWidgets.QLabel(musteriEkrani)
        self.label.setGeometry(QtCore.QRect(240, 20, 511, 131))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Serif")
        font.setPointSize(72)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(musteriEkrani)
        self.label_2.setGeometry(QtCore.QRect(420, 140, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("color:white;")
        self.girisBut = QtWidgets.QPushButton(musteriEkrani)
        self.girisBut.setGeometry(QtCore.QRect(340, 210, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setItalic(True)
        self.girisBut.setFont(font)
        self.girisBut.setStyleSheet("background:#edd080;\n"
"border-radius:20px;")
        self.girisBut.setObjectName("girisBut")
        self.cikisBut = QtWidgets.QPushButton(musteriEkrani)
        self.cikisBut.setGeometry(QtCore.QRect(340, 310, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setItalic(True)
        self.cikisBut.setFont(font)
        self.cikisBut.setStyleSheet("background:#edd080;\n"
"border-radius:20px;")
        self.cikisBut.setObjectName("cikisBut")
        self.label_3 = QtWidgets.QLabel(musteriEkrani)
        self.label_3.setGeometry(QtCore.QRect(740, 290, 181, 181))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("mamak.png"))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(musteriEkrani)
        QtCore.QMetaObject.connectSlotsByName(musteriEkrani)

    def retranslateUi(self, musteriEkrani):
        _translate = QtCore.QCoreApplication.translate
        musteriEkrani.setWindowTitle(_translate("musteriEkrani", "Müşteri Giriş Ekranı"))
        self.label.setText(_translate("musteriEkrani", "Merhaba"))
        self.label_2.setText(_translate("musteriEkrani", "Cafe24"))
        self.girisBut.setText(_translate("musteriEkrani", "Giriş"))
        self.cikisBut.setText(_translate("musteriEkrani", "Çıkış"))


class Ui_masaSecimEkrani(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, masaSecimEkrani):
        masaSecimEkrani.setObjectName("masaSecimEkrani")
        masaSecimEkrani.resize(760, 815)
        masaSecimEkrani.setMinimumSize(QtCore.QSize(760, 815))
        masaSecimEkrani.setMaximumSize(QtCore.QSize(760, 815))
        masaSecimEkrani.setStyleSheet("background:#492fb8;")
        self.lineEdit = QtWidgets.QLineEdit(masaSecimEkrani)
        self.lineEdit.setGeometry(QtCore.QRect(40, 70, 421, 41))
        self.lineEdit.setStyleSheet("background:white;\n"
"border-radius:20px;")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(masaSecimEkrani)
        self.label.setGeometry(QtCore.QRect(50, 20, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.tcOnay = QtWidgets.QPushButton(masaSecimEkrani)
        self.tcOnay.setGeometry(QtCore.QRect(160, 120, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(True)
        self.tcOnay.setFont(font)
        self.tcOnay.setStyleSheet("background:#32cf3c;\n"
"color:white;\n"
"border-radius:20px;")
        self.tcOnay.setObjectName("tcOnay")
        self.cafeFrame = QtWidgets.QFrame(masaSecimEkrani)
        self.cafeFrame.setGeometry(QtCore.QRect(30, 260, 701, 541))
        self.cafeFrame.setStyleSheet("background:white;")
        self.cafeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cafeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cafeFrame.setObjectName("cafeFrame")
        self.cafeFrame.setEnabled(False)
        self.masa1 = QtWidgets.QPushButton(self.cafeFrame)
        self.masa1.setGeometry(QtCore.QRect(40, 50, 131, 71))
        self.masa1.setStyleSheet("background:#592b27;\n"
"color:white;")
        self.masa1.setObjectName("masa1")
        self.label_3 = QtWidgets.QLabel(self.cafeFrame)
        self.label_3.setGeometry(QtCore.QRect(20, 280, 21, 131))
        self.label_3.setStyleSheet("background:#67baea;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.cafeFrame)
        self.label_4.setGeometry(QtCore.QRect(50, 340, 31, 17))
        self.label_4.setObjectName("label_4")
        self.masa5 = QtWidgets.QPushButton(self.cafeFrame)
        self.masa5.setGeometry(QtCore.QRect(40, 160, 131, 71))
        self.masa5.setStyleSheet("background:#592b27;\n"
"color:white;")
        self.masa5.setObjectName("masa5")
        self.masa2 = QtWidgets.QPushButton(self.cafeFrame)
        self.masa2.setGeometry(QtCore.QRect(210, 50, 131, 71))
        self.masa2.setStyleSheet("background:#592b27;\n"
"color:white;")
        self.masa2.setObjectName("masa2")
        self.masa6 = QtWidgets.QPushButton(self.cafeFrame)
        self.masa6.setGeometry(QtCore.QRect(210, 160, 131, 71))
        self.masa6.setStyleSheet("background:#592b27;\n"
"color:white;")
        self.masa6.setObjectName("masa6")
        self.masa4 = QtWidgets.QPushButton(self.cafeFrame)
        self.masa4.setGeometry(QtCore.QRect(540, 50, 131, 71))
        self.masa4.setStyleSheet("background:#592b27;\n"
"color:white;")
        self.masa4.setObjectName("masa4")
        self.masa9 = QtWidgets.QPushButton(self.cafeFrame)
        self.masa9.setGeometry(QtCore.QRect(390, 370, 131, 71))
        self.masa9.setStyleSheet("background:#592b27;\n"
"color:white;")
        self.masa9.setObjectName("masa9")
        self.masa11 = QtWidgets.QPushButton(self.cafeFrame)
        self.masa11.setGeometry(QtCore.QRect(390, 460, 131, 71))
        self.masa11.setStyleSheet("background:#592b27;\n"
"color:white;")
        self.masa11.setObjectName("masa11")
        self.label_5 = QtWidgets.QLabel(self.cafeFrame)
        self.label_5.setGeometry(QtCore.QRect(70, 430, 281, 91))
        self.label_5.setStyleSheet("background:#67baea;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.masa3 = QtWidgets.QPushButton(self.cafeFrame)
        self.masa3.setGeometry(QtCore.QRect(390, 50, 131, 71))
        self.masa3.setStyleSheet("background:#592b27;\n"
"color:white;")
        self.masa3.setObjectName("masa3")
        self.masa7 = QtWidgets.QPushButton(self.cafeFrame)
        self.masa7.setGeometry(QtCore.QRect(390, 160, 131, 71))
        self.masa7.setStyleSheet("background:#592b27;\n"
"color:white;")
        self.masa7.setObjectName("masa7")
        self.masa10 = QtWidgets.QPushButton(self.cafeFrame)
        self.masa10.setGeometry(QtCore.QRect(540, 370, 131, 71))
        self.masa10.setStyleSheet("background:#592b27;\n"
"color:white;")
        self.masa10.setObjectName("masa10")
        self.masa12 = QtWidgets.QPushButton(self.cafeFrame)
        self.masa12.setGeometry(QtCore.QRect(540, 460, 131, 71))
        self.masa12.setStyleSheet("background:#592b27;\n"
"color:white;")
        self.masa12.setObjectName("masa12")
        self.label_6 = QtWidgets.QLabel(self.cafeFrame)
        self.label_6.setGeometry(QtCore.QRect(651, 250, 20, 91))
        self.label_6.setStyleSheet("background:#67baea;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.cafeFrame)
        self.label_2.setGeometry(QtCore.QRect(590, 280, 51, 17))
        self.label_2.setObjectName("label_2")
        self.masa8 = QtWidgets.QPushButton(self.cafeFrame)
        self.masa8.setGeometry(QtCore.QRect(540, 160, 131, 71))
        self.masa8.setStyleSheet("background:#592b27;\n"
"color:white;")
        self.masa8.setObjectName("masa8")
        self.label_8 = QtWidgets.QLabel(self.cafeFrame)
        self.label_8.setGeometry(QtCore.QRect(196, 410, 41, 20))
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(masaSecimEkrani)
        self.label_7.setGeometry(QtCore.QRect(550, 20, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:white;")
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(masaSecimEkrani)
        self.label_9.setGeometry(QtCore.QRect(190, 210, 401, 31))
        self.label_9.hide()
        font = QtGui.QFont()
        font.setFamily("Lohit Punjabi")
        font.setPointSize(14)
        font.setItalic(False)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:black;")
        self.label_9.setObjectName("label_9")
        self.pushButton_2 = QtWidgets.QPushButton(masaSecimEkrani)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 70, 125, 125))
        self.pushButton_2.setStyleSheet("background:white;\n"
"border-radius:60px;")
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("temassizresim.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(207, 207))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(masaSecimEkrani)
        QtCore.QMetaObject.connectSlotsByName(masaSecimEkrani)

    def retranslateUi(self, masaSecimEkrani):
        _translate = QtCore.QCoreApplication.translate
        masaSecimEkrani.setWindowTitle(_translate("masaSecimEkrani", "Masa Seçim Ekranı"))
        self.label.setText(_translate("masaSecimEkrani", "Lütfen T.C. kimlik numaranızı giriniz"))
        self.tcOnay.setText(_translate("masaSecimEkrani", "Giriş yap!"))
        self.masa1.setText(_translate("masaSecimEkrani", "Masa 1"))
        self.label_4.setText(_translate("masaSecimEkrani", "Giriş"))
        self.masa5.setText(_translate("masaSecimEkrani", "Masa 5"))
        self.masa2.setText(_translate("masaSecimEkrani", "Masa 2"))
        self.masa6.setText(_translate("masaSecimEkrani", "Masa 6"))
        self.masa4.setText(_translate("masaSecimEkrani", "Masa 4"))
        self.masa9.setText(_translate("masaSecimEkrani", "Masa 9"))
        self.masa11.setText(_translate("masaSecimEkrani", "Masa 11"))
        self.masa3.setText(_translate("masaSecimEkrani", "Masa 3"))
        self.masa7.setText(_translate("masaSecimEkrani", "Masa 7"))
        self.masa10.setText(_translate("masaSecimEkrani", "Masa 10"))
        self.masa12.setText(_translate("masaSecimEkrani", "Masa 12"))
        self.label_2.setText(_translate("masaSecimEkrani", "Lavabo"))
        self.masa8.setText(_translate("masaSecimEkrani", "Masa 8"))
        self.label_8.setText(_translate("masaSecimEkrani", "Kasa"))
        self.label_7.setText(_translate("masaSecimEkrani", "Temassız giriş"))
        self.label_9.setText(_translate("masaSecimEkrani", "Lütfen oturmak istediğiniz masayı seçiniz"))


class Ui_uyariMesaji(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, uyariMesaji):
        uyariMesaji.setObjectName("uyariMesaji")
        uyariMesaji.resize(999, 264)
        uyariMesaji.setMinimumSize(QtCore.QSize(999, 264))
        uyariMesaji.setMaximumSize(QtCore.QSize(999, 264))
        uyariMesaji.setStyleSheet("background:#67baea;")
        self.label = QtWidgets.QLabel(uyariMesaji)
        self.label.setGeometry(QtCore.QRect(340, 10, 71, 151))
        font = QtGui.QFont()
        font.setPointSize(120)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#cf4d42;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(uyariMesaji)
        self.label_2.setGeometry(QtCore.QRect(410, 20, 271, 111))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:#cf4d42;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(uyariMesaji)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 961, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(uyariMesaji)
        QtCore.QMetaObject.connectSlotsByName(uyariMesaji)

    def retranslateUi(self, uyariMesaji):
        _translate = QtCore.QCoreApplication.translate
        uyariMesaji.setWindowTitle(_translate("uyariMesaji", "Uyarı Mesajı"))
        self.label.setText(_translate("uyariMesaji", "!"))
        self.label_2.setText(_translate("uyariMesaji", "Uyarı"))
        self.label_3.setText(_translate("uyariMesaji", "Hastalık tespiti yapılan kişiler sosyal mesafe kuralları gereğince kalabalık ortamlara giremezler"))

class Ui_bilgiMesaji(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Ui_bilgiMesaji):
        Ui_bilgiMesaji.setObjectName("Ui_bilgiMesaji")
        Ui_bilgiMesaji.resize(999, 264)
        Ui_bilgiMesaji.setMinimumSize(QtCore.QSize(999, 264))
        Ui_bilgiMesaji.setMaximumSize(QtCore.QSize(999, 264))
        Ui_bilgiMesaji.setStyleSheet("background:#67baea;")
        self.label_2 = QtWidgets.QLabel(Ui_bilgiMesaji)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 779, 111))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:#492fb8;")
        self.label_2.setObjectName("label_2")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3 = QtWidgets.QLabel(Ui_bilgiMesaji)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 779, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)

        self.retranslateUi(Ui_bilgiMesaji)
        QtCore.QMetaObject.connectSlotsByName(Ui_bilgiMesaji)

    def retranslateUi(self, Ui_bilgiMesaji):
        _translate = QtCore.QCoreApplication.translate
        Ui_bilgiMesaji.setWindowTitle(_translate("Ui_bilgiMesaji", "Bilgilendirme Mesajı"))
        self.label_2.setText(_translate("Ui_bilgiMesaji", "Bilgilendirme"))
        self.label_3.setText(_translate("Ui_bilgiMesaji", ""))


class Ui_cikisEkrani(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, cikisEkrani):
        cikisEkrani.setObjectName("cikisEkrani")
        cikisEkrani.resize(763, 285)
        cikisEkrani.setMinimumSize(QtCore.QSize(763, 285))
        cikisEkrani.setMaximumSize(QtCore.QSize(763, 285))
        cikisEkrani.setStyleSheet("background:#492fb8;")
        self.label = QtWidgets.QLabel(cikisEkrani)
        self.label.setGeometry(QtCore.QRect(90, 30, 571, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(cikisEkrani)
        self.lineEdit.setGeometry(QtCore.QRect(50, 90, 661, 51))
        self.lineEdit.setStyleSheet("background:white;\n"
"border-radius:20px;")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(cikisEkrani)
        self.pushButton.setGeometry(QtCore.QRect(280, 170, 191, 61))
        self.pushButton.setStyleSheet("color:white;\n"
"background:red;\n"
"border-radius:15px;")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(cikisEkrani)
        QtCore.QMetaObject.connectSlotsByName(cikisEkrani)

    def retranslateUi(self, cikisEkrani):
        _translate = QtCore.QCoreApplication.translate
        cikisEkrani.setWindowTitle(_translate("cikisEkrani", "Çıkış Ekranı"))
        self.label.setText(_translate("cikisEkrani", "Çıkış yapmak için lütfen T.C. kimlik numaranızı giriniz"))
        self.pushButton.setText(_translate("cikisEkrani", "Çıkış yap"))