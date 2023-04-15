# HoldMyRover takımı tarafından CodeMamak Hackathon'u için oluşturuldu!
# 17.05.2020

from guiBakanlik import *
import sqlite3 as sq

class System():
    def __init__(self):
        self.baglanti_baslat()

    def baglanti_baslat(self):
        self.con = sq.connect("veritabani.db")

        self.cursor = self.con.cursor()
		
        self.cursor.execute("CREATE TABLE IF NOT EXISTS kisiBilgileri(isim TEXT,soyad TEXT,yas TEXT,tc TEXT,cinsiyet TEXT,hastalik TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS kisiHareketleri(isim TEXT,soyad TEXT,tc TEXT,mekan TEXT,masa Text,durum TEXT,tarih TEXT)")

        self.con.commit()

    def baglanti_kopar(self):
        self.con.close()

    def sorguIslemi(self):
        self.cursor.execute("Select * From kisiBilgileri where tc = ?",(window.lineEdit.text(),))
        self.bilgiler = self.cursor.fetchall()[0]

        window.isimSoyisim.setText(self.bilgiler[0]+" "+self.bilgiler[1])
        window.cinsiyet.setText(self.bilgiler[4])
        window.yas.setText(self.bilgiler[2])
        window.hastalikDurumu.setText(self.bilgiler[-1])

        self.cursor.execute("Select * From kisiHareketleri where tc = ?",(window.lineEdit.text(),))
        self.bilgiler2 = self.cursor.fetchall()

        window.tablo.setRowCount(len(self.bilgiler2))
        
        for i in range(len(self.bilgiler2)):
            for j in range(4):
                window.tablo.setItem(i,j, QTableWidgetItem(self.bilgiler2[i][j+3]))

sistem = System()

try:
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_hastaSorgu()
    window.show()

    window.sorgulaBut.clicked.connect(sistem.sorguIslemi)

    sys.exit(app.exec_())

finally:
    sistem.baglanti_kopar()