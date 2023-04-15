# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reading.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(842, 132)
        Form.setMaximumSize(QtCore.QSize(842, 132))
        Form.setWindowIcon(QtGui.QIcon('Logom.png'))
        Form.setSizeIncrement(QtCore.QSize(842, 132))
        self.read_label = QtWidgets.QLabel(Form)
        self.read_label.setGeometry(QtCore.QRect(10, 10, 821, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.read_label.setFont(font)
        self.read_label.setText("")
        self.read_label.setObjectName("read_label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(370, 100, 99, 27))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "reading"))
        self.pushButton.setText(_translate("Form", "finish"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

