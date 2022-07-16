# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-07-09 22:31:13
# @Last Modified by:   Climax
# @Last Modified time: 2022-07-17 01:57:28


import sys 

from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel, QLineEdit)
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QFont, QRegExpValidator

from convert import SI_Calculator

# QRegExp is for the Regex Support. 
# QRegExpValidator is for the validator of the PyQt5 to be Regex Supported


calculuate = SI_Calculator()
app = QApplication(sys.argv)
exception = QtCore.QRegExp('[0-9.-]+$') # Regex syntax


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()	
		self.setWindowTitle("Testing Balls")
		self.setFixedSize(600,800)
		self.label_above()
		self.input_field()
		self.error_msg_label()
		self.slot_connect()


	def label_above(self):
		# first label
		label_Intro = QLabel("Enter your Temperature value below~", self)
		label_Intro.setFont(QFont("Arial", 15))
		label_Intro.resize(500,30)
		label_Intro.move(20,20)

		# second label
		label_description = QLabel("Please insert your value in one of the boxes given below. The application will display the converted value of the other corresponding values.", self)
		label_description.setFont(QFont("Arial", 15))
		label_description.resize(500,90)
		label_description.move(20,50)
		label_description.setWordWrap(True)

	def input_field(self):
		# Labels for the SI Units
		# dict - units, dimensions
		temperatures = {"Celcius" : 180, 
						"Fahrenheit" : 330, 
						"Kelvin" : 480}

		for unit,dimen in temperatures.items(): # dimen as of dimension
			labels = QLabel("*"+unit+":", self)
			labels.setFont(QFont("Arial", 20))
			labels.move(20,dimen)
			labels.resize(160,30)

		# input fields
		self.input_Celcius = QLineEdit("", self)
		self.input_Celcius.move(20,245)
		self.input_Celcius.setPlaceholderText("Enter your Celcius here")

		self.input_Fahrenheit = QLineEdit("", self)
		self.input_Fahrenheit.move(20,390)
		self.input_Fahrenheit.setPlaceholderText("Enter your Fahrenheit here")

		self.input_Kelvin = QLineEdit("", self)
		self.input_Kelvin.move(20,540)
		self.input_Kelvin.setPlaceholderText("Enter your Kelvin here")

		for size in self.input_Kelvin, self.input_Fahrenheit, self.input_Celcius:
			# set size for QLineEdit
			size.resize(500,50)

			font = size.font()
			font.setPointSize(16)
			size.setFont(font)

			# set designs for the QLineEdit
			size.setStyleSheet("QLineEdit {background:transparent; border-style: outset; border-width: 2px; border-color: green}")

			# restrict inputs to int + set limit
			size.setValidator(QRegExpValidator(exception))

	def error_msg_label(self):
		# temperatures = {"Celcius" : [180, 50], # dimen as of dimension
		# 				"Fahrenheit" : [330,50], 
		# 				"Kelvin" : [480,50]
		# 				}


		# for unit,dimen in temperatures.items():
		# 	labels = QLabel("Error.", self)
		# 	labels.setFont(QFont("Arial", 20))
		# 	labels.move(20,dimensions)
		# 	labels.resize(160,30)


		self.celcius_error = QLabel("Error found", self)
		# self.celcius_error.move(150, 182)
		# self.celcius_error.resize(160,30)

		self.fahrenheit_error = QLabel("Error found", self)
		# self.fahrenheit_error.move(170, 332)
		# self.fahrenheit_error.resize(160,30)

		self.kelvin_error = QLabel("Error found", self)
		# self.kelvin_error.move(150, 482)
		# self.kelvin_error.resize(160,30)

		units = {
			self.celcius_error: [250,182],
			self.fahrenheit_error: [250,332],
			self.kelvin_error: [250,482]	
		}

		for var, pos in units.items():
			var.move(pos[0], pos[1])
			var.resize(270,30)	
			var.setFont(QFont("Arial", 16))
			var.setStyleSheet("color: red; border: 2px solid black")
			var.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)


	def slot_connect(self):

		self.input_Celcius.textChanged.connect(self.celcius_evaluation)
		self.input_Fahrenheit.textChanged.connect(self.fahrenheit_evaluation)
		self.input_Kelvin.textChanged.connect(self.kelvin_evaluation)



	def celcius_evaluation(self, s):
		# disable if there is a value in a lineedit
		if len(s) > 0:
			self.input_Fahrenheit.setDisabled(True)
			self.input_Kelvin.setDisabled(True)
		else:
			self.input_Fahrenheit.setDisabled(False)
			self.input_Kelvin.setDisabled(False)

		if s == "":
			pass
		else:
			print(f"Fahrenheit: {calculuate.celcius_to_fahrenheit(s)}")
			print(f"Kelvin: {calculuate.celcius_to_kelvin(s)}")


	def fahrenheit_evaluation(self, s):
		# disable if there is a value in a lineedit
		if len(s) > 0:
			self.input_Celcius.setDisabled(True)
			self.input_Kelvin.setDisabled(True)
		else:
			self.input_Celcius.setDisabled(False)
			self.input_Kelvin.setDisabled(False)

		if s == "":
			pass
		else:
			print(f"Celcius: {calculuate.fahrenheit_to_celcius(s)}")
			print(f"Kelvin: {calculuate.fahrenheit_to_kelvin(s)}")


	def kelvin_evaluation(self, s):
		# disable if there is a value in a lineedit
		if len(s) > 0:
			self.input_Fahrenheit.setDisabled(True)
			self.input_Celcius.setDisabled(True)
		else:
			self.input_Fahrenheit.setDisabled(False)
			self.input_Celcius.setDisabled(False)

		if s == "":
			pass
		else:
			print(f"Celcius: {calculuate.kelvin_to_Celcius(s)}")
			print(f"Fahrenheit: {calculuate.kelvin_to_Fahrenheit(s)}")


window = MainWindow()
window.show()
app.exec_()
