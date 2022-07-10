# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-07-09 22:31:13
# @Last Modified by:   Climax
# @Last Modified time: 2022-07-10 19:11:22


import sys 

from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel, QLineEdit)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
app = QApplication(sys.argv)


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()	
		self.setWindowTitle("Testing")
		self.setFixedSize(600,700)
		self.label_above()
		self.input_field()


	def label_above(self):
		# first label
		label_Intro = QLabel("Enter your Temperature value below~", self)
		label_Intro.setFont(QFont("Arial", 15))
		label_Intro.resize(450,30)
		label_Intro.move(20,20)

		# second label
		label_description = QLabel("Please insert your value in one of the boxes given below. The application will display the converted value of the other corresponding values.", self)
		label_description.setFont(QFont("Arial", 15))
		label_description.resize(550,90)
		label_description.move(20,50)
		label_description.setWordWrap(True)

	def input_field(self):
		# label_Celcius
		label_Celcius = QLabel("*Celcius", self)
		label_Celcius.setFont(QFont("Arial", 17))
		label_Celcius.move(20,200)
		label_Celcius.resize(150,30)
		label_Celcius.setStyleSheet("border: 2px solid black")

		label_fahrenheit = QLabel("*Fahrenheit", self)
		label_fahrenheit.setFont(QFont("Arial", 17))
		label_fahrenheit.move(20,350)
		label_fahrenheit.resize(150,30)
		label_fahrenheit.setStyleSheet("border: 2px solid black")

		label_Kelvin = QLabel("*Kelvin", self)
		label_Kelvin.setFont(QFont("Arial", 17))
		label_Kelvin.move(20,500)
		label_Kelvin.resize(150,30)
		label_Kelvin.setStyleSheet("border: 2px solid black")







window = MainWindow()
window.show()
app.exec_()