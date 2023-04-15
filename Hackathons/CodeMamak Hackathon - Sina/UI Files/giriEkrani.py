# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'girisEkrani.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_musteriEkrani(object):
    def setupUi(self, musteriEkrani):
        musteriEkrani.setObjectName("musteriEkrani")
        musteriEkrani.resize(943, 487)
        musteriEkrani.setStyleSheet("background:#67baea;")
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    musteriEkrani = QtWidgets.QWidget()
    ui = Ui_musteriEkrani()
    ui.setupUi(musteriEkrani)
    musteriEkrani.show()
    sys.exit(app.exec_())

