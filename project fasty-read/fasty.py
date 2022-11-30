from create_win import *
import time
from threading import Thread

keep_reading = True

def time_calc(text,word,wpm):
    global text_list
    text_list = text.split(" ")
    total_time = len(text_list)/int(wpm)
    return total_time


def create():
    text = win.textEdit.toPlainText()
    global word
    word = win.words.currentText()
    global font
    font = win.fontComboBox.currentFont()
    font.setPointSize(17)

    word = int(word)
    win.close()
    win2.time_label.setText(str(time_calc(text,word,win.bolumler.currentText()))+" dk")
    win2.show()
    global keep_reading
    keep_reading = True
    win2.start.clicked.connect(start)
        
def finish():
    win3.close()
    global keep_reading
    keep_reading = False
    win.show()

def start():
    win2.close()
    win3.show()
    win3.pushButton.clicked.connect(finish)
    win3.read_label.setFont(font)
    def reading():

        cursor = 0
        wpm = int(win.bolumler.currentText())

        while cursor+1 <= len(text_list):
            if win3.isVisible() == True:
                pass
            else:
                break
            
            if keep_reading==True:
                pass
            else:
                break

            win3.read_label.setText("")
            new_text = ""

            for i in range(word):
                new_text += text_list[cursor]
                new_text += " "
                try:
                    cursor+=1
                except:
                    return

            win3.read_label.setText(new_text)
            time.sleep((60*word)/wpm)

    t = Thread(target= reading)
    t.start()

    
app = QtWidgets.QApplication(sys.argv)
win = Ui_Form()
win2 = Ui_start_window()
win3 = Ui_reader()

win.show()

win.create_but.clicked.connect(create)
win2.start.clicked.connect(start)

sys.exit(app.exec_())
