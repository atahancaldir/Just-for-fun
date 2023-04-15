# -*- coding: utf-8 -*-

# Created by Atahan Caldir


from PyQt5 import QtCore, QtGui, QtWidgets
import sys


yellow = QtGui.QBrush(QtCore.Qt.yellow)
green = QtGui.QBrush(QtCore.Qt.green)


class Ui_arastirma(QtWidgets.QWidget):

	def __init__(self):
		QtWidgets.QWidget.__init__(self)
		self.setupUi(self)

	def setupUi(self, arastirma):
		arastirma.setObjectName("arastirma")
		arastirma.setWindowModality(QtCore.Qt.NonModal)
		arastirma.resize(406, 450)
		arastirma.setMinimumSize(QtCore.QSize(406, 450))
		arastirma.setMaximumSize(QtCore.QSize(406, 450))
		self.arastirma_liste = QtWidgets.QListWidget(arastirma)
		self.arastirma_liste.setGeometry(QtCore.QRect(10, 10, 391, 391))
		self.arastirma_liste.setProperty("isWrapping", False)
		self.arastirma_liste.setUniformItemSizes(False)
		self.arastirma_liste.setObjectName("arastirma_liste")
		self.arastirma_yeni = QtWidgets.QPushButton(arastirma)
		self.arastirma_yeni.setGeometry(QtCore.QRect(75, 410, 111, 27))
		self.arastirma_yeni.setObjectName("arastirma_yeni")
		self.arastirma_yeni.setStyleSheet("background-color: orange;border-style: outset;border-width: 2px;border-color: black;padding: 4px;")
		self.arastirma_sil = QtWidgets.QPushButton(arastirma)
		self.arastirma_sil.setGeometry(QtCore.QRect(240, 410, 111, 27))
		self.arastirma_sil.setObjectName("arastirma_sil")
		self.arastirma_sil.setStyleSheet("background-color: orange;border-style: outset;border-width: 2px;border-color: black;padding: 4px;")

		self.retranslateUi(arastirma)
		QtCore.QMetaObject.connectSlotsByName(arastirma)

	def retranslateUi(self, arastirma):
		_translate = QtCore.QCoreApplication.translate
		arastirma.setWindowTitle(_translate("arastirma", "arastirma konulari"))
		self.arastirma_yeni.setText(_translate("arastirma", "yeni"))
		self.arastirma_sil.setText(_translate("arastirma", "sil"))

class Ui_arastirma_ekle_pencere(QtWidgets.QWidget):

	def __init__(self):
		QtWidgets.QWidget.__init__(self)
		self.setupUi(self)

	def setupUi(self, arastirma_ekle_pencere):
		arastirma_ekle_pencere.setObjectName("arastirma_ekle_pencere")
		arastirma_ekle_pencere.resize(400, 116)
		arastirma_ekle_pencere.setMinimumSize(QtCore.QSize(400, 116))
		arastirma_ekle_pencere.setMaximumSize(QtCore.QSize(400, 116))
		self.arastirma_ekle = QtWidgets.QPushButton(arastirma_ekle_pencere)
		self.arastirma_ekle.setGeometry(QtCore.QRect(220, 80, 99, 27))
		self.arastirma_ekle.setStyleSheet("background-color: orange;border-style: outset;border-width: 2px;border-color: black;padding: 4px;")
		self.arastirma_ekle.setObjectName("arastirma_ekle")
		self.arastirma_vazgec = QtWidgets.QPushButton(arastirma_ekle_pencere)
		self.arastirma_vazgec.setGeometry(QtCore.QRect(70, 80, 99, 27))
		self.arastirma_vazgec.setObjectName("arastirma_vazgec")
		self.arastirma_vazgec.setStyleSheet("background-color: orange;border-style: outset;border-width: 2px;border-color: black;padding: 4px;")
		self.arastirma_konu = QtWidgets.QLineEdit(arastirma_ekle_pencere)
		self.arastirma_konu.setGeometry(QtCore.QRect(10, 20, 371, 27))
		self.arastirma_konu.setObjectName("arastirma_konu")

		self.retranslateUi(arastirma_ekle_pencere)
		QtCore.QMetaObject.connectSlotsByName(arastirma_ekle_pencere)

	def retranslateUi(self, arastirma_ekle_pencere):
		_translate = QtCore.QCoreApplication.translate
		arastirma_ekle_pencere.setWindowTitle(_translate("arastirma_ekle_pencere", "arastirma ekle"))
		self.arastirma_ekle.setText(_translate("arastirma_ekle_pencere", "ekle"))
		self.arastirma_vazgec.setText(_translate("arastirma_ekle_pencere", "vazgec"))



