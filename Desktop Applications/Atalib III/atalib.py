from gui import *
import random
import sqlite3 as sq

class Library():
    
    def __init__(self):
        self.category_names = {"All Books":"allbooks","Academic":"academic","Art":"art","Biography":"biography","Business":"business",
        "Economics":"economics","History":"history","Law":"law","Novel":"novel","Personal Evolution":"persev","Philosophy":"philosophy",
        "Poetry":"poetry","Politics":"politics","Religion":"religion","Science":"science","Turkish Literature":"turlit",
        "World Literature":"worlit","Research":"research"}
        self.check_convert = {True:"yes",False:"no"}
        self.connectDatabase()
        self.categorizeBooks("All Books")

    def connectDatabase(self):
        self.con = sq.connect("books.db")
        self.cursor = self.con.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS shelves(name TEXT,author TEXT,page TEXT,owned TEXT,read TEXT,category TEXT)")
        self.con.commit()

    def placeBooks(self, books):
        mainWindow.book_list.clear()

        mainWindow.book_count_label.setText(str(len(books)))
        mainWindow.owned_count_label.setText(str(len(list(filter(lambda x: x[-3] == "yes", books)))))
        mainWindow.read_count_label.setText(str(len(list(filter(lambda x: x[-2] == "yes", books)))))

        for book in books:
            if book[-1] != "research":
                new_item = QtWidgets.QListWidgetItem(book[0]+" | "+book[1])
            else:
                new_item = QtWidgets.QListWidgetItem(book[0])
                mainWindow.book_list.addItem(new_item)
                continue
            
            if book[-3] == "yes" and book[-2] == "no":	
                new_item.setBackground(yellow)
            
            elif book[-2] == "yes":
                new_item.setBackground(green)

            mainWindow.book_list.addItem(new_item)

    def categorizeBooks(self, category="All Books"):
        mainWindow.search_box.clear()
        mainWindow.cat_name_label.setText(category)

        category = self.category_names[category]

        self.cat = category

        if category == "research":
            mainWindow.sorter.setDisabled(True)
            mainWindow.search_box.clear()
            mainWindow.search_box.setDisabled(True)
        else:
            mainWindow.sorter.setCurrentIndex(0)
            mainWindow.sorter.setDisabled(False)
            mainWindow.search_box.setDisabled(False)

        if category == "allbooks":
            self.cursor.execute("SELECT * FROM shelves WHERE category != 'research'")
        else:
            self.cursor.execute("SELECT * FROM shelves WHERE category = ?",(category,))
        
        self.items = self.cursor.fetchall()
        self.items.sort()
		
        self.placeBooks(self.items)

    def sortBy(self):
        def sortEdit(a):
            try:
                return int(a[2])
            except:
                return 99999

        sortCriteria = mainWindow.sorter.currentText()

        if "Book Name" in sortCriteria:
            self.items.sort(reverse=("Z>A" in sortCriteria))
            self.placeBooks(self.items)

        elif "Author Name" in sortCriteria:
            self.items.sort(reverse=("Z>A" in sortCriteria), key=lambda x: x[1])
            self.placeBooks(self.items)

        elif "Page Count" in sortCriteria:
            self.items.sort(key=sortEdit)
            self.placeBooks(self.items)

        elif "Owned Books" in sortCriteria:
            self.items2 = list(filter(lambda x: x[-3]=="yes", self.items))
            self.placeBooks(self.items2)

        else:
            self.items2 = list(filter(lambda x: x[-2]=="yes", self.items))
            self.placeBooks(self.items2)

    def searchBooks(self):
        search_text = mainWindow.search_box.text()

        if search_text == "":
            for i,j in self.category_names.items():
                if j == self.cat:
                    self.categorizeBooks(i)
            return
        
        if self.cat == "allbooks":
            self.cursor.execute("SELECT * FROM shelves WHERE name LIKE ? AND category != 'research'", ("%"+search_text+"%",))
            self.items = self.cursor.fetchall()
            self.cursor.execute("SELECT * FROM shelves WHERE author LIKE ? AND category != 'research'", ("%"+search_text+"%",))
            self.items.extend(self.cursor.fetchall())

        else:
            self.cursor.execute("SELECT * FROM shelves WHERE name LIKE ? AND category = ?", ("%"+search_text+"%", self.cat))
            self.items = self.cursor.fetchall()
            self.cursor.execute("SELECT * FROM shelves WHERE author LIKE ? AND category = ?", ("%"+search_text+"%", self.cat))
            self.items.extend(self.cursor.fetchall())

        self.items = list(set(self.items))
        self.items.sort()
        mainWindow.sorter.setCurrentIndex(0)

        self.placeBooks(self.items)

    def bookDetails(self, book):

        def editBook():
            bookDetailsWindow.book_name_label.setStyleSheet("background:white;")
            bookDetailsWindow.author_name_label.setStyleSheet("background:white;")
            bookDetailsWindow.page_label.setStyleSheet("background:white;")
            bookDetailsWindow.book_name_label.setReadOnly(False)
            bookDetailsWindow.author_name_label.setReadOnly(False)
            bookDetailsWindow.page_label.setReadOnly(False)
            bookDetailsWindow.owned_check.setDisabled(False)
            bookDetailsWindow.read_check.setDisabled(False)
            bookDetailsWindow.cat_combo.setDisabled(False)
            bookDetailsWindow.save_but.setDisabled(False)

        def saveBook():
            questionWindow.setWindowTitle("Save Book")
            questionWindow.label.setText("Are you sure you want to save changes?")
            questionWindow.show()

            def okPressed():
                new_book_name = bookDetailsWindow.book_name_label.text()
                new_author_name = bookDetailsWindow.author_name_label.text()
                new_page_number = bookDetailsWindow.page_label.text()
                new_owned = self.check_convert[bookDetailsWindow.owned_check.isChecked()]
                new_read = self.check_convert[bookDetailsWindow.read_check.isChecked()]
                new_category = self.category_names[bookDetailsWindow.cat_combo.currentText()]

                self.cursor.execute("UPDATE shelves SET name = ?, author = ?, page = ?, owned = ?, read = ?, category = ? WHERE name = ? AND author = ?",
                (new_book_name, new_author_name, new_page_number, new_owned, new_read, new_category, self.detailed_book[0], self.detailed_book[1]))
                self.con.commit()

                bookDetailsWindow.close()
                questionWindow.close()
                self.searchBooks()

            questionWindow.ok_but.clicked.connect(okPressed)

        def deleteBook():
            questionWindow.setWindowTitle("Delete Book")
            questionWindow.label.setText("Are you sure you want to delete this book?")
            questionWindow.show()

            def okPressed():
                self.cursor.execute("DELETE FROM shelves WHERE name = ? AND author = ? AND page = ? AND category = ?",
                (self.detailed_book[0],self.detailed_book[1],self.detailed_book[2],self.detailed_book[5]))
                self.con.commit()

                bookDetailsWindow.close()
                questionWindow.close()
                self.searchBooks()

            questionWindow.ok_but.clicked.connect(okPressed)

        bookDetailsWindow.show()
        bookDetailsWindow.save_but.setDisabled(True)

        book_name = book.text().split(" | ")[0]
        author_name = book.text().split(" | ")[1]

        self.cursor.execute("SELECT * FROM shelves WHERE name = ? AND author = ?",(book_name, author_name))
        self.detailed_book = self.cursor.fetchall()[0]

        bookDetailsWindow.book_name_label.setText(self.detailed_book[0])
        bookDetailsWindow.author_name_label.setText(self.detailed_book[1])
        bookDetailsWindow.page_label.setText(self.detailed_book[2])
        bookDetailsWindow.owned_check.setChecked(self.detailed_book[3]=="yes")
        bookDetailsWindow.read_check.setChecked(self.detailed_book[4]=="yes")

        if self.detailed_book[3] == "yes":
            bookDetailsWindow.owned_check.setStyleSheet("color:green;")
        else:
            bookDetailsWindow.owned_check.setStyleSheet("color:#d64922;")

        if self.detailed_book[4] == "yes":
            bookDetailsWindow.read_check.setStyleSheet("color:green;")
        else:
            bookDetailsWindow.read_check.setStyleSheet("color:#d64922;")

        for i,j in self.category_names.items():
                if j == self.detailed_book[5]:
                    bookDetailsWindow.cat_combo.setCurrentText(i)

        bookDetailsWindow.edit_but.clicked.connect(editBook)
        bookDetailsWindow.save_but.clicked.connect(saveBook)
        bookDetailsWindow.delete_but.clicked.connect(deleteBook)

    def addBook(self):
        addBookWindow.show()

        def saveAdd():
            add_book_name = addBookWindow.book_name_label.text()
            add_book_author = addBookWindow.author_name_label.text()
            add_book_page = addBookWindow.page_label.text()
            add_book_owned = self.check_convert[addBookWindow.owned_check.isChecked()]
            add_book_read = self.check_convert[addBookWindow.read_check.isChecked()]

            try:
                add_book_category = self.category_names[addBookWindow.cat_combo.currentText()]
            except:
                QtWidgets.QMessageBox.warning(addBookWindow, 'Warning', 'Please select a valid category!')
                return

            if add_book_name == "" or add_book_author == "" or add_book_page == "":
                QtWidgets.QMessageBox.warning(addBookWindow, 'Warning', 'Please be sure that all boxes are filled!')

            else:
                self.cursor.execute("INSERT INTO shelves VALUES(?,?,?,?,?,?)",
                (add_book_name,add_book_author,add_book_page,add_book_owned,add_book_read,add_book_category))
                self.con.commit()

                addBookWindow.close()
                self.searchBooks()

        addBookWindow.cancel_but.clicked.connect(lambda: addBookWindow.close())
        addBookWindow.add_but.clicked.connect(saveAdd)

    def randomBook(self):
        book = random.choice(self.items)
        book = book[0] + " | " + book[1]
        QtWidgets.QMessageBox.information(mainWindow, 'Random Book', book)

