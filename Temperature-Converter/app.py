# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-07-09 22:31:13
# @Last Modified by:   Climax
# @Last Modified time: 2022-07-10 01:19:25


import sys 

from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel)
from PyQt5.QtCore import Qt
app = QApplication(sys.argv)


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()	
		self.setWindowTitle("Testing")
		self.setFixedSize(600,800)
		self.label_above()


	def label_above(self):
		# first label
		label_Intro = QLabel("Enter your Temperature value below~", self)
		font = label_Intro.font()
		font.setPointSize(20)
		label_Intro.setFont(font)
		label_Intro.resize(450,30)
		label_Intro.move(20,20)

		# second label
		label_description = QLabel("Please insert your value in one of the boxes given below. The application will display the converted value of the other corresponding values.", self)
		label_descript_font = label_description.font()
		label_descript_font.setPointSize(15)
		label_description.setFont(label_descript_font)
		label_description.resize(550,90)
		label_description.move(20,50)
		label_description.setWordWrap(True)



window = MainWindow()
window.show()
app.exec_()