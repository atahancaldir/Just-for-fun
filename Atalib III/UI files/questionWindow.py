# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'questionWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_questionWindow(object):
    def setupUi(self, questionWindow):
        questionWindow.setObjectName("questionWindow")
        questionWindow.resize(570, 180)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../media/Logom2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        questionWindow.setWindowIcon(icon)
        questionWindow.setStyleSheet("background:#80c5ed;")
        self.horizontalLayoutWidget = QtWidgets.QWidget(questionWindow)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 90, 551, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ok_but = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ok_but.setStyleSheet("background:green;\n"
"color:white;")
        self.ok_but.setObjectName("ok_but")
        self.horizontalLayout.addWidget(self.ok_but)
        self.cancel_but = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cancel_but.setStyleSheet("background:red;\n"
"color:white;")
        self.cancel_but.setObjectName("cancel_but")
        self.horizontalLayout.addWidget(self.cancel_but)
        self.label = QtWidgets.QLabel(questionWindow)
        self.label.setGeometry(QtCore.QRect(10, 30, 551, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(questionWindow)
        QtCore.QMetaObject.connectSlotsByName(questionWindow)

    def retranslateUi(self, questionWindow):
        _translate = QtCore.QCoreApplication.translate
        questionWindow.setWindowTitle(_translate("questionWindow", "Form"))
        self.ok_but.setText(_translate("questionWindow", "OK"))
        self.cancel_but.setText(_translate("questionWindow", "Cancel"))
        self.label.setText(_translate("questionWindow", "Are you sure you want to delete book?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    questionWindow = QtWidgets.QWidget()
    ui = Ui_questionWindow()
    ui.setupUi(questionWindow)
    questionWindow.show()
    sys.exit(app.exec_())

