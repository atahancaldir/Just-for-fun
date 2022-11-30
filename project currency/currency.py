from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from gui import *
import sys
from threading import Thread
import time

app = QtWidgets.QApplication(sys.argv)
window = Ui_Form()

window.show()

def getValue(url):
    data = urlopen(Request(url, headers={'User-Agent': 'Mozilla'})).read()
    parse = BeautifulSoup(data,"html.parser")
    return parse.find_all('span', id="last_last")[0].text

def getChange(url):
    data = urlopen(Request(url, headers={'User-Agent': 'Mozilla'})).read()
    parse = BeautifulSoup(data,"html.parser")
    return parse.find_all('span', dir="ltr")[-1].text

class Dollar(QtCore.QThread):
	def __init__(self,parent=None):
		super(Dollar,self).__init__(parent)

	def run(self):
		url = "http://tr.investing.com/currencies/usd-try"
		while True:
			dollar_value = getValue(url)

			if dollar_value>window.dollar_buying.text():
				window.dollar_buying.setStyleSheet("background:#50e55a;color:white;")

			elif dollar_value<window.dollar_buying.text():
				window.dollar_buying.setStyleSheet("background:#d62023;color:white;")
				

			window.dollar_buying.setText(dollar_value)
			time.sleep(0.5)
			window.dollar_buying.setStyleSheet("background:None;color:white;")

			if getChange(url)[0]=="+":
				window.dollar_change.setStyleSheet("color:green;")
			else:
				window.dollar_change.setStyleSheet("color:red;")

			window.dollar_change.setText(getChange(url))

			time.sleep(3)

class Euro(QtCore.QThread):
	def __init__(self,parent=None):
		super(Euro,self).__init__(parent)

	def run(self):
		url = "https://tr.investing.com/currencies/eur-try"
		while True:
			euro_value = getValue(url)

			if euro_value>window.euro_buying.text():
				window.euro_buying.setStyleSheet("background:#50e55a;color:white;")

			elif euro_value<window.euro_buying.text():
				window.euro_buying.setStyleSheet("background:#d62023;color:white;")
				

			window.euro_buying.setText(euro_value)
			time.sleep(0.5)
			window.euro_buying.setStyleSheet("background:None;color:white;")

			if getChange(url)[0]=="+":
				window.euro_change.setStyleSheet("color:green;")
			else:
				window.euro_change.setStyleSheet("color:red;")
			
			window.euro_change.setText(getChange(url))

			time.sleep(3)

class Gold(QtCore.QThread):
	def __init__(self,parent=None):
		super(Gold,self).__init__(parent)

	def run(self):
		url = "https://tr.investing.com/currencies/gau-try"
		while True:
			gold_value = getValue(url)

			if gold_value>window.gold_buying.text():
				window.gold_buying.setStyleSheet("background:#50e55a;color:white;")

			elif gold_value<window.gold_buying.text():
				window.gold_buying.setStyleSheet("background:#d62023;color:white;")
				

			window.gold_buying.setText(gold_value)
			time.sleep(0.5)
			window.gold_buying.setStyleSheet("background:None;color:white;")
			
			if getChange(url)[0]=="+":
				window.gold_change.setStyleSheet("color:green;")
			else:
				window.gold_change.setStyleSheet("color:red;")

			window.gold_change.setText(getChange(url))

			time.sleep(3)

def exit():
    sys.exit()

dollar = Dollar()
dollar.start()

euro = Euro()
euro.start()

gold = Gold()
gold.start()

window.exit_but.clicked.connect(exit)

sys.exit(app.exec_())
