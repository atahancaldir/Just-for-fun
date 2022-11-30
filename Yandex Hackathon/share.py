# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'share.ui'
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
        self.shareBackBut = QtWidgets.QPushButton(self.shareFrame)
        self.shareBackBut.setGeometry(QtCore.QRect(20, 20, 40, 40))
        self.shareBackBut.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.shareBackBut.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shareBackBut.setIcon(icon)
        self.shareBackBut.setIconSize(QtCore.QSize(30, 30))
        self.shareBackBut.setObjectName("shareBackBut")
        self.shareTopLabel = QtWidgets.QLabel(self.shareFrame)
        self.shareTopLabel.setGeometry(QtCore.QRect(0, 30, 401, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.shareTopLabel.setFont(font)
        self.shareTopLabel.setStyleSheet("background: rgb(0,0,0,0);\n"
"color:white;")
        self.shareTopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.shareTopLabel.setObjectName("shareTopLabel")
        self.shareMap = QtWidgets.QLabel(self.shareFrame)
        self.shareMap.setGeometry(QtCore.QRect(0, 70, 401, 201))
        self.shareMap.setText("")
        self.shareMap.setPixmap(QtGui.QPixmap("img/gps.png"))
        self.shareMap.setScaledContents(True)
        self.shareMap.setObjectName("shareMap")
        self.shareSongList = QtWidgets.QListWidget(self.shareFrame)
        self.shareSongList.setGeometry(QtCore.QRect(0, 341, 401, 361))
        self.shareSongList.setStyleSheet("background:white;")
        self.shareSongList.setObjectName("shareSongList")
        self.shareSearchBox = QtWidgets.QLineEdit(self.shareFrame)
        self.shareSearchBox.setGeometry(QtCore.QRect(14, 280, 371, 41))
        self.shareSearchBox.setStyleSheet("background:white;\n"
"border-radius:10px;")
        self.shareSearchBox.setObjectName("shareSearchBox")
        self.shareSearchButton = QtWidgets.QPushButton(self.shareFrame)
        self.shareSearchButton.setGeometry(QtCore.QRect(350, 287, 31, 28))
        self.shareSearchButton.setStyleSheet("background: rgb(0,0,0,0);")
        self.shareSearchButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shareSearchButton.setIcon(icon1)
        self.shareSearchButton.setObjectName("shareSearchButton")
        self.shareShareBut = QtWidgets.QPushButton(self.shareFrame)
        self.shareShareBut.setGeometry(QtCore.QRect(10, 710, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.shareShareBut.setFont(font)
        self.shareShareBut.setStyleSheet("background:#61d47e;\n"
"border:0px;\n"
"border-radius:20px;\n"
"color:white;")
        self.shareShareBut.setObjectName("shareShareBut")
        self.shareTopLabel.raise_()
        self.shareBackBut.raise_()
        self.shareMap.raise_()
        self.shareSongList.raise_()
        self.shareSearchBox.raise_()
        self.shareSearchButton.raise_()
        self.shareShareBut.raise_()

        self.retranslateUi(MAIN)
        QtCore.QMetaObject.connectSlotsByName(MAIN)

    def retranslateUi(self, MAIN):
        _translate = QtCore.QCoreApplication.translate
        MAIN.setWindowTitle(_translate("MAIN", "Apollo"))
        self.shareTopLabel.setText(_translate("MAIN", "Share"))
        self.shareSearchBox.setPlaceholderText(_translate("MAIN", "Search for a music"))
        self.shareShareBut.setText(_translate("MAIN", "Share!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MAIN = QtWidgets.QWidget()
    ui = Ui_MAIN()
    ui.setupUi(MAIN)
    MAIN.show()
    sys.exit(app.exec_())

