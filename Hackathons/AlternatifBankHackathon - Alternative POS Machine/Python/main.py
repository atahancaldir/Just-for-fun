#!/usr/bin/env python
# -*- coding: utf-8 -*-

#ses oynatma

from GUI import *
import sys
import time
from gtts import gTTS
import rospy
from std_msgs.msg import Int32
from threading import Thread
from pygame import mixer

class System():
    def __init__(self):
        rospy.init_node("Hackathon")
        t = Thread(target=self.ros)
        t.start()
        Window.sure.display(0)


    def ros(self):
        rospy.Subscriber("cardID", Int32, self.cardValue)
        rospy.spin()

    def cardValue(a,b):
        if Window.paraTutari.text() == "":
            pass
        
        if Window.kartDurumu.text() != "Kart Bekleniyor" and Window.sure.value() == 0:
            pass

        else:
            if int(str(b)[-1]) == 1:
                if Window.sure.value() == 0:
                    Window.kartDurumu.setText("Ücret Okuma Aktif")
                    Window.kartDurumu.setStyleSheet("color:green;")
                    system.readValue()
                    system.countThread()
                else:
                    system.twice = True

            else:
                system.success = True
                system.payed()

    def payment(self):
        Window.kartDurumu.setStyleSheet("color:yellow;")
        Window.kartDurumu.setText("Kart Bekleniyor")
    
    def payedMessage(self):
        Window.paraTutari.setText("")
        if self.success == True:
            self.endOfTransaction = u"Ödeme Başarılı"
        else:
            self.endOfTransaction = u"Ödeme Başarısız"
        
        Window.kartDurumu.setText(self.endOfTransaction)
        Window.kartDurumu.setStyleSheet("color:blue;")

        tts = gTTS(text=self.endOfTransaction, lang="tr")
        tts.save("speech.mp3")

        mixer.init()
        mixer.music.load("/home/atahan/Desktop/Hackathon/Python/speech.mp3")
        mixer.music.play()

        time.sleep(3)
        Window.kartDurumu.setText("İşlem Bekleniyor")
        Window.kartDurumu.setStyleSheet("")


    def payed(self):
        self.t2=Thread(target=self.payedMessage)
        self.t2.start()

    def readValue(self):
        self.amount = Window.paraTutari.text()

        if len(self.amount.split(",")) == 1:
            self.read = u"Ödeme tutarı "+self.amount+u" lira. Ödeme için kartı tekrar gösteriniz."

        else:
            self.read = u"Ödeme tutarı "+self.amount.split(",")[0]+" lira "+self.amount.split(",")[1]+u" kuruş. Lütfen kartınızı tekrar gösteriniz."

        tts = gTTS(text=self.read, lang="tr")
        tts.save("speech.mp3")

        mixer.init()
        mixer.music.load("/home/atahan/Desktop/Hackathon/Python/speech.mp3")
        mixer.music.play()


    def countDown(self):
        self.counter = 10
        while self.counter>0:
            if(self.twice == False):
                Window.sure.display(self.counter)
                self.counter-=1
            else:
                break
            time.sleep(1)
        Window.sure.display(0)

        if self.counter != 0:
            self.success = True
            self.payed()
        else:
            self.success = False
            self.payed()

    def countThread(self):
        self.twice = False
        self.t3 = Thread(target=self.countDown)
        self.t3.start()


app = QtWidgets.QApplication(sys.argv)

Window = Ui_Form()
Window.show()

system = System()

Window.odemeAl.clicked.connect(system.payment)

sys.exit(app.exec_())