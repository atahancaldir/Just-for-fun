# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_win.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(471, 484)
        Form.setMinimumSize(QtCore.QSize(471, 484))
        Form.setMaximumSize(QtCore.QSize(471, 484))
        self.create_but = QtWidgets.QPushButton(Form)
        self.create_but.setGeometry(QtCore.QRect(10, 440, 451, 27))
        self.create_but.setObjectName("create_but")
        self.fontComboBox = QtWidgets.QFontComboBox(Form)
        self.fontComboBox.setGeometry(QtCore.QRect(10, 310, 201, 27))
        self.fontComboBox.setObjectName("fontComboBox")
        self.font_label = QtWidgets.QLabel(Form)
        self.font_label.setGeometry(QtCore.QRect(10, 290, 67, 17))
        self.font_label.setObjectName("font_label")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 451, 261))
        self.textEdit.setObjectName("textEdit")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 350, 221, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.word_number_label = QtWidgets.QLabel(Form)
        self.word_number_label.setGeometry(QtCore.QRect(10, 370, 141, 17))
        self.word_number_label.setObjectName("word_number_label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 400, 113, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(240, 290, 16, 131))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.timeEdit = QtWidgets.QTimeEdit(Form)
        self.timeEdit.setGeometry(QtCore.QRect(280, 360, 171, 27))
        self.timeEdit.setObjectName("timeEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(290, 330, 141, 17))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "fasty read"))
        self.create_but.setText(_translate("Form", "create"))
        self.font_label.setText(_translate("Form", "font:"))
        self.word_number_label.setText(_translate("Form", "word number (0-10) :"))
        self.label.setText(_translate("Form", "words per minute:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

