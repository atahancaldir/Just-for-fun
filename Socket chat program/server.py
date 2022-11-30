from tkinter import *
import tkinter.messagebox as tm
import socket
import sys
import pygame
from threading import Thread
import time

pygame.init()
mesaj_sesi = pygame.mixer.Sound("mesaj_sesi.wav")
mesaj_sesi.set_volume(.9)

def quit():
	sys.exit()

pencere=Tk()
pencere.title("Giriş")
pencere.geometry("400x90+300+200")
pencere.protocol("WM_DELETE_WINDOW",quit)
pencere.resizable(1,1)

Label(text=" ").grid(row=0)

Label(text="Kullanıcı adı").grid(row=0,column=1,columnspan=3)

nick=Entry(pencere,width=30)
nick.grid(row=1,column=1)

Label(text="  ").grid(row=1,column=2)

HOST = Entry(pencere,width=30)
HOST.grid(row=1,column=3,pady=3)

def sorgu():
	global HOST

	kullanıcı_adı=nick.get()
	HOST = "31.170.164.53"
	if not kullanıcı_adı or kullanıcı_adı.isspace() or not HOST or HOST.isspace():
		tm.showerror("Giriş hatası","Değerleri doğru giriniz!!!")
	elif len(kullanıcı_adı)>10:
		tm.showerror("Çok uzun","Daha kısa bir isim seçiniz.")
	else:
		pencere.destroy()
		sohbet=Tk()
		sohbet.title("Gizli sohbet")
		sohbet.geometry("400x320+300+200")
		liste=Listbox(sohbet,bg="grey")
		liste.pack(fill="both",expand="yes")

		liste.insert(END,"Server başlatıldı.")
		liste.insert(END,"Karşı taraf bekleniyor.")

		mesaj=Text(sohbet,height=7)
		mesaj.pack(fill="both",expand="yes")

		def chat():
			global soket
			global baglanti

			soket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			PORT = 1234
			try:
				soket.bind((HOST,PORT))
			except:
				quit()
			soket.listen(1)
			baglanti ,adres = soket.accept()
			liste.insert(END,"Konuşma başladı.")
			while True:
				gelen = baglanti.recv(1024)
				if gelen.decode() == "-*-cikis_yapildi-*-":
					tm.showinfo("Sohbet bitti","Karşı taraf konuşmadan çıktı.")
				else:
					pygame.mixer.Sound.play(mesaj_sesi)
					liste.insert(END, gelen)
					liste.see('end')
					time.sleep(0.2)

		def cikis():
			try:
				baglanti.send("-*-cikis_yapildi-*-".encode())
				soket.close()
				baglanti.close()
				pygame.quit()
				quit()
			except:
				quit()

		sohbet.protocol("WM_DELETE_WINDOW",cikis)

		t = Thread(target = chat)
		t.start()

		def gonder():

			kaynak = 'çğıöşüÇĞİÖŞÜ'
			hedef =  'cgiosuCGIOSU'
			turkce_karakter = str.maketrans(kaynak,hedef)

			ileti=mesaj.get("1.0",END)
			if ileti=="" or ileti.isspace():
				tm.showerror("Geçersiz","Geçerli bir ileti giriniz.")
			else:
				ileti=kullanıcı_adı+": "+ileti
				ileti = ileti.translate(turkce_karakter)
				liste.insert(END,ileti)
				try:
					baglanti.send(ileti.encode())
				except ConnectionResetError:
					quit()
				mesaj.delete("1.0",END)
				liste.see("end")

		Button(sohbet,text="Gönder!",height=10,command=gonder).pack(fill="both",side="bottom",expand="yes")

		sohbet.mainloop()

Button(pencere,text="Giriş yap!",width=50,command=sorgu).grid(row=2,column=1,columnspan=3)
pencere.mainloop()
