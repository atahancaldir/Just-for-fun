import sqlite3

class Database():
    def __init__(self):
        self.con = sqlite3.connect("market.db")
        self.cursor = self.con.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS n11 (name TEXT, seller TEXT, price TEXT, freeShipping BOOLEAN, imgLocation TEXT)")
        self.con.commit()