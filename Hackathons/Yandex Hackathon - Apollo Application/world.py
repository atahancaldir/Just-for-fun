# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'world.ui'
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
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/phone.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.worldFrame = QtWidgets.QFrame(MAIN)
        self.worldFrame.setGeometry(QtCore.QRect(31, 58, 401, 772))
        self.worldFrame.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.0738636 #205AFF, stop:0.840909 #1180FF);")
        self.worldFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.worldFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.worldFrame.setObjectName("worldFrame")
        self.worldBackBut = QtWidgets.QPushButton(self.worldFrame)
        self.worldBackBut.setGeometry(QtCore.QRect(20, 20, 40, 40))
        self.worldBackBut.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.worldBackBut.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.worldBackBut.setIcon(icon)
        self.worldBackBut.setIconSize(QtCore.QSize(30, 30))
        self.worldBackBut.setObjectName("worldBackBut")
        self.worldTopLabel = QtWidgets.QLabel(self.worldFrame)
        self.worldTopLabel.setGeometry(QtCore.QRect(0, 30, 401, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.worldTopLabel.setFont(font)
        self.worldTopLabel.setStyleSheet("background: rgb(0,0,0,0);\n"
"color:white;")
        self.worldTopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.worldTopLabel.setObjectName("worldTopLabel")
        self.worldImage = QtWidgets.QLabel(self.worldFrame)
        self.worldImage.setGeometry(QtCore.QRect(0, 70, 401, 701))
        self.worldImage.setText("")
        self.worldImage.setPixmap(QtGui.QPixmap("img/gps2.png"))
        self.worldImage.setScaledContents(True)
        self.worldImage.setObjectName("worldImage")
        self.worldTopLabel.raise_()
        self.worldBackBut.raise_()
        self.worldImage.raise_()

        self.retranslateUi(MAIN)
        QtCore.QMetaObject.connectSlotsByName(MAIN)

    def retranslateUi(self, MAIN):
        _translate = QtCore.QCoreApplication.translate
        MAIN.setWindowTitle(_translate("MAIN", "Apollo"))
        self.worldTopLabel.setText(_translate("MAIN", "Discover"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MAIN = QtWidgets.QWidget()
    ui = Ui_MAIN()
    ui.setupUi(MAIN)
    MAIN.show()
    sys.exit(app.exec_())

