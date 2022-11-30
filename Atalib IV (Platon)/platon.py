# -*- coding: utf-8 -*-

# Created by Atahan Caldir

from gui import *
import random
import sqlite3 as sq
import os
import sys
import locale
from functools import cmp_to_key
import uuid

class Library():
    def __init__(self):
        self.categoryNames = {"All Books":"allbooks","Academic":"academic","Art":"art","Biography":"biography","Business":"business","Comics":"comics",
        "Economics":"economics","Essay":"essay","History":"history","Law":"law","Novel":"novel","Personal Evolution":"persev","Philosophy":"philosophy",
        "Poetry":"poetry","Politics":"politics","Religion":"religion","Science":"science","Turkish Literature":"turlit",
        "World Literature":"worlit","Research":"research"}
        self.itemCounter = 0
        self.connectDatabase()
        self.placeBooks(clear = True)

    def connectDatabase(self):
        self.con = sq.connect("books.db")
        self.cursor = self.con.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS shelves(name TEXT,author TEXT,page TEXT,owned TEXT,read TEXT,category TEXT)")
        self.con.commit()

    def placeBooks(self, category = "All Books", search = "", clear = False, sortChanged = False):
        if clear == False and mainWindow.bookList.verticalScrollBar().value() != mainWindow.bookList.verticalScrollBar().maximum():
            return

        if sortChanged:
            mainWindow.bookList.clear()
            self.itemCounter = 0
            self.sortBooks()

        if clear and not sortChanged: #If clear is True, self.books will be created again and list will be placed from zero. Else, it will continue to place books(for scrolling down)
            mainWindow.bookList.clear()
            self.itemCounter = 0
            self.getBooks(category, search)
            self.books = list(set(self.books))
            mainWindow.sortCombo.setCurrentIndex(0)
            self.sortBooks()

            mainWindow.bookCount.setProperty("intValue", len(self.books))
            mainWindow.ownCount.setProperty("intValue", len(list(filter(lambda x: x[3] == "yes", self.books))))
            mainWindow.readCount.setProperty("intValue", len(list(filter(lambda x: x[4] == "yes", self.books))))

            mainWindow.readProgress.setMaximum(len(self.books))
            mainWindow.readProgress.setProperty("value", len(list(filter(lambda x: x[4] == "yes", self.books))))

            if category == "Research":
                mainWindow.sortCombo.setDisabled(True)
            else:
                mainWindow.sortCombo.setDisabled(False)
        
        for book in self.books[self.itemCounter:self.itemCounter + 10]:
            if book[5] != "research":
                myQCustomQWidget = Ui_bookItemWindow()

                for i,j in self.categoryNames.items():
                    if j == book[5]:
                        cleanedCategory = i

                myQCustomQWidget.setBookDetails(book[0], book[1], book[2] + " pages", cleanedCategory, book[-1], book[-2])
                myQListWidgetItem = QtWidgets.QListWidgetItem(mainWindow.bookList)

                if book[3] == "yes" and book[4] == "no":	
                    myQCustomQWidget.indicatorLabel.setStyleSheet("border-radius: 5px; background: #E0CA33;")
            
                elif book[4] == "yes":
                    myQCustomQWidget.indicatorLabel.setStyleSheet("border-radius: 5px; background: #40DE82;")

                myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
                mainWindow.bookList.addItem(myQListWidgetItem)
                mainWindow.bookList.setItemWidget(myQListWidgetItem, myQCustomQWidget)
                
            else:
                new_item = QtWidgets.QListWidgetItem(book[0])
                mainWindow.bookList.addItem(new_item)

        self.itemCounter += 10

    def getBooks(self, category = "All Books", search = ""):
        category = self.categoryNames[category]

        if category != "allbooks":
            self.cursor.execute("SELECT * FROM shelves WHERE category = ?", (category,))
            self.books = self.cursor.fetchall()
            mainWindow.searchLine.clear()

        elif search != "":
            self.cursor.execute("SELECT * FROM shelves WHERE name LIKE ? AND category != 'research'", ("%" + search + "%",))
            self.books = self.cursor.fetchall()
            self.cursor.execute("SELECT * FROM shelves WHERE author LIKE ? AND category != 'research'", ("%" + search + "%",))
            self.books.extend(self.cursor.fetchall())
        
        else:
            self.cursor.execute("SELECT * FROM shelves WHERE category != 'research'")
            self.books = self.cursor.fetchall()
            mainWindow.searchLine.clear()

    def sortBooks(self):
        def sortPage(x):
            try:
                return int(x[2])
            except:
                return 99999

        def sortLetter(x):
            for i in range(len(sortList)):
                if x == sortList[i]:
                    return i

        sortBy = mainWindow.sortCombo.currentText()

        sortList = []

        if ("Book Name" in sortBy) or ("Author Name" in sortBy):
            if "Book Name" in sortBy:
                index = 0 #index for book information order in database
            else:
                index = 1

            for i in self.books:
                sortList.append(i[index])

            sortList.sort(key=cmp_to_key(locale.strcoll))

            self.books.sort(reverse=("Z>A" in sortBy), key=lambda x: sortLetter(x[index]))

        elif "Page Count" in sortBy:
            self.books.sort(key=sortPage)

        elif "Owned Books" in sortBy:
            self.books = list(filter(lambda x: x[3]=="yes", self.books))

        else:
            self.books = list(filter(lambda x: x[4]=="yes", self.books))

    def openNotes(self):
        os.system(os.getcwd() + "\\Notes.txt")

app = QtWidgets.QApplication(sys.argv)

mainWindow = Ui_MAIN()
bookDetailsWindow = Ui_bookDetailsWindow()

mainWindow.show()

locale.setlocale(locale.LC_ALL, "tr_TR.UTF-8")
library = Library()

mainWindow.bookList.verticalScrollBar().valueChanged.connect(lambda: library.placeBooks())
mainWindow.notesBut.clicked.connect(lambda: library.openNotes())
mainWindow.categoryCombo.currentTextChanged.connect(lambda: library.placeBooks(category=mainWindow.categoryCombo.currentText(), clear=True))
mainWindow.sortCombo.currentTextChanged.connect(lambda: library.placeBooks(sortChanged=True, clear=True))
mainWindow.searchBut.clicked.connect(lambda: library.placeBooks(clear=True, search=mainWindow.searchLine.text()))
mainWindow.searchLine.returnPressed.connect(lambda: library.placeBooks(clear=True, search=mainWindow.searchLine.text()))

sys.exit(app.exec_())