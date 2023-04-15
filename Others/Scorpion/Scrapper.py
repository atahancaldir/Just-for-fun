import requests
from bs4 import BeautifulSoup
import os
from DatabaseManager import Database

class Product():
    def __init__(self, product):
        self.name = product.find("a",{"class":"plink"}).get("title")
        self.seller = product.find("span",{"class":"sallerName"}).text.strip().replace(" ","").replace("\n","")
        self.price = product.find("ins").text.strip().replace(" ","").replace("\n","")
        self.freeShipping = bool(len(product.find_all("span",{"class":"textImg freeShipping"})))
        self.imgName = product.find("img",{"class":"lazy"}).get("data-original")

    def download_img(self, homeDir):
        os.chdir(homeDir + "\\img")

        fileName = self.name + self.seller + self.price
        self.lastFileName = ""

        for i in fileName:
            if not i.isalnum():
                self.lastFileName += "_"
            else:
                self.lastFileName += i

        self.lastFileName = self.lastFileName + "." + self.imgName.split(".")[-1]

        if self.lastFileName not in os.listdir():
            with open(self.lastFileName, "wb") as f:
                f.write(requests.get(self.imgName).content)

    def insertToDatabase(self, database):
        database.cursor.execute("INSERT INTO n11 VALUES(?,?,?,?,?)",(self.name,self.seller,self.price,self.freeShipping,self.lastFileName))
        database.con.commit()

    def __str__(self):
        return "name: {}\nprice: {}\nfree shipping: {}\nseller: {}\nimgName: {}".format(self.name,self.price,self.freeShipping,self.seller,self.imgName)

try:
    homeDir = os.getcwd()
    database = Database()

    key = input("keyword: ")
    count = int(input("Take x objects: "))

    url = "https://www.n11.com/arama?q=" + key.replace(" ","+")
    response = requests.get(url)

    html_content = response.content
    soup =  BeautifulSoup(html_content, "html.parser")

    products = soup.find("ul",{"class":"clearfix"})

    for product in products.find_all("li",{"class":"column"}, limit = count):
        p = Product(product)
        print(p)
        p.download_img(homeDir)
        p.insertToDatabase(database)

        print("*******************")

finally:
    database.con.close()