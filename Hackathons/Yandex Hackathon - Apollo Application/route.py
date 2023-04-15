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
        self.label.setStyleSheet("backgruo")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/phone.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.routeFrame = QtWidgets.QFrame(MAIN)
        self.routeFrame.setGeometry(QtCore.QRect(31, 58, 401, 772))
        self.routeFrame.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.0738636 #205AFF, stop:0.840909 #1180FF);")
        self.routeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.routeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.routeFrame.setObjectName("routeFrame")
        self.routeBackBut = QtWidgets.QPushButton(self.routeFrame)
        self.routeBackBut.setGeometry(QtCore.QRect(20, 20, 40, 40))
        self.routeBackBut.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.routeBackBut.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.routeBackBut.setIcon(icon)
        self.routeBackBut.setIconSize(QtCore.QSize(30, 30))
        self.routeBackBut.setObjectName("routeBackBut")
        self.routeTopLabel = QtWidgets.QLabel(self.routeFrame)
        self.routeTopLabel.setGeometry(QtCore.QRect(0, 30, 401, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.routeTopLabel.setFont(font)
        self.routeTopLabel.setStyleSheet("background: rgb(0,0,0,0);\n"
"color:white;")
        self.routeTopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.routeTopLabel.setObjectName("routeTopLabel")
        self.routeMap = QtWidgets.QLabel(self.routeFrame)
        self.routeMap.setGeometry(QtCore.QRect(0, 70, 401, 322))
        self.routeMap.setText("")
        self.routeMap.setPixmap(QtGui.QPixmap("img/gps3.png"))
        self.routeMap.setScaledContents(True)
        self.routeMap.setObjectName("routeMap")
        self.routeSongList = QtWidgets.QListWidget(self.routeFrame)
        self.routeSongList.setGeometry(QtCore.QRect(0, 444, 401, 328))
        self.routeSongList.setStyleSheet("background:white;")
        self.routeSongList.setObjectName("routeSongList")
        self.comboBox = QtWidgets.QComboBox(self.routeFrame)
        self.comboBox.setGeometry(QtCore.QRect(10, 400, 381, 31))
        self.comboBox.setStyleSheet("background:#01A7FF;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.routeTopLabel.raise_()
        self.routeBackBut.raise_()
        self.routeMap.raise_()
        self.routeSongList.raise_()
        self.comboBox.raise_()

        self.retranslateUi(MAIN)
        QtCore.QMetaObject.connectSlotsByName(MAIN)

    def retranslateUi(self, MAIN):
        _translate = QtCore.QCoreApplication.translate
        MAIN.setWindowTitle(_translate("MAIN", "Apollo"))
        self.routeTopLabel.setText(_translate("MAIN", "Discover"))
        self.comboBox.setCurrentText(_translate("MAIN", "Select a category"))
        self.comboBox.setItemText(0, _translate("MAIN", "Select a category"))
        self.comboBox.setItemText(1, _translate("MAIN", "Metal"))
        self.comboBox.setItemText(2, _translate("MAIN", "Rock"))
        self.comboBox.setItemText(3, _translate("MAIN", "Rap"))
        self.comboBox.setItemText(4, _translate("MAIN", "Pop"))
        self.comboBox.setItemText(5, _translate("MAIN", "Blues"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MAIN = QtWidgets.QWidget()
    ui = Ui_MAIN()
    ui.setupUi(MAIN)
    MAIN.show()
    sys.exit(app.exec_())

