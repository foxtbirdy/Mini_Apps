import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *      
from PyQt5.QtCore import *
import pyperclip                    
import resources

__author__ = "@Black_2_white"
__encryption_by__ = "sam allen"


class APP(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("ROT13 GUI")
        self.setFixedSize(800,840)
        self.box_edit() # title Box
        self.buttons_config() #  buttons characteristics
        self.widget_toolTip() # add widget tooltips
        self.slot_connect() # add functionality
        self.setStyleSheet(open("design.css", "r").read()) # access stylesheet
        self.setWindowIcon(QIcon(":icon.png")) # set program icon
        self.set_label_logo()

		
    def buttons_config(self):
        self.button_paste = QPushButton(self)
        self.button_paste.setText("PASTE")
        self.button_paste.clicked.connect(self.paste_text)
        self.button_paste.move(150,350)

        self.button_copy = QPushButton(self)
        self.button_copy.setText("COPY")
        self.button_copy.clicked.connect(self.copy_text)
        self.button_copy.move(30,350)
        self.button_copy.setCheckable(False) 
        
        self.button_clear = QPushButton(self) 
        self.button_clear.setText("CLEAR")
        self.button_clear.clicked.connect(self.clear_text)
        self.button_clear.move(270,350)

            
    def box_edit(self):
        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(30,30, 740,300)
        self.text_edit.textChanged.connect(self.text_changed)

        self.text_edit_2 = QTextEdit(self)
        self.text_edit_2.setGeometry(30,400, 740,300)
        self.text_edit_2.setReadOnly(True)    


        
    def widget_toolTip(self):
        self.text_edit.setPlaceholderText("Write the raw text here")
        self.text_edit_2.setPlaceholderText("Encrypted results here")
        self.button_copy.setToolTip("<b>Copy Text</b>")
        self.button_paste.setToolTip("Paste <b>Copied </b> text")
        self.button_clear.setToolTip("Clear <b>Text</b>")
    
    def slot_connect(self):
        self.text_edit.textChanged.connect(self.text_changed)
        self.button_paste.clicked.connect(self.paste_text)
        self.button_copy.clicked.connect(self.copy_text)
        self.button_clear.clicked.connect(self.clear_text)

    
    def set_label_logo(self):
        self.logo = QLabel(self)
        self.logo.setStyleSheet("""
        background-image: url(:icon.png)
        """)
        self.logo.setGeometry(325,740,62,62)
        
        self.text_label = QLabel(self)
        self.text_label.setText("ROT13 \nGUI \nAPPLICATION")
        self.text_label.setGeometry(400, 735, 140, 70)

        
        
    def rot13(self):
        result = ""
        s = self.text_edit.toPlainText()
        for v in s:
            c = ord(v)
            if c >= ord('a') and c <= ord('z'):
                if c > ord('m'):
                    c -= 13
                else:
                    c += 13
            elif c >= ord('A') and c <= ord('Z'):
                if c > ord('M'):
                    c -= 13
                else:
                    c += 13
            result += chr(c)
        printout = self.text_edit_2.setText("".join(result)) # result of the text_edit
        return printout
        
        
    def copy_text(self):
        if self.text_edit.toPlainText() == '':
            pass
        elif self.text_edit.toPlainText() == '\n':
            pass
        else:
            pyperclip.copy(self.text_edit_2.toPlainText())

        
    def clear_text(self):
        self.text_edit_2.clear()
        self.text_edit.clear()
    
    
    def paste_text(self):
        self.text_edit.setText(pyperclip.paste())

        
    def text_changed(self):
        self.rot13()
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = APP()
    ex.show()
    sys.exit(app.exec_())
