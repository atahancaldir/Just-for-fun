# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MAIN(object):
    def setupUi(self, MAIN):
        MAIN.setObjectName("MAIN")
        MAIN.resize(468, 887)
        MAIN.setMinimumSize(QtCore.QSize(468, 887))
        MAIN.setMaximumSize(QtCore.QSize(468, 887))
        self.label = QtWidgets.QLabel(MAIN)
        self.label.setGeometry(QtCore.QRect(0, 0, 463, 901))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/phone.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(MAIN)
        self.widget.setGeometry(QtCore.QRect(31, 60, 401, 771))
        self.widget.setStyleSheet("background:white;")
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(100, 100, 200, 291))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("img/icon.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(0, 400, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.username = QtWidgets.QLineEdit(self.widget)
        self.username.setGeometry(QtCore.QRect(80, 500, 270, 30))
        self.username.setStyleSheet("border:1px solid #53bde0;")
        self.username.setAlignment(QtCore.Qt.AlignCenter)
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setGeometry(QtCore.QRect(80, 550, 270, 30))
        self.password.setStyleSheet("border:1px solid #53bde0;")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setObjectName("password")
        self.loginBut = QtWidgets.QPushButton(self.widget)
        self.loginBut.setGeometry(QtCore.QRect(50, 600, 300, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.loginBut.setFont(font)
        self.loginBut.setStyleSheet("border:0px;\n"
"background:#4be37b;\n"
"border-radius:17px;\n"
"color:white;")
        self.loginBut.setObjectName("loginBut")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(50, 500, 30, 30))
        self.label_4.setStyleSheet("background:#53bde0;\n"
"border:3px solid #53bde0;")
        self.label_4.setText("")
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setPixmap(QtGui.QPixmap("img/user.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(50, 550, 30, 30))
        self.label_5.setStyleSheet("background:#53bde0;\n"
"border:3px solid #53bde0;")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("img/password.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(90, 640, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(240, 638, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setUnderline(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(195, 430, 71, 31))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("img/yandex_PNG20.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")

        self.retranslateUi(MAIN)
        QtCore.QMetaObject.connectSlotsByName(MAIN)

    def retranslateUi(self, MAIN):
        _translate = QtCore.QCoreApplication.translate
        MAIN.setWindowTitle(_translate("MAIN", "Apollo"))
        self.label_3.setText(_translate("MAIN", "A P O L L O"))
        self.username.setPlaceholderText(_translate("MAIN", "Username"))
        self.password.setPlaceholderText(_translate("MAIN", "Password"))
        self.loginBut.setText(_translate("MAIN", "Log In"))
        self.label_6.setText(_translate("MAIN", "Don\'t have an account?"))
        self.label_7.setText(_translate("MAIN", "Sign Up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MAIN = QtWidgets.QWidget()
    ui = Ui_MAIN()
    ui.setupUi(MAIN)
    MAIN.show()
    sys.exit(app.exec_())

