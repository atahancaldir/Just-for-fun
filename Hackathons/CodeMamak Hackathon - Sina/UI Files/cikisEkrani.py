# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cikisEkrani.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_cikisEkrani(object):
    def setupUi(self, cikisEkrani):
        cikisEkrani.setObjectName("cikisEkrani")
        cikisEkrani.resize(763, 285)
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
        self.label.setText(_translate("cikisEkrani", "Çıkış yapmak için lütfen T.C. Kimlik Numaranızı giriniz"))
        self.pushButton.setText(_translate("cikisEkrani", "Çıkış yap"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cikisEkrani = QtWidgets.QWidget()
    ui = Ui_cikisEkrani()
    ui.setupUi(cikisEkrani)
    cikisEkrani.show()
    sys.exit(app.exec_())

