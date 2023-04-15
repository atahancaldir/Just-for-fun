# HoldMyRover takımı tarafından CodeMamak Hackathon'u için oluşturuldu!
# 17.05.2020

from guiIsletme import *
import time
import sqlite3 as sq
from datetime import datetime

class Sistem():
    def __init__(self):
        self.baglanti_baslat()
        self.masaNo = 0
        self.mekanAdi = "Cafe 24"

    def baglanti_baslat(self):
        self.con = sq.connect("veritabani.db")

        self.cursor = self.con.cursor()
		
        self.cursor.execute("CREATE TABLE IF NOT EXISTS kisiBilgileri(isim TEXT,soyad TEXT,yas TEXT,tc TEXT,cinsiyet TEXT,hastalik TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS kisiHareketleri(isim TEXT,soyad TEXT,tc TEXT,mekan TEXT,masa Text,durum TEXT,tarih TEXT)")

        self.con.commit()

    def baglanti_kopar(self):
        self.con.close()

    def girisIslemi(self):
        window.close()
        window2.show()

        window2.tcOnay.clicked.connect(sistem.girisOnay)

        window2.masa1.clicked.connect(self.masaAyarla1)
        window2.masa2.clicked.connect(self.masaAyarla2)
        window2.masa3.clicked.connect(self.masaAyarla3)
        window2.masa4.clicked.connect(self.masaAyarla4)
        window2.masa5.clicked.connect(self.masaAyarla5)
        window2.masa6.clicked.connect(self.masaAyarla6)
        window2.masa7.clicked.connect(self.masaAyarla7)
        window2.masa8.clicked.connect(self.masaAyarla8)
        window2.masa9.clicked.connect(self.masaAyarla9)
        window2.masa10.clicked.connect(self.masaAyarla10)
        window2.masa11.clicked.connect(self.masaAyarla11)
        window2.masa12.clicked.connect(self.masaAyarla12)

    def cikisIslemi(self):
        window.close()
        window5.show()

        window5.pushButton.clicked.connect(self.cikisOnay)

    def cikisOnay(self):
        self.cursor.execute("Select * From kisiBilgileri where tc = ?",(window5.lineEdit.text(),))

        self.bilgiler = self.cursor.fetchall()[0]

        self.current_time = datetime.now().strftime("%d.%m.%Y/%H:%M:%S")

        self.cursor.execute("INSERT INTO kisiHareketleri VALUES(?, ?, ?, ?, ?, ?, ?)",(self.bilgiler[0],self.bilgiler[1],self.bilgiler[3],self.mekanAdi,"-","Çıkış",self.current_time))
        self.con.commit()

        window5.close()
        window4.label_3.setText("Çıkış işleminiz başarıyla gerçekleşti. İyi günler!")
        window4.show()

    def girisOnay(self):
        self.cursor.execute("Select * From kisiBilgileri where tc = ?",(window2.lineEdit.text(),))
        self.bilgiler = self.cursor.fetchall()[0]
        
        if self.bilgiler[-1] == "Pozitif":
            window2.close()
            window3.show()
        
        else:
            window2.cafeFrame.setEnabled(True)
            window2.label_9.show()

    def masaAyarla1(self):
        self.masaNo = 1
        self.hareketEkle()

    def masaAyarla2(self):
        self.masaNo = 2
        self.hareketEkle()

    def masaAyarla3(self):
        self.masaNo = 3
        self.hareketEkle()

    def masaAyarla4(self):
        self.masaNo = 4
        self.hareketEkle()

    def masaAyarla5(self):
        self.masaNo = 5
        self.hareketEkle()

    def masaAyarla6(self):
        self.masaNo = 6
        self.hareketEkle()

    def masaAyarla7(self):
        self.masaNo = 7
        self.hareketEkle()

    def masaAyarla8(self):
        self.masaNo = 8
        self.hareketEkle()

    def masaAyarla9(self):
        self.masaNo = 9
        self.hareketEkle()

    def masaAyarla10(self):
        self.masaNo = 10
        self.hareketEkle()

    def masaAyarla11(self):
        self.masaNo = 11
        self.hareketEkle()

    def masaAyarla12(self):
        self.masaNo = 12
        self.hareketEkle()

    def hareketEkle(self):
        self.current_time = datetime.now().strftime("%d.%m.%Y/%H:%M:%S")

        self.cursor.execute("INSERT INTO kisiHareketleri VALUES(?, ?, ?, ?, ?, ?, ?)",(self.bilgiler[0],self.bilgiler[1],self.bilgiler[3],self.mekanAdi,"No "+str(self.masaNo),"Giriş",self.current_time))
        self.con.commit()

        window2.close()
        window4.label_3.setText("Giriş işleminiz başarıyla gerçekleşti. İyi eğlenceler!")
        window4.show()



sistem = Sistem()

try:

    app = QtWidgets.QApplication(sys.argv)
    window = Ui_musteriEkrani()
    window2 = Ui_masaSecimEkrani()
    window3 = Ui_uyariMesaji()
    window4 = Ui_bilgiMesaji()
    window5 = Ui_cikisEkrani()
    window.show()

    window.girisBut.clicked.connect(sistem.girisIslemi)
    window.cikisBut.clicked.connect(sistem.cikisIslemi)

    sys.exit(app.exec_())
	

finally:
    sistem.baglanti_kopar()