class Ui_kitap_sil(QtWidgets.QWidget):

	def __init__(self):
		QtWidgets.QWidget.__init__(self)
		self.setupUi(self)


	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(400, 115)
		self.evet_tus = QtWidgets.QPushButton(Form)
		self.evet_tus.setGeometry(QtCore.QRect(90, 70, 99, 27))
		self.evet_tus.setObjectName("evet_tus")
		self.evet_tus.setStyleSheet("background-color: orange;border-style: outset;border-width: 2px;border-color: black;padding: 4px;")
		self.hayir_tus = QtWidgets.QPushButton(Form)
		self.hayir_tus.setGeometry(QtCore.QRect(200, 70, 99, 27))
		self.hayir_tus.setMinimumSize(QtCore.QSize(99, 27))
		self.hayir_tus.setMaximumSize(QtCore.QSize(99, 27))
		self.hayir_tus.setObjectName("hayir_tus")
		self.hayir_tus.setStyleSheet("background-color: orange;border-style: outset;border-width: 2px;border-color: black;padding: 4px;")
		self.label = QtWidgets.QLabel(Form)
		self.label.setGeometry(QtCore.QRect(30, 10, 351, 51))
		font = QtGui.QFont()
		font.setFamily("URW Gothic L")
		font.setPointSize(16)
		font.setItalic(True)
		self.label.setFont(font)
		self.label.setObjectName("label")

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "kitap sil"))
		self.evet_tus.setText(_translate("Form", "evet"))
		self.hayir_tus.setText(_translate("Form", "hayir"))
		self.label.setText(_translate("Form", "kitabi silmek istedigine emin misin?"))


