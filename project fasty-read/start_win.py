# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_win.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_start_window(object):
    def setupUi(self, start_window):
        start_window.setObjectName("start_window")
        start_window.resize(265, 115)
        self.label = QtWidgets.QLabel(start_window)
        self.label.setGeometry(QtCore.QRect(20, 30, 61, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.time_label = QtWidgets.QLabel(start_window)
        self.time_label.setGeometry(QtCore.QRect(90, 20, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Tibetan Machine Uni")
        font.setPointSize(13)
        self.time_label.setFont(font)
        self.time_label.setText("")
        self.time_label.setObjectName("time_label")
        self.start = QtWidgets.QPushButton(start_window)
        self.start.setGeometry(QtCore.QRect(70, 70, 119, 27))
        self.start.setObjectName("start")

        self.retranslateUi(start_window)
        QtCore.QMetaObject.connectSlotsByName(start_window)

    def retranslateUi(self, start_window):
        _translate = QtCore.QCoreApplication.translate
        start_window.setWindowTitle(_translate("start_window", "start reading"))
        self.label.setText(_translate("start_window", "time:"))
        self.start.setText(_translate("start_window", "start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    start_window = QtWidgets.QWidget()
    ui = Ui_start_window()
    ui.setupUi(start_window)
    start_window.show()
    sys.exit(app.exec_())

