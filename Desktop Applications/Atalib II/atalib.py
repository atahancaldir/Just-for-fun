from gui import *
import random
import sqlite3 as sq


class Library():
	def __init__(self):
		self.start_connection()
		
		
	def start_connection(self):
		self.con = sq.connect("kitaplik2.db")
		self.cursor = self.con.cursor()
		
		self.cursor.execute("CREATE TABLE IF NOT EXISTS raflar(isim TEXT,yazar TEXT,sayfa TEXT,sahip TEXT,okundu TEXT,bolum TEXT)")
		self.con.commit()
		
	def kill_connection(self):
		self.con.close()
		
	def place_book(self):
		window.book_list.clear()
		self.cursor.execute("Select * From raflar where bolum != 'arastirma'")
		self.items = self.cursor.fetchall()
		self.items.sort()
		self.print_book_count()
		self.print_read_book_count(self.items)
		
		for i in self.items:
			new_item = QtWidgets.QListWidgetItem(i[0]+" - "+i[1])
			
			if i[-3] == "yes" and i[-2] == "no":	
				new_item.setBackground(yellow)
			
			elif i[-2] == "yes":
				new_item.setBackground(green)
			window.book_list.addItem(new_item)
			

			
	def print_book_count(self):
		window.book_count.setText(str(self.cursor.execute("SELECT COUNT(*) FROM raflar where bolum != 'arastirma'").fetchone()[0]))

	def print_read_book_count(self,liste):
		read_book_count = 0
		
		for i in liste:
			if i[-2]=="yes":
				read_book_count+=1			

		window.read_count.setText(str(read_book_count))
		
	
	def close_add_book(self):
		window2.book_name.setText("")
		window2.author_name.setText("")
		window2.page_number.setText("")
		window2.own.setChecked(False)
		window2.read.setChecked(False)
		window2.close()
		
	def add_book(self):

		isim = window2.book_name.text()
		yazar = window2.author_name.text()
		yazar = yazar.title()
		sayfa = window2.page_number.text()
		sahip = window2.own.isChecked()
		okundu = window2.read.isChecked()
		bolum = window2.category.currentText()
		
		if bolum == "Novel":
			bolum = "roman"

		if bolum == "Science":
			bolum = "bilim"

		if bolum == "History":
			bolum = "tarih"

		if bolum == "Philosophy":
			bolum = "felsefe"

		if bolum == "Poetry":
			bolum = "siir"

		if bolum == "Personal_evolution":
			bolum = "kisisel_gelisim"

		if bolum == "World_literature":
			bolum = "dunya_edebiyati"

		if bolum == "Turkish_literature":
			bolum = "turk_edebiyati"

		if bolum == "Religion":
			bolum = "din"

		if bolum == "Biography":
			bolum = "biyografi"

		bolum = bolum.replace(" ","_")
		
		if okundu == True:
			okundu = "yes"
		else:
			okundu = "no"
		
		if sahip == True:
			sahip = "yes"
		else:
			sahip = "no"
		
		
		if isim == "" or yazar == "" or sayfa == "" or bolum == "":		
			return None
		
		
		self.cursor.execute("Insert Into raflar Values(?,?,?,?,?,?)",(isim,yazar,sayfa,sahip,okundu,bolum))
		self.con.commit()
		new_item = QtWidgets.QListWidgetItem(isim+" - "+yazar)
			
		if sahip == "yes" and okundu == "no":	
			new_item.setBackground(yellow)
			
		elif okundu == "yes":
			new_item.setBackground(green)
			
		window.book_list.addItem(new_item)
		self.print_book_count()
		self.print_read_book_count(self.items)
		QtWidgets.QMessageBox.information(window2,"bilgi","islem gerceklestirildi!")
		window2.close()
		self.search_book_author()

		window2.book_name.clear()
		window2.author_name.clear()
		window2.page_number.clear()
		window2.own.setChecked(False)
		window2.read.setChecked(False)
		window2.category.setCurrentIndex(-1)
					
				
	def add_book_window(self):

		window2.show()
		window2.add_but.clicked.connect(self.add_book)
		window2.cancel_but.clicked.connect(self.close_add_book)
		
	def filter(self):
		
		filtre_bolum = window.category.currentText()

		if filtre_bolum == "Novel":
			filtre_bolum = "roman"

		if filtre_bolum == "Science":
			filtre_bolum = "bilim"

		if filtre_bolum == "History":
			filtre_bolum = "tarih"

		if filtre_bolum == "Philosophy":
			filtre_bolum = "felsefe"

		if filtre_bolum == "Poetry":
			filtre_bolum = "siir"

		if filtre_bolum == "Personal_evolution":
			filtre_bolum = "kisisel_gelisim"

		if filtre_bolum == "World_literature":
			filtre_bolum = "dunya_edebiyati"

		if filtre_bolum == "Turkish_literature":
			filtre_bolum = "turk_edebiyati"

		if filtre_bolum == "Religion":
			filtre_bolum = "din"

		if filtre_bolum == "Biography":
			filtre_bolum = "biyografi"

		filtre_bolum = filtre_bolum.replace(" ","_")
		
		if filtre_bolum == "All":
			self.place_book()
			return
		
		window.book_list.clear()
		
		self.cursor.execute("Select * From raflar where bolum = ?",(filtre_bolum,))
		
		self.items = self.cursor.fetchall()
		self.items.sort()
		
		for i in self.items:
			new_item = QtWidgets.QListWidgetItem(i[0]+" - "+i[1])
			
			if i[-3] == "yes" and i[-2] == "no":	
				new_item.setBackground(yellow)
			
			elif i[-2] == "yes":
				new_item.setBackground(green)
			window.book_list.addItem(new_item)

		window.book_count.setText(str(len(self.items)))
		self.print_read_book_count(self.items)


	def random_book_recommendation(self):
		try:
		    self.rastgele_liste = []
		        
		    for i in range(window.book_list.count()):
		        self.rastgele_liste.append(window.book_list.item(i).text())
		        
		        
		    kitap = random.choice(self.rastgele_liste)
		        
		    QtWidgets.QMessageBox.information(window,"Random book",kitap)
		except:
			pass

	def search_book_author(self):
		isim = window.search_line.text()
		if isim == "":
			self.place_book()
			return

		else:
			isim = isim.split()
			isim2 = []
			for m in isim:
				if m[0] == "i":
					m = "İ" + m[1:]
		
				else:
					m = m.title()
				isim2.append(m)
				
			isim = " ".join(isim2)

		self.cursor.execute("Select * From raflar where isim like ? and bolum != 'arastirma'",("%"+isim+"%",))
		self.data = self.cursor.fetchall()
		self.cursor.execute("Select * From raflar where yazar like ? and bolum != 'arastirma'",("%"+isim+"%",))
		self.data.extend(self.cursor.fetchall())
		self.data = set(self.data)
		self.data = list(self.data)
		self.data.sort()
			
		window.book_list.clear()
		
		for i in self.data:
			new_item = QtWidgets.QListWidgetItem(i[0]+" - "+i[1])
			
			if i[-3] == "yes" and i[-2] == "no":	
				new_item.setBackground(yellow)
			
			elif i[-2] == "yes":
				new_item.setBackground(green)
			window.book_list.addItem(new_item)
		window.book_count.setText(str(len(self.data)))
		self.print_read_book_count(self.data)


	def save_book_detail(self):
		try:
			self.kitap_sahip = window3.own.isChecked()
			if self.kitap_sahip == True:
				self.kitap_sahip = "yes"
			else:
				self.kitap_sahip = "no"
			self.cursor.execute("Update raflar set sahip = ? where isim = ? and yazar = ?",(self.kitap_sahip,self.data[0],self.data[1]))
			self.con.commit()

			self.kitap_okundu = window3.read.isChecked()
			if self.kitap_okundu == True:
				self.kitap_okundu = "yes"
			else:
				self.kitap_okundu = "no"
			self.cursor.execute("Update raflar set okundu = ? where isim = ? and yazar = ?",(self.kitap_okundu,self.data[0],self.data[1]))
			self.con.commit()

		except:
			pass

		finally:
			window3.close()
			self.search_book_author()


	def delete_book_acceptance(self):
		self.cursor.execute("Delete From raflar where isim = ?",(self.data[0],))
		self.con.commit()
		window4.close()
		window3.close()
		self.search_book_author()
	

	def delete_book_cancellation(self):
		window4.close()


	def delete_book_window(self):
		window4.show()
		
		window4.no.clicked.connect(self.delete_book_cancellation)
		window4.yes.clicked.connect(self.delete_book_acceptance)


	def book_detail_window(self,kitap_):
		
		window3.show()
		self.kitap = kitap_.text().split("-")[0][:-1]
		self.yazar = kitap_.text().split("-")[1][1:]

		self.cursor.execute("Select * From raflar where isim = ? and yazar = ?",(self.kitap,self.yazar))
		self.data = self.cursor.fetchall()[0]
		
		window3.book_name.setText(self.data[0])
		window3.author_name.setText(self.data[1])
		window3.page_number.setText(self.data[2])
		bolum_=self.data[5]

		if bolum_ == "roman":
			bolum_ = "Novel"

		if bolum_ == "bilim":
			bolum_ = "Science"

		if bolum_ == "tarih":
			bolum_ = "History"

		if bolum_ == "felsefe":
			bolum_ = "Philosophy"

		if bolum_ == "siir":
			bolum_ = "Poetry"

		if bolum_ == "kisisel_gelisim":
			bolum_ = "Personal_evolution"

		if bolum_ == "dunya_edebiyati":
			bolum_ = "World_literature"

		if bolum_ == "turk_edebiyati":
			bolum_ = "Turkish_literature"

		if bolum_ == "din":
			bolum_ = "Religion"

		if bolum_ == "biyografi":
			bolum_ = "Biography"

		window3.category.setText(bolum_)

		if self.data[3] == "yes":
			window3.own.setChecked(True)
		else:
			window3.own.setChecked(False)
		
		if self.data[4] == "yes":
			window3.read.setChecked(True)
		else:
			window3.read.setChecked(False)
		
		window3.save_but.clicked.connect(self.save_book_detail)
		window3.delete_but.clicked.connect(self.delete_book_window)


	def research_window(self):
		window5.list.clear()
		self.cursor.execute("Select * From raflar where bolum = ?",("arastirma",))
		self.items_arastirma = self.cursor.fetchall()
		self.items_arastirma.sort()
		
		for i in self.items_arastirma:
			window5.list.addItem(i[0])

		window5.show()
		window5.new.clicked.connect(self.add_research_window)
		window5.delete.clicked.connect(self.delete_research)


	def delete_research(self):
		try:
			arastirma_adi = window5.list.currentItem().text()

			for i in self.items_arastirma:
				if i[0] == arastirma_adi:
					self.cursor.execute("Delete From raflar where isim = ? and bolum = 'arastirma'",(arastirma_adi,))
					self.con.commit()
					self.research_window()
		except:
			pass


	def add_research(self):

		arastirma_ismi = window6.name.text()

		for i in self.items_arastirma:
			if i[0] == arastirma_ismi:
				window6.close()
				return None

		self.cursor.execute("Insert Into raflar Values(?,?,?,?,?,?)",(arastirma_ismi,"_","_","_","_","arastirma"))
		self.con.commit()
		
		window6.name.setText("")
		window6.close()
		self.research_window()

	def close_research(self):
		window6.name.setText("")
		window6.close()

	def add_research_window(self):
		
		window6.show()
		window6.add.clicked.connect(self.add_research)
		window6.cancel.clicked.connect(self.close_research)


library = Library()
	
try:

	app = QtWidgets.QApplication(sys.argv)
	window = Ui_MAIN()
	window2 = Ui_ADD_BOOK()
	window3 = Ui_BOOK_DETAIL()
	window4 = Ui_DELETE_BOOK()
	window5 = Ui_RESEARCH()
	window6 = Ui_RESEARCH_ADD()
	library.place_book()
	window.show()
	
	
	
	window.add_but.clicked.connect(library.add_book_window)
	window.random_but.clicked.connect(library.random_book_recommendation)
	window.filter_but.clicked.connect(library.filter)
	window.search_but.clicked.connect(library.search_book_author)
	window.search_line.returnPressed.connect(window.search_but.click)
	window.book_list.itemDoubleClicked.connect(library.book_detail_window)
	window.research_but.clicked.connect(library.research_window)
	window6.name.returnPressed.connect(library.add_research)



	sys.exit(app.exec_())
	

finally:
	library.kill_connection()
