# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uyariMesaji.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_uyariMesaji(object):
    def setupUi(self, uyariMesaji):
        uyariMesaji.setObjectName("uyariMesaji")
        uyariMesaji.resize(999, 264)
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    uyariMesaji = QtWidgets.QWidget()
    ui = Ui_uyariMesaji()
    ui.setupUi(uyariMesaji)
    uyariMesaji.show()
    sys.exit(app.exec_())

