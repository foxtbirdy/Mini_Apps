# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-07-09 22:31:13
# @Last Modified by:   Climax
# @Last Modified time: 2022-07-10 20:42:30


import sys 

from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel, QLineEdit)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
app = QApplication(sys.argv)


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()	
		self.setWindowTitle("Testing")
		self.setFixedSize(600,800)
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
		# Labels for the SI Units
		# dict - units, dimensions
		temperatures = {"Celcius" : 200, 
						"Fahrenheit" : 350, 
						"Kelvin" : 500}

		for unit,dimensions in temperatures.items():
			labels = QLabel("*"+unit+":", self)
			labels.setFont(QFont("Arial", 20))
			labels.move(20,dimensions)
			labels.resize(160,30)
			labels.setStyleSheet("border: 2px solid black")


		input_Celcius = QLineEdit("", self)
		input_Celcius.move(20,265)

		input_Fahrenheit = QLineEdit("", self)
		input_Fahrenheit.move(20,415)

		input_kelvin = QLineEdit("", self)
		input_kelvin.move(20,570)

		for size in input_kelvin, input_Fahrenheit, input_Celcius:
			size.resize(200,50)



window = MainWindow()
window.show()
app.exec_()