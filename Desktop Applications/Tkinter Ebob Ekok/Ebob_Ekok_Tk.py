from tkinter import *
import tkinter.messagebox as tm
import sys

def program():
        pencere=Tk()
        pencere.config(cursor="@Arrow.cur")
        pencere.title("Ebob Ekok - Ata Official")
        pencere.wm_attributes("-alpha",0.95)
        pencere.wm_iconbitmap("Logom2.ico")
        pencere.geometry("450x250+300+100")
        pencere.resizable(0,0)

        Label(pencere,text="EBOB-EKOK Bulucu",font=("Yu Gothic UI Semibold",20)).grid(row=0,columnspan=2)

        Label(pencere,text="İlk sayıyı giriniz     ",font=("Yu Gothic UI Light",15)).grid(row=1,column=0)
        Sayı1=Entry(pencere,width=30,cursor="@IBeam.cur")
        Sayı1.grid(row=1,column=1,padx=5)

        Label(pencere,text="İkinci sayıyı giriniz  ",font=("Yu Gothic UI Light",15)).grid(row=2,column=0)
        Sayı2=Entry(pencere,width=30,cursor="@IBeam.cur")
        Sayı2.grid(row=2,column=1)
        
        def Ebob():
                try:
                        sayı1=int(Sayı1.get())
                        sayı2=int(Sayı2.get())
                        for i in range(min(sayı2,sayı1),0,-1):
                                if sayı1%i==0 and sayı2%i==0:
                                        Ebob=i
                                        Ekok=int(sayı1*sayı2/i)
                                        break
                        Label(pencere,text="Ebob: "+str(Ebob),font=("Yu Gothic UI Light",15)).grid(row=5,column=0,columnspan=2)
                        Label(pencere,text="Ekok: "+str(Ekok),font=("Yu Gothic UI Light",15)).grid(row=6,column=0,columnspan=2)
                except:
                        tm.showerror("Geçersiz giriş","Yeniden deneyin.")
                        pencere.update()

        Button(pencere,text="!Bul",width=10,command=Ebob).grid(row=1,rowspan=2,column=2)
        def oturumu_kapat():
                f=open("Bilgiler.txt","w")
                f.write("")
                f.close()
                sys.exit()
        Button(pencere,text="Oturumu kapat",command=oturumu_kapat).grid(row=7,column=1)

        pencere.mainloop()



panel = Tk()
var=IntVar()
panel.config(cursor="@Arrow.cur")
panel.wm_attributes("-alpha",0.95)
panel.title("Giris Ekrani")
panel.wm_iconbitmap("Logom2.ico")
panel.wm_attributes("-toolwindow",1)
def cikis():
        sys.exit()
panel.wm_protocol("WM_DELETE_WINDOW",cikis)
panel.geometry("280x80")
panel.minsize(280,80)
panel.maxsize(280,80)

f=open("Bilgiler.txt","r")
if f.readline()=="yes":
        f.close()
        panel.destroy()
        program()

user = Label(panel,text="Kullanıcı adı: ")
password = Label(panel,text="Şifre: ")

user.grid(row= 0,column = 0)
password.grid(row= 1,column= 0)

user_entry= Entry(panel,cursor="@IBeam.cur")
password_entry= Entry(panel,show="•",cursor="@IBeam.cur")

user_entry.grid(row= 0, column= 1)
password_entry.grid(row= 1, column= 1)

beni_hatirla=Checkbutton(text="Beni Hatirla",variable=var)
beni_hatirla.grid(row=2,column=0)

def sorgu():
	kullanici=user_entry.get()
	sifre=password_entry.get()

	if kullanici=="XXX" and sifre=="YYY":
		tm.showinfo("Unlocked","Welcome Master!")
		if var.get()==1:
			f=open("Bilgiler.txt","w")
			f.write("yes")
			f.close()
		
		panel.destroy()
		program()
	else:
		tm.showerror("Locked","ALARM! ALARM!")

giris_yap=Button(text="Giris Yap",command=sorgu)
giris_yap.grid(row=2, column=1)

resim=PhotoImage(file="login.gif")
Label(image=resim).grid(rowspan=3,column=2,row=0)

panel.mainloop()