import speech_recognition as sr
import os
import random
import webbrowser
from gtts import gTTS
import pygame
import ffmpy
import urllib.request
import time

pygame.mixer.init()

while 1:
    try:

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Bir şeyler söyle!")
            audio = r.listen(source)

        komut = r.recognize_google(audio, language = "tr-TR")
    except:
        print("Dediğinizi anlayamadım :(")
        continue

    print(komut)

    def konus(text):
        tts = gTTS(text = text, lang="tr")
        tts.save("ses.mp3")
        ses = "ses.mp3"
        ff = ffmpy.FFmpeg(
            inputs={ses: None},
            outputs={ses[:-4] + ".wav": None}
        )
        ff.run()
        os.remove(ses)
        ses = pygame.mixer.Sound("ses.wav")
        pygame.mixer.Sound.play(ses)
        os.remove("ses.wav")

    if "rastgele müzik aç" in komut:
        konus("Rastgele müzik açıyorum.")
        os.chdir("C:\\Users\\atahan\\Desktop\\Belgeler\\Muzikler")
        sayi = random.randrange(1,98)
        muzik = (os.listdir(os.curdir))[sayi]
        os.startfile(muzik)
    if "YouTube'u aç" in komut:
        webbrowser.open("www.youtube.com",new = 2)
    if "Google'ı aç" in komut:
        webbrowser.open("www.google.com",new = 2)
    if "Gmail aç" in komut:
        webbrowser.open("www.gmail.com",new = 2)
    if "Facebook u aç" in komut:
        webbrowser.open("www.facebook.com",new = 2)
    if "Counter Strike Global offensive aç" in komut:
        os.chdir("C:\\Users\\atahan\\Desktop\\Oyunlar")
        os.startfile("Counter-Strike Global Offensive.url")
    if "oyunlar" in komut:
        os.chdir("C:\\Program Files (x86)\\Steam")
        os.startfile("Steam.exe")
    if "müziği kapat" in komut:
        os.system("TASKKILL /F /IM wmplayer.exe")
    if "nasılsın" in komut:
        konus("Çok iyiyim Atahan. İsteğiniz nedir?")
    if "hava durumu" in komut:
        url = "http://www.havadurumu15gunluk.net/havadurumu/konya-hava-durumu-15-gunluk.html"
        a = str(urllib.request.urlopen(url).readlines()[267])
        durum = "Konya' da hava " + str(a[69:71]) +" derece Atahan."
        konus(durum)
    if komut== "kapan" or komut == "görüşürüz" or komut == "güle güle":
        konus("Görüşmek üzere efendim.")
        time.sleep(3)
        quit()