try:
    app = QtWidgets.QApplication(sys.argv)

    mainWindow = Ui_mainWindow()
    addBookWindow = Ui_addBookWindow()
    bookDetailsWindow = Ui_bookDetailsWindow()
    questionWindow = Ui_questionWindow()

    library = Library()

    mainWindow.show()

    mainWindow.cat_allbooks.clicked.connect(lambda: library.categorizeBooks("All Books"))
    mainWindow.cat_academic.clicked.connect(lambda: library.categorizeBooks("Academic"))
    mainWindow.cat_art.clicked.connect(lambda: library.categorizeBooks("Art"))
    mainWindow.cat_biography.clicked.connect(lambda: library.categorizeBooks("Biography"))
    mainWindow.cat_business.clicked.connect(lambda: library.categorizeBooks("Business"))
    mainWindow.cat_economics.clicked.connect(lambda: library.categorizeBooks("Economics"))
    mainWindow.cat_history.clicked.connect(lambda: library.categorizeBooks("History"))
    mainWindow.cat_law.clicked.connect(lambda: library.categorizeBooks("Law"))
    mainWindow.cat_novel.clicked.connect(lambda: library.categorizeBooks("Novel"))
    mainWindow.cat_persev.clicked.connect(lambda: library.categorizeBooks("Personal Evolution"))
    mainWindow.cat_philosophy.clicked.connect(lambda: library.categorizeBooks("Philosophy"))
    mainWindow.cat_poetry.clicked.connect(lambda: library.categorizeBooks("Poetry"))
    mainWindow.cat_politics.clicked.connect(lambda: library.categorizeBooks("Politics"))
    mainWindow.cat_religion.clicked.connect(lambda: library.categorizeBooks("Religion"))
    mainWindow.cat_science.clicked.connect(lambda: library.categorizeBooks("Science"))
    mainWindow.cat_turlit.clicked.connect(lambda: library.categorizeBooks("Turkish Literature"))
    mainWindow.cat_worlit.clicked.connect(lambda: library.categorizeBooks("World Literature"))
    mainWindow.cat_research.clicked.connect(lambda: library.categorizeBooks("Research"))
    mainWindow.search_but.clicked.connect(library.searchBooks)
    mainWindow.search_box.returnPressed.connect(library.searchBooks)
    mainWindow.sorter.currentIndexChanged.connect(library.sortBy)
    mainWindow.book_list.itemDoubleClicked.connect(library.bookDetails)
    mainWindow.random_book_but.clicked.connect(library.randomBook)
    mainWindow.add_book_but.clicked.connect(library.addBook)

    sys.exit(app.exec_())

finally:
    library.con.close()