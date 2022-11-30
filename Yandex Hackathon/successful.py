# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'successful.ui'
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
        self.label.setMinimumSize(QtCore.QSize(463, 901))
        self.label.setMaximumSize(QtCore.QSize(463, 901))
        self.label.setStyleSheet("backgruo")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/phone.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.shareFrame = QtWidgets.QFrame(MAIN)
        self.shareFrame.setGeometry(QtCore.QRect(31, 58, 401, 772))
        self.shareFrame.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.0738636 #205AFF, stop:0.840909 #1180FF);")
        self.shareFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.shareFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.shareFrame.setObjectName("shareFrame")
        self.successFrame = QtWidgets.QFrame(self.shareFrame)
        self.successFrame.setGeometry(QtCore.QRect(95, 240, 211, 211))
        self.successFrame.setStyleSheet("background:white;\n"
"border-radius:25px;")
        self.successFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.successFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.successFrame.setObjectName("successFrame")
        self.successImg = QtWidgets.QLabel(self.successFrame)
        self.successImg.setGeometry(QtCore.QRect(30, 30, 150, 150))
        self.successImg.setText("")
        self.successImg.setPixmap(QtGui.QPixmap("img/tick.png"))
        self.successImg.setScaledContents(True)
        self.successImg.setObjectName("successImg")
        self.successLabel = QtWidgets.QLabel(self.successFrame)
        self.successLabel.setGeometry(QtCore.QRect(50, 180, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.successLabel.setFont(font)
        self.successLabel.setObjectName("successLabel")
        self.successBackBut = QtWidgets.QPushButton(self.successFrame)
        self.successBackBut.setGeometry(QtCore.QRect(170, 10, 25, 25))
        self.successBackBut.setStyleSheet("color:white;\n"
"background:red;\n"
"border-radius:12px;")
        self.successBackBut.setText("")
        self.successBackBut.setObjectName("successBackBut")

        self.retranslateUi(MAIN)
        QtCore.QMetaObject.connectSlotsByName(MAIN)

    def retranslateUi(self, MAIN):
        _translate = QtCore.QCoreApplication.translate
        MAIN.setWindowTitle(_translate("MAIN", "Apollo"))
        self.successLabel.setText(_translate("MAIN", "Music shared!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MAIN = QtWidgets.QWidget()
    ui = Ui_MAIN()
    ui.setupUi(MAIN)
    MAIN.show()
    sys.exit(app.exec_())

