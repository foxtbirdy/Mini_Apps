# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-07-09 22:31:13
# @Last Modified by:   Climax
# @Last Modified time: 2022-07-10 00:02:38


import sys 

from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel, QVBoxLayout)
from PyQt5.QtCore import Qt
app = QApplication(sys.argv)


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()	
		self.setWindowTitle("Testing")
		self.layout = QVBoxLayout()
		self.setLayout(self.layout)
		self.setFixedSize(600,800)
		self.label_above()


	def label_above(self):
		label_Intro = QLabel("Enter your Temperature value below~", self)
		font = label_Intro.font()
		font.setPointSize(17)
		label_Intro.setFont(font)
		label_Intro.resize(400,20)
		label_Intro.move(20,10)

		label_description = QLabel("Please insert your value in one of the boxes given below. The application will display the converted value of the other corresponding values.", self)
		label_descript_font = label_description.font()
		label_descript_font.setPointSize(17)
		label_description.setFont(label_descript_font)
		label_description.resize(600,20)
		label_description.move(20,45)
		label_description.setWordWrap(True)


window = MainWindow()
window.show()
app.exec_()