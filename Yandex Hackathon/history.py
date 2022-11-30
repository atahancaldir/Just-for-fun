# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'history.ui'
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
        self.historyFrame = QtWidgets.QFrame(MAIN)
        self.historyFrame.setGeometry(QtCore.QRect(31, 58, 401, 772))
        self.historyFrame.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.0738636 #205AFF, stop:0.840909 #1180FF);")
        self.historyFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.historyFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.historyFrame.setObjectName("historyFrame")
        self.historyBackBut = QtWidgets.QPushButton(self.historyFrame)
        self.historyBackBut.setGeometry(QtCore.QRect(20, 20, 40, 40))
        self.historyBackBut.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.historyBackBut.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.historyBackBut.setIcon(icon)
        self.historyBackBut.setIconSize(QtCore.QSize(30, 30))
        self.historyBackBut.setObjectName("historyBackBut")
        self.historyTopLabel = QtWidgets.QLabel(self.historyFrame)
        self.historyTopLabel.setGeometry(QtCore.QRect(0, 30, 401, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.historyTopLabel.setFont(font)
        self.historyTopLabel.setStyleSheet("background: rgb(0,0,0,0);\n"
"color:white;")
        self.historyTopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.historyTopLabel.setObjectName("historyTopLabel")
        self.historyLineEdit = QtWidgets.QLineEdit(self.historyFrame)
        self.historyLineEdit.setGeometry(QtCore.QRect(14, 80, 371, 41))
        self.historyLineEdit.setStyleSheet("background:white;\n"
"border-radius:10px;")
        self.historyLineEdit.setMaxLength(32766)
        self.historyLineEdit.setObjectName("historyLineEdit")
        self.historySearchBut = QtWidgets.QPushButton(self.historyFrame)
        self.historySearchBut.setGeometry(QtCore.QRect(343, 85, 31, 28))
        self.historySearchBut.setStyleSheet("background:white;\n"
"border:0px;")
        self.historySearchBut.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.historySearchBut.setIcon(icon1)
        self.historySearchBut.setObjectName("historySearchBut")
        self.historySongList = QtWidgets.QListWidget(self.historyFrame)
        self.historySongList.setGeometry(QtCore.QRect(0, 140, 401, 631))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(11)
        self.historySongList.setFont(font)
        self.historySongList.setStyleSheet("background:white;\n"
"color:gray;\n"
"border:0px;")
        self.historySongList.setObjectName("historySongList")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.historySongList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.historySongList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.historySongList.addItem(item)
        self.historyTopLabel.raise_()
        self.historyLineEdit.raise_()
        self.historySearchBut.raise_()
        self.historySongList.raise_()
        self.historyBackBut.raise_()

        self.retranslateUi(MAIN)
        QtCore.QMetaObject.connectSlotsByName(MAIN)

    def retranslateUi(self, MAIN):
        _translate = QtCore.QCoreApplication.translate
        MAIN.setWindowTitle(_translate("MAIN", "Apollo"))
        self.historyTopLabel.setText(_translate("MAIN", "History"))
        self.historyLineEdit.setPlaceholderText(_translate("MAIN", "Search in your history"))
        __sortingEnabled = self.historySongList.isSortingEnabled()
        self.historySongList.setSortingEnabled(False)
        item = self.historySongList.item(0)
        item.setText(_translate("MAIN", "Whenever, Wherever - Shakira"))
        item = self.historySongList.item(1)
        item.setText(_translate("MAIN", "Dark Horse - Katy Perry"))
        item = self.historySongList.item(2)
        item.setText(_translate("MAIN", "Smooth Criminal - Micheal Jackson"))
        self.historySongList.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MAIN = QtWidgets.QWidget()
    ui = Ui_MAIN()
    ui.setupUi(MAIN)
    MAIN.show()
    sys.exit(app.exec_())

