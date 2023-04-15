from gui import *
import sys

class Apollo():
    def __init__(self):
        self.username = "a.caldir"
        self.password = "12345"

        with open("musicList.txt","r",encoding="utf-8") as file:
            self.songListContent = file.readlines()
            self.songListContent = list(map(lambda x: x[:-1], self.songListContent))

            self.songListNames = []
            self.songListTypes = []

            for i in self.songListContent:
                self.songListNames.append(i.split("-")[0].strip() + " - " + i.split("-")[1].strip())
                self.songListTypes.append(i.split("-")[-1].strip())


    def login(self):
        if window.username.text() == self.username and window.password.text() == self.password:
            window.loginFrame.hide()
            window.homeFrame.show()

    def history(self):
        window.homeFrame.hide()
        window.historyFrame.show()

        def history_close():
            window.historyFrame.hide()
            window.homeFrame.show()
        
        window.historyBackBut.clicked.connect(history_close)

    def friends(self):
        window.homeFrame.hide()
        window.friendsFrame.show()

        def friends_close():
            window.friendsFrame.hide()
            window.homeFrame.show()
        
        window.friendsBackBut.clicked.connect(friends_close)

    def world(self):
        window.homeFrame.hide()
        window.worldFrame.show()

        def world_close():
            window.worldFrame.hide()
            window.homeFrame.show()
        
        window.worldBackBut.clicked.connect(world_close)

    def details(self):
        window.homeFrame.hide()
        window.detailsFrame.show()

        def details_close():
            window.detailsFrame.hide()
            window.homeFrame.show()
        
        window.detailsBackBut.clicked.connect(details_close)

    def share(self):
        window.homeFrame.hide()
        window.shareFrame.show()

        for i in self.songListNames:
            new_item = QtWidgets.QListWidgetItem(i)
            window.shareSongList.addItem(new_item)

        def share_close():
            window.shareFrame.hide()
            window.homeFrame.show()
        
        def successful():
            window.successFrame.show()
            window.shareMap.setPixmap(QtGui.QPixmap("img/gps4.png"))
            window.mapLabel.setPixmap(QtGui.QPixmap("img/gps4.png"))

        window.shareShareBut.clicked.connect(successful)
        window.successBackBut.clicked.connect(lambda: window.successFrame.hide())
        window.shareBackBut.clicked.connect(share_close)

    def route(self):
        window.homeFrame.hide()
        window.routeFrame.show()

        for i in self.songListNames:
            new_item = QtWidgets.QListWidgetItem(i)
            window.routeSongList.addItem(new_item)

        def place_songs():
            category = window.comboBox.currentText()
            window.routeSongList.clear()

            count = 0

            for i in self.songListTypes:
                if i == category:
                    new_item = QtWidgets.QListWidgetItem(self.songListNames[count])
                    window.routeSongList.addItem(new_item)

                count += 1

        def route_close():
            window.routeFrame.hide()
            window.homeFrame.show()
        
        window.routeBackBut.clicked.connect(route_close)
        window.comboBox.currentIndexChanged.connect(place_songs)

apollo = Apollo()

app = QtWidgets.QApplication(sys.argv)
window = Ui_MAIN()
window.homeFrame.hide()
window.historyFrame.hide()
window.friendsFrame.hide()
window.worldFrame.hide()
window.routeFrame.hide()
window.shareFrame.hide()
window.successFrame.hide()
window.detailsFrame.hide()
window.show()

window.loginBut.clicked.connect(apollo.login)
window.likeBut.clicked.connect(apollo.history)
window.friendsBut.clicked.connect(apollo.friends)
window.worldBut.clicked.connect(apollo.world)
window.routeBut.clicked.connect(apollo.route)
window.musicBut.clicked.connect(apollo.share)
window.songNameList.itemClicked.connect(apollo.details)

sys.exit(app.exec_())