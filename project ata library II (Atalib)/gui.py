# -*- coding: utf-8 -*-

# Created by Atahan Caldir


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

yellow = QtGui.QBrush(QtCore.Qt.yellow)
green = QtGui.QBrush(QtCore.Qt.green)

class Ui_MAIN(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, MAIN):
        MAIN.setObjectName("MAIN")
        MAIN.resize(705, 531)
        MAIN.setMinimumSize(QtCore.QSize(705, 531))
        MAIN.setMaximumSize(QtCore.QSize(705, 531))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MAIN.setWindowIcon(icon)
        MAIN.setStyleSheet("background:#67baea;")
        self.search_frame = QtWidgets.QFrame(MAIN)
        self.search_frame.setGeometry(QtCore.QRect(20, 10, 561, 40))
        self.search_frame.setStyleSheet("background:white;\n"
"border-radius:20px;")
        self.search_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.search_frame.setObjectName("search_frame")
        self.search_but = QtWidgets.QPushButton(self.search_frame)
        self.search_but.setGeometry(QtCore.QRect(517, 5, 30, 30))
        self.search_but.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_but.setIcon(icon1)
        self.search_but.setIconSize(QtCore.QSize(20, 20))
        self.search_but.setObjectName("search_but")
        self.search_line = QtWidgets.QLineEdit(self.search_frame)
        self.search_line.setGeometry(QtCore.QRect(20, 8, 481, 24))
        self.search_line.setObjectName("search_line")
        self.top_frame = QtWidgets.QFrame(MAIN)
        self.top_frame.setGeometry(QtCore.QRect(590, 10, 101, 250))
        self.top_frame.setStyleSheet("background:#80c5ed;\n"
"border-radius:25px;")
        self.top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame.setObjectName("top_frame")
        self.add_but = QtWidgets.QPushButton(self.top_frame)
        self.add_but.setGeometry(QtCore.QRect(23, 15, 50, 50))
        self.add_but.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/add_book.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_but.setIcon(icon2)
        self.add_but.setIconSize(QtCore.QSize(50, 50))
        self.add_but.setObjectName("add_but")
        self.random_but = QtWidgets.QPushButton(self.top_frame)
        self.random_but.setGeometry(QtCore.QRect(30, 103, 40, 40))
        self.random_but.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/randomm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.random_but.setIcon(icon3)
        self.random_but.setIconSize(QtCore.QSize(40, 40))
        self.random_but.setObjectName("random_but")
        self.research_but = QtWidgets.QPushButton(self.top_frame)
        self.research_but.setGeometry(QtCore.QRect(30, 175, 40, 40))
        self.research_but.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/research.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.research_but.setIcon(icon4)
        self.research_but.setIconSize(QtCore.QSize(40, 40))
        self.research_but.setObjectName("research_but")
        self.label = QtWidgets.QLabel(self.top_frame)
        self.label.setGeometry(QtCore.QRect(20, 75, 58, 14))
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.top_frame)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 81, 20))
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.top_frame)
        self.label_3.setGeometry(QtCore.QRect(22, 220, 58, 14))
        self.label_3.setStyleSheet("color:white;")
        self.label_3.setObjectName("label_3")
        self.bot_frame = QtWidgets.QFrame(MAIN)
        self.bot_frame.setGeometry(QtCore.QRect(590, 270, 101, 250))
        self.bot_frame.setStyleSheet("background:#80c5ed;\n"
"border-radius:25px;")
        self.bot_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bot_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bot_frame.setObjectName("bot_frame")
        self.category = QtWidgets.QComboBox(self.bot_frame)
        self.category.setGeometry(QtCore.QRect(10, 40, 78, 24))
        self.category.setStyleSheet("background:#edd080;\n"
"border-radius:10px;color:black;")
        self.category.setObjectName("category")
        self.category.addItems(["All","Novel","Science","History","Poetry","Personal_evolution","Philosophy","World_literature","Turkish_literature","Religion","Biography"])
        self.filter_but = QtWidgets.QPushButton(self.bot_frame)
        self.filter_but.setGeometry(QtCore.QRect(10, 70, 81, 27))
        self.filter_but.setStyleSheet("background:#c6ae69;\n"
"border-radius:10px;\n"
"border:2px solid orange;")
        self.filter_but.setObjectName("filter_but")
        self.label_4 = QtWidgets.QLabel(self.bot_frame)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 58, 14))
        self.label_4.setStyleSheet("color:white;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.bot_frame)
        self.label_5.setGeometry(QtCore.QRect(15, 120, 71, 16))
        self.label_5.setStyleSheet("color:white;")
        self.label_5.setObjectName("label_5")
        self.book_count = QtWidgets.QLabel(self.bot_frame)
        self.book_count.setGeometry(QtCore.QRect(15, 140, 71, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.book_count.setFont(font)
        self.book_count.setStyleSheet("background:#c68969;\n"
"border-radius:10px;")
        self.book_count.setText("")
        self.book_count.setAlignment(QtCore.Qt.AlignCenter)
        self.book_count.setObjectName("book_count")
        self.read_count = QtWidgets.QLabel(self.bot_frame)
        self.read_count.setGeometry(QtCore.QRect(15, 200, 71, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.read_count.setFont(font)
        self.read_count.setStyleSheet("background:#c68969;\n"
"border-radius:10px;")
        self.read_count.setText("")
        self.read_count.setAlignment(QtCore.Qt.AlignCenter)
        self.read_count.setObjectName("read_count")
        self.label_8 = QtWidgets.QLabel(self.bot_frame)
        self.label_8.setGeometry(QtCore.QRect(15, 180, 71, 16))
        self.label_8.setStyleSheet("color:white;")
        self.label_8.setObjectName("label_8")
        self.book_list = QtWidgets.QListWidget(MAIN)
        self.book_list.setGeometry(QtCore.QRect(20, 60, 561, 461))
        self.book_list.setStyleSheet("background:white;\n"
"border:3px solid #417da0;")
        self.book_list.setObjectName("book_list")

        self.retranslateUi(MAIN)
        QtCore.QMetaObject.connectSlotsByName(MAIN)

    def retranslateUi(self, MAIN):
        _translate = QtCore.QCoreApplication.translate
        MAIN.setWindowTitle(_translate("MAIN", "Atalib"))
        self.search_line.setPlaceholderText(_translate("MAIN", "Search book or author\'s name"))
        self.label.setText(_translate("MAIN", "Add book"))
        self.label_2.setText(_translate("MAIN", "Random book"))
        self.label_3.setText(_translate("MAIN", "Research"))
        self.filter_but.setText(_translate("MAIN", "Filter"))
        self.label_4.setText(_translate("MAIN", "Category"))
        self.label_5.setText(_translate("MAIN", "Book count"))
        self.label_8.setText(_translate("MAIN", "Read count"))


class Ui_ADD_BOOK(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, ADD_BOOK):
        ADD_BOOK.setObjectName("ADD_BOOK")
        ADD_BOOK.resize(377, 280)
        ADD_BOOK.setMinimumSize(QtCore.QSize(377, 280))
        ADD_BOOK.setMaximumSize(QtCore.QSize(377, 280))
        ADD_BOOK.setStyleSheet("background:#67baea;")
        self.book_name = QtWidgets.QLineEdit(ADD_BOOK)
        self.book_name.setGeometry(QtCore.QRect(20, 10, 331, 31))
        self.book_name.setStyleSheet("background:white;\n"
"border-radius:15px;")
        self.book_name.setObjectName("book_name")
        self.author_name = QtWidgets.QLineEdit(ADD_BOOK)
        self.author_name.setGeometry(QtCore.QRect(20, 60, 331, 31))
        self.author_name.setStyleSheet("background:white;\n"
"border-radius:15px;")
        self.author_name.setObjectName("author_name")
        self.page_number = QtWidgets.QLineEdit(ADD_BOOK)
        self.page_number.setGeometry(QtCore.QRect(20, 110, 331, 31))
        self.page_number.setStyleSheet("background:white;\n"
"border-radius:15px;")
        self.page_number.setObjectName("page_number")
        self.label = QtWidgets.QLabel(ADD_BOOK)
        self.label.setGeometry(QtCore.QRect(20, 163, 61, 16))
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.category = QtWidgets.QComboBox(ADD_BOOK)
        self.category.setGeometry(QtCore.QRect(85, 160, 261, 24))
        self.category.setStyleSheet("background:#edd080;\n"
"border-radius:10px;color:black;")
        self.category.setObjectName("category")
        self.category.addItems(["All","Novel","Science","History","Poetry","Personal_evolution","Philosophy","World_literature","Turkish_literature","Religion","Biography"])
        self.label_2 = QtWidgets.QLabel(ADD_BOOK)
        self.label_2.setGeometry(QtCore.QRect(20, 200, 41, 16))
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(ADD_BOOK)
        self.label_3.setGeometry(QtCore.QRect(20, 240, 41, 16))
        self.label_3.setStyleSheet("color:white;")
        self.label_3.setObjectName("label_3")
        self.own = QtWidgets.QCheckBox(ADD_BOOK)
        self.own.setGeometry(QtCore.QRect(60, 200, 21, 21))
        self.own.setStyleSheet("background:green;")
        self.own.setText("")
        self.own.setObjectName("own")
        self.read = QtWidgets.QCheckBox(ADD_BOOK)
        self.read.setGeometry(QtCore.QRect(60, 240, 21, 21))
        self.read.setStyleSheet("background:green;")
        self.read.setText("")
        self.read.setObjectName("read")
        self.add_but = QtWidgets.QPushButton(ADD_BOOK)
        self.add_but.setGeometry(QtCore.QRect(130, 210, 88, 51))
        self.add_but.setStyleSheet("background:#80c5ed;\n"
"border-radius:20px;\n"
"border:2px solid red;")
        self.add_but.setObjectName("add_but")
        self.cancel_but = QtWidgets.QPushButton(ADD_BOOK)
        self.cancel_but.setGeometry(QtCore.QRect(250, 210, 88, 51))
        self.cancel_but.setStyleSheet("background:#80c5ed;\n"
"border-radius:20px;\n"
"border:2px solid red;")
        self.cancel_but.setObjectName("cancel_but")

        self.retranslateUi(ADD_BOOK)
        QtCore.QMetaObject.connectSlotsByName(ADD_BOOK)

    def retranslateUi(self, ADD_BOOK):
        _translate = QtCore.QCoreApplication.translate
        ADD_BOOK.setWindowTitle(_translate("ADD_BOOK", "Book name"))
        self.book_name.setPlaceholderText(_translate("ADD_BOOK", " Book name"))
        self.author_name.setPlaceholderText(_translate("ADD_BOOK", " Author name"))
        self.page_number.setPlaceholderText(_translate("ADD_BOOK", " Page number"))
        self.label.setText(_translate("ADD_BOOK", "Category:"))
        self.label_2.setText(_translate("ADD_BOOK", "Own:"))
        self.label_3.setText(_translate("ADD_BOOK", "Read:"))
        self.add_but.setText(_translate("ADD_BOOK", "Add"))
        self.cancel_but.setText(_translate("ADD_BOOK", "Cancel"))

class Ui_BOOK_DETAIL(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, BOOK_DETAIL):
        BOOK_DETAIL.setObjectName("BOOK_DETAIL")
        BOOK_DETAIL.resize(500, 350)
        BOOK_DETAIL.setMinimumSize(QtCore.QSize(500, 350))
        BOOK_DETAIL.setMaximumSize(QtCore.QSize(500, 350))
        BOOK_DETAIL.setStyleSheet("background:#67baea;")
        self.label = QtWidgets.QLabel(BOOK_DETAIL)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.book_name = QtWidgets.QLabel(BOOK_DETAIL)
        self.book_name.setGeometry(QtCore.QRect(20, 41, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.book_name.setFont(font)
        self.book_name.setStyleSheet("background:#80c5ed;\n"
"border-radius:10px;\n"
"color:white;")
        self.book_name.setText("")
        self.book_name.setObjectName("book_name")
        self.label_2 = QtWidgets.QLabel(BOOK_DETAIL)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.author_name = QtWidgets.QLabel(BOOK_DETAIL)
        self.author_name.setGeometry(QtCore.QRect(20, 130, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.author_name.setFont(font)
        self.author_name.setStyleSheet("background:#80c5ed;\n"
"border-radius:10px;\n"
"color:white;")
        self.author_name.setText("")
        self.author_name.setObjectName("author_name")
        self.label_3 = QtWidgets.QLabel(BOOK_DETAIL)
        self.label_3.setGeometry(QtCore.QRect(10, 190, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.category = QtWidgets.QLabel(BOOK_DETAIL)
        self.category.setGeometry(QtCore.QRect(90, 187, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.category.setFont(font)
        self.category.setStyleSheet("background:#80c5ed;\n"
"border-radius:10px;\n"
"color:white;")
        self.category.setText("")
        self.category.setObjectName("category")
        self.label_4 = QtWidgets.QLabel(BOOK_DETAIL)
        self.label_4.setGeometry(QtCore.QRect(250, 190, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.page_number = QtWidgets.QLabel(BOOK_DETAIL)
        self.page_number.setGeometry(QtCore.QRect(370, 187, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.page_number.setFont(font)
        self.page_number.setStyleSheet("background:#80c5ed;\n"
"border-radius:10px;\n"
"color:white;")
        self.page_number.setText("")
        self.page_number.setObjectName("page_number")
        self.label_5 = QtWidgets.QLabel(BOOK_DETAIL)
        self.label_5.setGeometry(QtCore.QRect(10, 250, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(BOOK_DETAIL)
        self.label_6.setGeometry(QtCore.QRect(10, 310, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.own = QtWidgets.QCheckBox(BOOK_DETAIL)
        self.own.setGeometry(QtCore.QRect(60, 250, 21, 21))
        self.own.setStyleSheet("background:green;")
        self.own.setText("")
        self.own.setObjectName("own")
        self.read = QtWidgets.QCheckBox(BOOK_DETAIL)
        self.read.setGeometry(QtCore.QRect(60, 310, 21, 21))
        self.read.setStyleSheet("background:green;")
        self.read.setText("")
        self.read.setObjectName("read")
        self.save_but = QtWidgets.QPushButton(BOOK_DETAIL)
        self.save_but.setGeometry(QtCore.QRect(160, 250, 101, 81))
        self.save_but.setStyleSheet("background:#edd080;\n"
"border-radius:30px;\n"
"border:2px solid red;")
        self.save_but.setObjectName("save_but")
        self.delete_but = QtWidgets.QPushButton(BOOK_DETAIL)
        self.delete_but.setGeometry(QtCore.QRect(310, 250, 101, 81))
        self.delete_but.setStyleSheet("background:#edd080;\n"
"border-radius:30px;\n"
"border:2px solid red;")
        self.delete_but.setObjectName("delete_but")

        self.retranslateUi(BOOK_DETAIL)
        QtCore.QMetaObject.connectSlotsByName(BOOK_DETAIL)

    def retranslateUi(self, BOOK_DETAIL):
        _translate = QtCore.QCoreApplication.translate
        BOOK_DETAIL.setWindowTitle(_translate("BOOK_DETAIL", "Book detail"))
        self.label.setText(_translate("BOOK_DETAIL", "Book name:"))
        self.label_2.setText(_translate("BOOK_DETAIL", "Author name:"))
        self.label_3.setText(_translate("BOOK_DETAIL", "Category:"))
        self.label_4.setText(_translate("BOOK_DETAIL", "Page number:"))
        self.label_5.setText(_translate("BOOK_DETAIL", "Own:"))
        self.label_6.setText(_translate("BOOK_DETAIL", "Read:"))
        self.save_but.setText(_translate("BOOK_DETAIL", "Save and exit"))
        self.delete_but.setText(_translate("BOOK_DETAIL", "Delete book"))


class Ui_DELETE_BOOK(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, DELETE_BOOK):
        DELETE_BOOK.setObjectName("DELETE_BOOK")
        DELETE_BOOK.resize(400, 115)
        DELETE_BOOK.setMinimumSize(QtCore.QSize(400, 115))
        DELETE_BOOK.setMaximumSize(QtCore.QSize(400, 115))
        DELETE_BOOK.setStyleSheet("background:#67baea;")
        self.label = QtWidgets.QLabel(DELETE_BOOK)
        self.label.setGeometry(QtCore.QRect(20, 10, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.yes = QtWidgets.QPushButton(DELETE_BOOK)
        self.yes.setGeometry(QtCore.QRect(70, 60, 88, 27))
        self.yes.setStyleSheet("background:#59b74b;\n"
"border-radius:10px;")
        self.yes.setObjectName("yes")
        self.no = QtWidgets.QPushButton(DELETE_BOOK)
        self.no.setGeometry(QtCore.QRect(240, 60, 88, 27))
        self.no.setStyleSheet("background:#c15034;\n"
"border-radius:10px;")
        self.no.setObjectName("no")

        self.retranslateUi(DELETE_BOOK)
        QtCore.QMetaObject.connectSlotsByName(DELETE_BOOK)

    def retranslateUi(self, DELETE_BOOK):
        _translate = QtCore.QCoreApplication.translate
        DELETE_BOOK.setWindowTitle(_translate("DELETE_BOOK", "Delete book"))
        self.label.setText(_translate("DELETE_BOOK", "Are you sure you want to delete this book?"))
        self.yes.setText(_translate("DELETE_BOOK", "Yes"))
        self.no.setText(_translate("DELETE_BOOK", "No"))


class Ui_RESEARCH(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, RESEARCH):
        RESEARCH.setObjectName("RESEARCH")
        RESEARCH.resize(406, 450)
        RESEARCH.setMinimumSize(QtCore.QSize(406, 450))
        RESEARCH.setMaximumSize(QtCore.QSize(406, 450))
        RESEARCH.setStyleSheet("background:#67baea;")
        self.list = QtWidgets.QListWidget(RESEARCH)
        self.list.setGeometry(QtCore.QRect(13, 10, 380, 391))
        self.list.setStyleSheet("background:white;")
        self.list.setObjectName("list")
        self.new = QtWidgets.QPushButton(RESEARCH)
        self.new.setGeometry(QtCore.QRect(10, 410, 185, 27))
        self.new.setStyleSheet("background:#59b74b;\n"
"border-radius:10px;")
        self.new.setObjectName("new")
        self.delete = QtWidgets.QPushButton(RESEARCH)
        self.delete.setGeometry(QtCore.QRect(205, 410, 185, 27))
        self.delete.setStyleSheet("background:#c15034;\n"
"border-radius:10px;")
        self.delete.setObjectName("delete")

        self.retranslateUi(RESEARCH)
        QtCore.QMetaObject.connectSlotsByName(RESEARCH)

    def retranslateUi(self, RESEARCH):
        _translate = QtCore.QCoreApplication.translate
        RESEARCH.setWindowTitle(_translate("RESEARCH", "Research topics"))
        self.new.setText(_translate("RESEARCH", "New"))
        self.delete.setText(_translate("RESEARCH", "Delete"))


class Ui_RESEARCH_ADD(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, RESEARCH_ADD):
        RESEARCH_ADD.setObjectName("RESEARCH_ADD")
        RESEARCH_ADD.resize(406, 150)
        RESEARCH_ADD.setMinimumSize(QtCore.QSize(406, 150))
        RESEARCH_ADD.setMaximumSize(QtCore.QSize(406, 150))
        RESEARCH_ADD.setStyleSheet("background:#67baea;")
        self.add = QtWidgets.QPushButton(RESEARCH_ADD)
        self.add.setGeometry(QtCore.QRect(10, 60, 185, 27))
        self.add.setStyleSheet("background:#59b74b;\n"
"border-radius:10px;")
        self.add.setObjectName("add")
        self.cancel = QtWidgets.QPushButton(RESEARCH_ADD)
        self.cancel.setGeometry(QtCore.QRect(205, 60, 185, 27))
        self.cancel.setStyleSheet("background:#c15034;\n"
"border-radius:10px;")
        self.cancel.setObjectName("cancel")
        self.name = QtWidgets.QLineEdit(RESEARCH_ADD)
        self.name.setGeometry(QtCore.QRect(10, 13, 381, 31))
        self.name.setStyleSheet("background:white;\n"
"border-radius:15px;")
        self.name.setObjectName("name")

        self.retranslateUi(RESEARCH_ADD)
        QtCore.QMetaObject.connectSlotsByName(RESEARCH_ADD)

    def retranslateUi(self, RESEARCH_ADD):
        _translate = QtCore.QCoreApplication.translate
        RESEARCH_ADD.setWindowTitle(_translate("RESEARCH_ADD", "Add topic"))
        self.add.setText(_translate("RESEARCH_ADD", "Add"))
        self.cancel.setText(_translate("RESEARCH_ADD", "Cancel"))