# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-07-09 22:31:13
# @Last Modified by:   Climax
# @Last Modified time: 2022-07-15 22:06:49


import sys 
import re

from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel, QLineEdit)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from convert import SI_Calculator


calculuate = SI_Calculator()
app = QApplication(sys.argv)
exception = re.compile('[0-9.]+$')


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()	
		self.setWindowTitle("Testing Balls")
		self.setFixedSize(600,800)
		self.label_above()
		self.input_field()
		self.slot_connect()


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

		# input fields
		self.input_Celcius = QLineEdit("", self)
		self.input_Celcius.move(20,265)

		self.input_Fahrenheit = QLineEdit("", self)
		self.input_Fahrenheit.move(20,415)

		self.input_Kelvin = QLineEdit("", self)
		self.input_Kelvin.move(20,570)

		for size in self.input_Kelvin, self.input_Fahrenheit, self.input_Celcius:
			size.resize(300,50)

			font = size.font()
			font.setPointSize(16)
			size.setFont(font)

			size.setStyleSheet("QLineEdit {background:transparent; border-style: outset; border-width: 2px; border-color: green}")

	# def error_msg_label(self):


	def slot_connect(self):

		self.input_Celcius.textChanged.connect(self.celcius_evaluation)
		self.input_Fahrenheit.textChanged.connect(self.fahrenheit_evaluation)
		self.input_Kelvin.textChanged.connect(self.kelvin_evaluation)



	def celcius_evaluation(self, s):
		print(f"length {len(s)}")

		self.input_Fahrenheit.setDisabled(True)
		self.input_Kelvin.setDisabled(True)

		if not exception.match(s):
		 	self.input_Celcius.setText(s)
		else:
			print(f"Fahrenheit: {calculuate.celcius_to_fahrenheit(s)}")
			print(f"Kelvin: {calculuate.celcius_to_kelvin(s)}")


	def fahrenheit_evaluation(self, s):
		if not exception.match(s):
		 	self.input_Celcius.setText(s)		 	
		else:
			print(f"Celcius: {calculuate.fahrenheit_to_celcius(s)}")
			print(f"Kelvin: {calculuate.fahrenheit_to_kelvin(s)}")


	def kelvin_evaluation(self, s):
		if not exception.match(s):
		 	self.input_Kelvin.setText(s)
		else:
			print(f"Celcius: {calculuate.kelvin_to_Celcius(s)}")
			print(f"Fahrenheit: {calculuate.kelvin_to_Fahrenheit(s)}")





window = MainWindow()
window.show()
app.exec_()



