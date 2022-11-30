# -*- coding: utf-8 -*-

# Created by Atahan Caldir

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Form(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowIcon(QtGui.QIcon('Logom.png'))
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
        self.words = QtWidgets.QComboBox(Form)
        self.words.setGeometry(QtCore.QRect(10, 400, 113, 27))
        self.words.setObjectName("words")
        self.words.addItems(list(map(lambda x:str(x),(list(range(1,11))))))
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(240, 290, 16, 131))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.bolumler = QtWidgets.QComboBox(Form)
        self.bolumler.setGeometry(QtCore.QRect(280, 360, 171, 27))
        self.bolumler.setObjectName("word_per")
        self.bolumler.addItems(list(map(lambda x:str(x),(list(range(50,500))))))
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
        self.word_number_label.setText(_translate("Form", "word number (1-10) :"))
        self.label.setText(_translate("Form", "words per minute:"))


class Ui_start_window(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, start_window):
        start_window.setObjectName("start_window")
        start_window.resize(265, 115)
        start_window.setMinimumSize(QtCore.QSize(265, 115))
        start_window.setMaximumSize(QtCore.QSize(265, 115))
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


class Ui_reader(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, reader):
        reader.setObjectName("reader")
        reader.resize(842, 132)
        reader.setMaximumSize(QtCore.QSize(842, 132))
        reader.setMinimumSize(QtCore.QSize(842, 132))
        self.read_label = QtWidgets.QLabel(reader)
        self.read_label.setGeometry(QtCore.QRect(10, 10, 821, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.read_label.setFont(font)
        self.read_label.setText("")
        self.read_label.setObjectName("read_label")
        self.read_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pushButton = QtWidgets.QPushButton(reader)
        self.pushButton.setGeometry(QtCore.QRect(370, 100, 99, 27))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(reader)
        QtCore.QMetaObject.connectSlotsByName(reader)

    def retranslateUi(self, reader):
        _translate = QtCore.QCoreApplication.translate
        reader.setWindowTitle(_translate("reader", "reading"))
        self.pushButton.setText(_translate("reader", "finish"))