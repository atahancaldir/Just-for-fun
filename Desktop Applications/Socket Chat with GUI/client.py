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

pencere=Tk()
pencere.title("Giriş")
pencere.geometry("200x80+300+200")
pencere.resizable(0,0)
def quit():
	sys.exit()
pencere.protocol("WM_DELETE_WINDOW",quit)

Label(text="Kullanıcı adı").pack()

nick=Entry(pencere,width=30)
nick.pack(pady=5)


def sorgu():
	kullanıcı_adı=nick.get()
	if not kullanıcı_adı or kullanıcı_adı.isspace():
		tm.showerror("İsim","Bu alan boş bırakılamaz!!!")
	elif len(kullanıcı_adı)>10:
		tm.showerror("Çok uzun","Daha kısa bir isim seçiniz.")
	else:
		pencere.destroy()
		sohbet=Tk()
		sohbet.title("Gizli sohbet")
		sohbet.geometry("400x320+300+200")
		liste=Listbox(sohbet,bg="grey")
		liste.pack(fill="both",expand="yes")

		liste.insert(END,"Konuşma başlatıldı.")

		mesaj=Text(sohbet,height=7)
		mesaj.pack(fill="both",expand="yes")

		def chat():
			global soket
			global baglanti
			soket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			HOST = "localhost"
			port = 1234
			soket.connect((HOST,port))
			while True:
				gelen = soket.recv(1024)
				if gelen.decode() == "-*-cikis_yapildi-*-":
					tm.showinfo("Sohbet bitti","Karşı taraf konuşmadan çıktı.")
					quit()
				else:
					pygame.mixer.Sound.play(mesaj_sesi)
					liste.insert(END, gelen)
					liste.see('end')
					time.sleep(0.2)

		def cikis():
			try:
				soket.send("-*-cikis_yapildi-*-".encode())
				soket.close()
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
					soket.send(ileti.encode())
				except ConnectionResetError:
					quit()
				mesaj.delete("1.0",END)
				liste.see("end")

		Button(sohbet,text="Gönder!",height=10,command=gonder).pack(fill="both",side="bottom",expand="yes")

		sohbet.mainloop()

Button(pencere,text="Giriş yap!",command=sorgu).pack()
pencere.mainloop()
