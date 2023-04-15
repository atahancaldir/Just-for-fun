# -*- coding: utf-8 -*-

####################################
#         |ATAHAN CALDIR |         #
#      -Video Indirici v0.1-       #
####################################

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import youtube_dl
import ffmpy

userhome = os.path.expanduser('~')
desktop = os.path.join(userhome, 'Desktop')
os.chdir(desktop)

class Ui_Pencere(QtWidgets.QWidget):
	def __init__(self):
		QtWidgets.QWidget.__init__(self)
		self.setupUi(self)
	def setupUi(self, Pencere):
		Pencere.setObjectName("Pencere")
		Pencere.setWindowModality(QtCore.Qt.NonModal)
		Pencere.setEnabled(True)
		Pencere.resize(526, 532)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(Pencere.sizePolicy().hasHeightForWidth())
		Pencere.setSizePolicy(sizePolicy)
		Pencere.setMinimumSize(QtCore.QSize(526, 532))
		Pencere.setMaximumSize(QtCore.QSize(526, 532))
		font = QtGui.QFont()
		font.setFamily("MV Boli")
		font.setPointSize(12)
		Pencere.setFont(font)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("Belgeler/Logom.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		Pencere.setWindowIcon(icon)
		self.Liste = QtWidgets.QListWidget(Pencere)
		self.Liste.setGeometry(QtCore.QRect(5, 11, 511, 240))
		self.Liste.setObjectName("Liste")
		self.mp3 = QtWidgets.QRadioButton(Pencere)
		self.mp3.setGeometry(QtCore.QRect(30, 310, 101, 41))
		font = QtGui.QFont()
		font.setPointSize(16)
		font.setBold(True)
		font.setWeight(75)
		self.mp3.setFont(font)
		self.mp3.setObjectName("mp3")
		self.mp4 = QtWidgets.QRadioButton(Pencere)
		self.mp4.setGeometry(QtCore.QRect(160, 310, 81, 41))
		font = QtGui.QFont()
		font.setPointSize(16)
		font.setBold(True)
		font.setWeight(75)
		self.mp4.setFont(font)
		self.mp4.setObjectName("mp4")
		self.Indir = QtWidgets.QPushButton(Pencere)
		self.Indir.setGeometry(QtCore.QRect(270, 310, 231, 41))
		font = QtGui.QFont()
		font.setPointSize(16)
		font.setBold(False)
		font.setItalic(True)
		font.setWeight(50)
		self.Indir.setFont(font)
		self.Indir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.Indir.setObjectName("Indir")
		self.Indir.clicked.connect(self.kontrol)
		self.LinkInput = QtWidgets.QLineEdit(Pencere)
		self.LinkInput.setGeometry(QtCore.QRect(70, 280, 431, 21))
		font = QtGui.QFont()
		font.setFamily("Yu Gothic UI Light")
		font.setPointSize(12)
		self.LinkInput.setFont(font)
		self.LinkInput.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
		self.LinkInput.setInputMask("")
		self.LinkInput.setText("")
		self.LinkInput.setObjectName("LinkInput")
		self.Link = QtWidgets.QLabel(Pencere)
		self.Link.setGeometry(QtCore.QRect(10, 280, 51, 21))
		font = QtGui.QFont()
		font.setFamily("Leelawadee UI")
		font.setPointSize(16)
		self.Link.setFont(font)
		self.Link.setObjectName("Link")
		self.Aciklama = QtWidgets.QLabel(Pencere)
		self.Aciklama.setGeometry(QtCore.QRect(20, 370, 491, 251))
		font = QtGui.QFont()
		font.setFamily("Yu Gothic UI Light")
		font.setPointSize(14)
		font.setItalic(True)
		self.Aciklama.setFont(font)
		self.Aciklama.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		self.Aciklama.setObjectName("Aciklama")
		self.deger = 1
		self.retranslateUi(Pencere)
		QtCore.QMetaObject.connectSlotsByName(Pencere)

	def retranslateUi(self, Pencere):
		_translate = QtCore.QCoreApplication.translate
		Pencere.setWindowTitle(_translate("Pencere", "Video İndirici | Atahan ÇALDIR"))
		self.mp3.setText(_translate("Pencere", "mp3"))
		self.mp4.setText(_translate("Pencere", "mp4"))
		self.Indir.setText(_translate("Pencere", "İndir!"))
		self.Link.setText(_translate("Pencere", "Link:"))
		self.Aciklama.setText(_translate("Pencere", "<html><head/><body><p>1 - Linkler tam olarak girilmelidir.</p><p>2- Videoların (veya seslerin) inme hızları internet</p><p> bağlantınıza göre değişebilir.</p><p>3 - Videolar masaüstünüze kaydedilir.</p></body></html>"))

	def hook(self, info):

		if info["status"] == "downloading":
			self.Indir.setEnabled(False)
			QtWidgets.QApplication.processEvents()
			if self.deger == 1:
				QtWidgets.QMessageBox.information(self,"İndiriliyor...","Video/ses indiriliyor.")
				self.deger += 1

		elif info["status"] == "finished":
			QtWidgets.QApplication.processEvents()
			QtWidgets.QMessageBox.information(self,"İşleniyor...","Video/ses işleniyor.")

		else:
			pass

	def kontrol(self):

		if not self.mp3.isChecked() and not self.mp4.isChecked():
			QtWidgets.QMessageBox.warning(self,"Hata","MP3 veya MP4'den birini seçmeniz lazım !!!")
		elif not self.LinkInput.text():
			QtWidgets.QMessageBox.warning(self,"Hata","Link bölümü boş bırakılamaz !!!")
		else:

			if self.mp4.isChecked():
				try:
					ydl_opts = {
						'noplaylist': True,
						'progress_hooks': [self.hook]
					}
					ydl = youtube_dl.YoutubeDL(ydl_opts)
					ydl.add_default_info_extractors()
					info = ydl.extract_info(self.LinkInput.text(), download=True)

					dosyalar = os.listdir(os.curdir)
					for dosya in dosyalar:

						if dosya.startswith((info["title"])[:5]) and dosya.endswith(".webm"):
							ff = ffmpy.FFmpeg(
								inputs={dosya: None},
								outputs={dosya[:-5]+".mp4": None}
							)
							ff.run()
							os.remove(desktop + dosya)

						if dosya.startswith((info["title"])[:5]) and dosya.endswith(".mkv"):
							ff = ffmpy.FFmpeg(
								inputs={dosya: None},
								outputs={dosya[:-4] + ".mp4": None}
							)
							ff.run()
							os.remove(desktop + dosya)

					self.Liste.insertItem(0,info["title"]+".mp4")
					QtWidgets.QMessageBox.information(self,"İndirme Başarılı","Video Başarıyla MP4 formatında indirildi :)")
					self.deger = 1
					self.Indir.setEnabled(True)
				except:
					QtWidgets.QMessageBox.warning(self,"Hata","Bir hata oluştu.\nLütfen yeniden deneyiniz.")

			elif self.mp3.isChecked():
				try:
					ydl_opts = {
						'progress_hooks': [self.hook],
						'format': 'bestaudio/best',
						'noplaylist': True,
                        'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                        }],
					}
					ydl = youtube_dl.YoutubeDL(ydl_opts)
					ydl.add_default_info_extractors()
					info = ydl.extract_info(self.LinkInput.text(), download=True)

					self.Liste.insertItem(0,info["title"]+".mp3")
					QtWidgets.QMessageBox.information(self,"İndirme Başarılı","Müzik/ses Başarıyla MP3 formatında indirildi :)")
					self.deger = 1
					self.Indir.setEnabled(True)

				except:
					QtWidgets.QMessageBox.warning(self,"Hata","Bir hata oluştu.\nLütfen yeniden deneyiniz.")

	def closeEvent(self, QCloseEvent):
		sys.exit()
		QCloseEvent.accept()

if __name__ == "__main__":
	uygulama = QtWidgets.QApplication(sys.argv)
	pencere = Ui_Pencere()
	pencere.show()
	sys.exit(uygulama.exec_())