class Ui_kitap_ekle_pencere(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi_(self)


    def setupUi_(self, kitap_ekle_pencere):
        kitap_ekle_pencere.setObjectName("kitap_ekle_pencere")
        kitap_ekle_pencere.resize(377, 280)
        kitap_ekle_pencere.setMinimumSize(QtCore.QSize(377, 280))
        kitap_ekle_pencere.setMaximumSize(QtCore.QSize(377, 280))
        self.label = QtWidgets.QLabel(kitap_ekle_pencere)
        self.label.setGeometry(QtCore.QRect(20, 30, 81, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(kitap_ekle_pencere)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 81, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(kitap_ekle_pencere)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 81, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(kitap_ekle_pencere)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 81, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(kitap_ekle_pencere)
        self.label_5.setGeometry(QtCore.QRect(20, 190, 81, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(kitap_ekle_pencere)
        self.label_6.setGeometry(QtCore.QRect(20, 230, 81, 17))
        self.label_6.setObjectName("label_6")
        self.kitap_adi = QtWidgets.QLineEdit(kitap_ekle_pencere)
        self.kitap_adi.setGeometry(QtCore.QRect(110, 30, 251, 21))
        self.kitap_adi.setObjectName("kitap_adi")
        self.yazar_adi = QtWidgets.QLineEdit(kitap_ekle_pencere)
        self.yazar_adi.setGeometry(QtCore.QRect(110, 70, 251, 21))
        self.yazar_adi.setObjectName("yazar_adi")
        self.sayfa_sayisi = QtWidgets.QLineEdit(kitap_ekle_pencere)
        self.sayfa_sayisi.setGeometry(QtCore.QRect(110, 110, 251, 21))
        self.sayfa_sayisi.setObjectName("sayfa_sayisi")
        self.bolumler = QtWidgets.QComboBox(kitap_ekle_pencere)
        self.bolumler.setGeometry(QtCore.QRect(110, 150, 150, 25))
        self.bolumler.setObjectName("bolumler")
        self.bolumler.addItems([" ","roman","bilim","tarih","felsefe","kisisel gelisim","dunya edebiyati","siir","turk edebiyati","din","biyografi"])
        self.sahip_durum = QtWidgets.QCheckBox(kitap_ekle_pencere)
        self.sahip_durum.setGeometry(QtCore.QRect(120, 190, 21, 22))
        self.sahip_durum.setText("")
        self.sahip_durum.setObjectName("sahip_durum")
        self.okuma_durum = QtWidgets.QCheckBox(kitap_ekle_pencere)
        self.okuma_durum.setGeometry(QtCore.QRect(120, 230, 21, 22))
        self.okuma_durum.setText("")
        self.okuma_durum.setObjectName("okuma_durum")
        self.vazgec = QtWidgets.QPushButton(kitap_ekle_pencere)
        self.vazgec.setGeometry(QtCore.QRect(270, 180, 99, 27))
        self.vazgec.setObjectName("vazgec")
        self.vazgec.setStyleSheet("background-color: orange;border-style: outset;border-width: 2px;border-color: black;padding: 4px;")
        self.ekle = QtWidgets.QPushButton(kitap_ekle_pencere)
        self.ekle.setGeometry(QtCore.QRect(270, 150, 99, 27))
        self.ekle.setObjectName("ekle")
        self.ekle.setStyleSheet("background-color: orange;border-style: outset;border-width: 2px;border-color: black;padding: 4px;")

        self.retranslateUi_(kitap_ekle_pencere)
        QtCore.QMetaObject.connectSlotsByName(kitap_ekle_pencere)

    def retranslateUi_(self, kitap_ekle_pencere):
        _translate = QtCore.QCoreApplication.translate
        kitap_ekle_pencere.setWindowTitle(_translate("kitap_ekle_pencere", "kitap ekle"))
        self.label.setText(_translate("kitap_ekle_pencere", "kitap adi:"))
        self.label_2.setText(_translate("kitap_ekle_pencere", "yazar:"))
        self.label_3.setText(_translate("kitap_ekle_pencere", "sayfa sayisi:"))
        self.label_4.setText(_translate("kitap_ekle_pencere", "bolum:"))
        self.label_5.setText(_translate("kitap_ekle_pencere", "sahip misin:"))
        self.label_6.setText(_translate("kitap_ekle_pencere", "okudun mu:"))
        self.vazgec.setText(_translate("kitap_ekle_pencere", "vazgec"))
        self.ekle.setText(_translate("kitap_ekle_pencere", "ekle"))


class Ui_kitap_detay_isim(QtWidgets.QWidget):

	def __init__(self):
		QtWidgets.QWidget.__init__(self)
		self.setupUi__(self)
	
	def setupUi__(self, kitap_detay_isim):
		kitap_detay_isim.setObjectName("kitap_detay_isim")
	#478,257 idi
		kitap_detay_isim.resize(500, 350)
		kitap_detay_isim.setMinimumSize(QtCore.QSize(500, 350))
		kitap_detay_isim.setMaximumSize(QtCore.QSize(500, 350))
		self.label = QtWidgets.QLabel(kitap_detay_isim)
		self.label.setGeometry(QtCore.QRect(10, 10, 650, 51))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.label.setFont(font)
		self.label.setText("")
		self.label.setObjectName("kitap_detay_kitap_adi")
		self.kitap_detay_yazar = QtWidgets.QLabel(kitap_detay_isim)
		self.kitap_detay_yazar.setGeometry(QtCore.QRect(10, 80, 650, 41))
		font = QtGui.QFont()
		font.setItalic(True)
		self.kitap_detay_yazar.setFont(font)
		self.kitap_detay_yazar.setText("")
		self.kitap_detay_yazar.setObjectName("kitap_detay_yazar")
		self.kitap_detay_sayfa = QtWidgets.QLabel(kitap_detay_isim)
		self.kitap_detay_sayfa.setGeometry(QtCore.QRect(200, 150, 451, 41))
		font = QtGui.QFont()
		font.setFamily("Purisa")
		font.setPointSize(16)
		self.kitap_detay_sayfa.setFont(font)
		self.kitap_detay_sayfa.setText("")
		self.kitap_detay_sayfa.setObjectName("kitap_detay_sayfa")
		self.kitap_detay_bolum = QtWidgets.QLabel(kitap_detay_isim)
		self.kitap_detay_bolum.setGeometry(QtCore.QRect(10, 150, 451, 41))
		self.kitap_detay_bolum.setFont(font)
		self.kitap_detay_bolum.setText("")
		self.kitap_detay_bolum.setObjectName("kitap_detay_bolum")
		self.label_4 = QtWidgets.QLabel(kitap_detay_isim)
		self.label_4.setGeometry(QtCore.QRect(10, 10, 67, 17))
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(kitap_detay_isim)
		self.label_5.setGeometry(QtCore.QRect(10, 70, 67, 17))
		self.label_5.setObjectName("label_5")
		self.label_6 = QtWidgets.QLabel(kitap_detay_isim)
		self.label_6.setGeometry(QtCore.QRect(200, 140, 81, 17))
		self.label_6.setObjectName("label_6")
		self.label_7 = QtWidgets.QLabel(kitap_detay_isim)
		self.label_7.setGeometry(QtCore.QRect(10, 140, 81, 17))
		self.label_7.setObjectName("label_6")
		self.kitap_detay_sahip = QtWidgets.QCheckBox(kitap_detay_isim)
		self.kitap_detay_sahip.setGeometry(QtCore.QRect(10, 210, 97, 22))
		self.kitap_detay_sahip.setObjectName("kitap_detay_sahip")
		self.kitap_detay_okundu = QtWidgets.QCheckBox(kitap_detay_isim)
		self.kitap_detay_okundu.setGeometry(QtCore.QRect(130, 210, 97, 22))
		self.kitap_detay_okundu.setObjectName("kitap_detay_okundu")
		self.kitap_detay_tus = QtWidgets.QPushButton(kitap_detay_isim)
		self.kitap_detay_tus.setGeometry(QtCore.QRect(10, 270, 121, 27))
		self.kitap_detay_tus.setObjectName("kitap_detay_tus")
		self.kitap_detay_tus.setStyleSheet("background-color: orange;border-style: outset;border-width: 2px;border-color: black;padding: 4px;")
		self.kitap_detay_sil = QtWidgets.QPushButton(kitap_detay_isim)
		self.kitap_detay_sil.setGeometry(QtCore.QRect(140, 270, 80, 27))
		self.kitap_detay_sil.setObjectName("kitap_detay_sil")
		self.kitap_detay_sil.setStyleSheet("background-color: orange;border-style: outset;border-width: 2px;border-color: black;padding: 4px;")
		self.retranslateUi__(kitap_detay_isim)
		QtCore.QMetaObject.connectSlotsByName(kitap_detay_isim)

	def retranslateUi__(self, kitap_detay_isim):
		_translate = QtCore.QCoreApplication.translate
		kitap_detay_isim.setWindowTitle(_translate("kitap_detay_isim", "kitap detaylari"))
		self.label_4.setText(_translate("kitap_detay_isim", "kitap adi:"))
		self.label_5.setText(_translate("kitap_detay_isim", "yazar:"))
		self.label_6.setText(_translate("kitap_detay_isim", "sayfa sayisi:"))
		self.label_7.setText(_translate("kitap_detay_isim", "kategori:"))
		self.kitap_detay_sahip.setText(_translate("kitap_detay_isim", "sahip"))
		self.kitap_detay_okundu.setText(_translate("kitap_detay_isim", "okundu"))
		self.kitap_detay_tus.setText(_translate("kitap_detay_isim", "kaydet ve kapat"))
		self.kitap_detay_sil.setText(_translate("kitap_detay_isim", "kitabi sil"))



class Ui_Form(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowIcon(QtGui.QIcon('img/icon.png'))
        Form.setEnabled(True)
        Form.resize(667, 448)
        Form.setMinimumSize(QtCore.QSize(667, 448))
        Form.setMaximumSize(QtCore.QSize(667, 448))
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 651, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.arama = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.arama.setObjectName("arama")
        self.horizontalLayout.addWidget(self.arama)
        self.ara_tusu = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ara_tusu.setObjectName("ara_tusu")
        self.ara_tusu.setStyleSheet("background-color: orange;border-style: outset;border-width: 2px;border-color: black;padding: 4px;")
        self.horizontalLayout.addWidget(self.ara_tusu)
        self.kitap_listesi = QtWidgets.QListWidget(Form)
        self.kitap_listesi.setGeometry(QtCore.QRect(10, 60, 531, 371))
        self.kitap_listesi.setProperty("isWrapping", False)
        self.kitap_listesi.setUniformItemSizes(False)
        self.kitap_listesi.setObjectName("kitap_listesi")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(550, 60, 67, 21))
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.bolumler = QtWidgets.QComboBox(Form)
        self.bolumler.setGeometry(QtCore.QRect(550, 80, 111, 27))
        self.bolumler.setObjectName("bolumler")
        self.bolumler.addItems(["hepsi","roman","bilim","tarih","siir","kisisel gelisim","felsefe","dunya edebiyati","turk edebiyati","din","biyografi"])
        self.filtre = QtWidgets.QPushButton(Form)
        self.filtre.setGeometry(QtCore.QRect(550, 110, 111, 27))
        self.filtre.setObjectName("filtre")
        self.filtre.setStyleSheet("background-color: orange;border-style: outset;border-width: 2px;border-color: black;padding: 4px;")
        self.kitap_ekle = QtWidgets.QPushButton(Form)
        self.kitap_ekle.setGeometry(QtCore.QRect(550, 290, 111, 27))
        self.kitap_ekle.setObjectName("kitap_ekle")
        self.kitap_ekle.setStyleSheet("background-color: orange;border-style: outset;border-width: 2px;border-color: black;padding: 4px;")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(550, 152, 91, 21))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(550, 220, 91, 21))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(550, 320, 91, 21))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setObjectName("label_2")
        self.kitap_sayisi = QtWidgets.QLCDNumber(Form)
        self.kitap_sayisi.setEnabled(True)
        self.kitap_sayisi.setGeometry(QtCore.QRect(550, 173, 64, 23))
        self.kitap_sayisi.setObjectName("kitap_sayisi")
        self.kitap_sayisi.setStyleSheet("""QLCDNumber { background-color: blue; color: white; }""")
        self.okunan = QtWidgets.QLCDNumber(Form)
        self.okunan.setEnabled(True)
        self.okunan.setGeometry(QtCore.QRect(550, 241, 64, 23))
        self.okunan.setObjectName("okunan")
        self.okunan.setStyleSheet("""QLCDNumber { background-color: green; color: white; }""")
        self.rastgele_kitap = QtWidgets.QPushButton(Form)
        self.rastgele_kitap.setGeometry(QtCore.QRect(550, 330, 111, 27))
        self.rastgele_kitap.setObjectName("rastgele_kitap")
        self.rastgele_kitap.setStyleSheet("background-color: orange;border-style: outset;border-width: 2px;border-color: black;padding: 4px;")
        self.arastirma_tus = QtWidgets.QPushButton(Form)
        self.arastirma_tus.setGeometry(QtCore.QRect(550, 370, 111, 27))
        self.arastirma_tus.setObjectName("rastgele_kitap")
        self.arastirma_tus.setStyleSheet("background-color: orange;border-style: outset;border-width: 2px;border-color: black;padding: 4px;")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ata library"))
        self.ara_tusu.setText(_translate("Form", "ara"))
        self.filtre.setText(_translate("Form", "filtrele"))
        self.label.setText(_translate("Form", "kategori:"))
        self.kitap_ekle.setText(_translate("Form", "kitap ekle"))
        self.label_2.setText(_translate("Form", "kitap sayisi:"))
        self.label_3.setText(_translate("Form", "okunan kitap:"))
        self.rastgele_kitap.setText(_translate("Form", "rastgele kitap"))
        self.arastirma_tus.setText(_translate("Form", "arastirma"))

