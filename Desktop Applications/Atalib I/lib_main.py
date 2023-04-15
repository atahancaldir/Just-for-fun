from arayuz import *
import random
import sqlite3 as sq


class Kutuphane():
	def __init__(self):
		self.baglanti_kur()
		
		
	def baglanti_kur(self):
		self.con = sq.connect("kitaplik2.db")
		self.cursor = self.con.cursor()
		
		self.cursor.execute("CREATE TABLE IF NOT EXISTS raflar(isim TEXT,yazar TEXT,sayfa TEXT,sahip TEXT,okundu TEXT,bolum TEXT)")
		self.con.commit()
		
	def baglanti_kes(self):
		self.con.close()
		
	def kitap_yerlestir(self):
		pencere.kitap_listesi.clear()
		self.cursor.execute("Select * From raflar where bolum != 'arastirma'")
		self.items = self.cursor.fetchall()
		self.items.sort()
		self.kitap_sayisi_bastir()
		self.okunan_kitap_sayisi_bastir(self.items)
		
		for i in self.items:
			new_item = QtWidgets.QListWidgetItem(i[0]+" - "+i[1])
			
			if i[-3] == "yes" and i[-2] == "no":	
				new_item.setBackground(yellow)
			
			elif i[-2] == "yes":
				new_item.setBackground(green)
			pencere.kitap_listesi.addItem(new_item)
			

			
	def kitap_sayisi_bastir(self):
		pencere.kitap_sayisi.display(self.cursor.execute("SELECT COUNT(*) FROM raflar where bolum != 'arastirma'").fetchone()[0])

	def okunan_kitap_sayisi_bastir(self,liste):
		okunan_count = 0
		
		for i in liste:
			if i[-2]=="yes":
				okunan_count+=1			

		pencere.okunan.display(okunan_count)
		
	
	def kitap_ekle_kapat(self):
		pencere2.kitap_adi.setText("")
		pencere2.yazar_adi.setText("")
		pencere2.sayfa_sayisi.setText("")
		pencere2.sahip_durum.setChecked(False)
		pencere2.okuma_durum.setChecked(False)
		pencere2.close()
		
	def kitap_ekle(self):

		isim = pencere2.kitap_adi.text()
		yazar = pencere2.yazar_adi.text()
		yazar = yazar.title()
		sayfa = pencere2.sayfa_sayisi.text()
		sahip = pencere2.sahip_durum.isChecked()
		okundu = pencere2.okuma_durum.isChecked()
		bolum = pencere2.bolumler.currentText()
		
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
			
		pencere.kitap_listesi.addItem(new_item)
		self.kitap_sayisi_bastir()
		self.okunan_kitap_sayisi_bastir(self.items)
		QtWidgets.QMessageBox.information(pencere2,"bilgi","islem gerceklestirildi!")
		pencere2.close()
		self.kitap_yazar_sorgula()

		pencere2.kitap_adi.clear()
		pencere2.yazar_adi.clear()
		pencere2.sayfa_sayisi.clear()
		pencere2.sahip_durum.setChecked(False)
		pencere2.okuma_durum.setChecked(False)
		pencere2.bolumler.setCurrentIndex(-1)
					
				
	def kitap_ekle_pencere(self):

		pencere2.show()
		pencere2.ekle.clicked.connect(self.kitap_ekle)
		pencere2.vazgec.clicked.connect(self.kitap_ekle_kapat)
		
	def filtrele(self):
		
		filtre_bolum = pencere.bolumler.currentText()
		filtre_bolum = filtre_bolum.replace(" ","_")
		
		if filtre_bolum == "hepsi":
			self.kitap_yerlestir()
			return
		
		pencere.kitap_listesi.clear()
		
		self.cursor.execute("Select * From raflar where bolum = ?",(filtre_bolum,))
		
		self.items = self.cursor.fetchall()
		self.items.sort()
		
		for i in self.items:
			new_item = QtWidgets.QListWidgetItem(i[0]+" - "+i[1])
			
			if i[-3] == "yes" and i[-2] == "no":	
				new_item.setBackground(yellow)
			
			elif i[-2] == "yes":
				new_item.setBackground(green)
			pencere.kitap_listesi.addItem(new_item)

		pencere.kitap_sayisi.display(len(self.items))
		self.okunan_kitap_sayisi_bastir(self.items)


	def rastgele_kitap_oner(self):
		
		self.rastgele_liste = []
			
		for i in range(pencere.kitap_listesi.count()):
			self.rastgele_liste.append(pencere.kitap_listesi.item(i).text())
			
			
		kitap = random.choice(self.rastgele_liste)
			
		QtWidgets.QMessageBox.information(pencere,"rastgele kitap",kitap)
				
	def kitap_yazar_sorgula(self):
		isim = pencere.arama.text()
		if isim == "":
			self.kitap_yerlestir()
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
			
		pencere.kitap_listesi.clear()
		
		for i in self.data:
			new_item = QtWidgets.QListWidgetItem(i[0]+" - "+i[1])
			
			if i[-3] == "yes" and i[-2] == "no":	
				new_item.setBackground(yellow)
			
			elif i[-2] == "yes":
				new_item.setBackground(green)
			pencere.kitap_listesi.addItem(new_item)
		pencere.kitap_sayisi.display(len(self.data))
		self.okunan_kitap_sayisi_bastir(self.data)


	def kitap_detay_kaydet(self):
		try:
			self.kitap_sahip = pencere3.kitap_detay_sahip.isChecked()
			if self.kitap_sahip == True:
				self.kitap_sahip = "yes"
			else:
				self.kitap_sahip = "no"
			self.cursor.execute("Update raflar set sahip = ? where isim = ? and yazar = ?",(self.kitap_sahip,self.data[0],self.data[1]))
			self.con.commit()

			self.kitap_okundu = pencere3.kitap_detay_okundu.isChecked()
			if self.kitap_okundu == True:
				self.kitap_okundu = "yes"
			else:
				self.kitap_okundu = "no"
			self.cursor.execute("Update raflar set okundu = ? where isim = ? and yazar = ?",(self.kitap_okundu,self.data[0],self.data[1]))
			self.con.commit()

		except:
			pass

		finally:
			pencere3.close()
			self.kitap_yazar_sorgula()


	def kitap_sil_onay(self):
		self.cursor.execute("Delete From raflar where isim = ?",(self.data[0],))
		self.con.commit()
		pencere4.close()
		pencere3.close()
		self.kitap_yazar_sorgula()
	

	def kitap_sil_iptal(self):
		pencere4.close()


	def kitap_sil_pencere(self):
		pencere4.show()
		
		pencere4.hayir_tus.clicked.connect(self.kitap_sil_iptal)
		pencere4.evet_tus.clicked.connect(self.kitap_sil_onay)


	def kitap_detay_pencere(self,kitap_):
		
		pencere3.show()
		self.kitap = kitap_.text().split("-")[0][:-1]
		self.yazar = kitap_.text().split("-")[1][1:]

		self.cursor.execute("Select * From raflar where isim = ? and yazar = ?",(self.kitap,self.yazar))
		self.data = self.cursor.fetchall()[0]
		
		pencere3.label.setText(self.data[0])
		pencere3.kitap_detay_yazar.setText(self.data[1])
		pencere3.kitap_detay_sayfa.setText(self.data[2])
		pencere3.kitap_detay_bolum.setText(self.data[5])

		if self.data[3] == "yes":
			pencere3.kitap_detay_sahip.setChecked(True)
		else:
			pencere3.kitap_detay_sahip.setChecked(False)
		
		if self.data[4] == "yes":
			pencere3.kitap_detay_okundu.setChecked(True)
		else:
			pencere3.kitap_detay_okundu.setChecked(False)
		
		pencere3.kitap_detay_tus.clicked.connect(self.kitap_detay_kaydet)
		pencere3.kitap_detay_sil.clicked.connect(self.kitap_sil_pencere)


	def arastirma_pencere(self):
		pencere5.arastirma_liste.clear()
		self.cursor.execute("Select * From raflar where bolum = ?",("arastirma",))
		self.items_arastirma = self.cursor.fetchall()
		self.items_arastirma.sort()
		
		for i in self.items_arastirma:
			pencere5.arastirma_liste.addItem(i[0])

		pencere5.show()
		pencere5.arastirma_yeni.clicked.connect(self.arastirma_ekle_pencere)
		pencere5.arastirma_sil.clicked.connect(self.arastirma_silme)


	def arastirma_silme(self):
		try:
			arastirma_adi = pencere5.arastirma_liste.currentItem().text()

			for i in self.items_arastirma:
				if i[0] == arastirma_adi:
					self.cursor.execute("Delete From raflar where isim = ? and bolum = 'arastirma'",(arastirma_adi,))
					self.con.commit()
					self.arastirma_pencere()
		except:
			pass


	def arastirma_ekle(self):

		arastirma_ismi = pencere6.arastirma_konu.text()

		for i in self.items_arastirma:
			if i[0] == arastirma_ismi:
				pencere6.close()
				return None

		self.cursor.execute("Insert Into raflar Values(?,?,?,?,?,?)",(arastirma_ismi,"_","_","_","_","arastirma"))
		self.con.commit()
		
		pencere6.arastirma_konu.setText("")
		pencere6.close()
		self.arastirma_pencere()

	def arastirma_kapat(self):
		pencere6.arastirma_konu.setText("")
		pencere6.close()

	def arastirma_ekle_pencere(self):
		
		pencere6.show()
		pencere6.arastirma_ekle.clicked.connect(self.arastirma_ekle)
		pencere6.arastirma_vazgec.clicked.connect(self.arastirma_kapat)


kutuphane = Kutuphane()
	
try:

	uygulama = QtWidgets.QApplication(sys.argv)
	pencere = Ui_Form()
	pencere2 = Ui_kitap_ekle_pencere()
	pencere3 = Ui_kitap_detay_isim()
	pencere4 = Ui_kitap_sil()
	pencere5 = Ui_arastirma()
	pencere6 = Ui_arastirma_ekle_pencere()
	kutuphane.kitap_yerlestir()
	pencere.show()
	
	
	
	pencere.kitap_ekle.clicked.connect(kutuphane.kitap_ekle_pencere)
	pencere.rastgele_kitap.clicked.connect(kutuphane.rastgele_kitap_oner)
	pencere.filtre.clicked.connect(kutuphane.filtrele)
	pencere.ara_tusu.clicked.connect(kutuphane.kitap_yazar_sorgula)
	pencere.arama.returnPressed.connect(pencere.ara_tusu.click)
	pencere.kitap_listesi.itemDoubleClicked.connect(kutuphane.kitap_detay_pencere)
	pencere.arastirma_tus.clicked.connect(kutuphane.arastirma_pencere)
	pencere6.arastirma_konu.returnPressed.connect(kutuphane.arastirma_ekle)



	sys.exit(uygulama.exec_())
	

finally:
	kutuphane.baglanti_kes()
