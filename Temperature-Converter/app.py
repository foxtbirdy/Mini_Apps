# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-07-09 22:31:13
# @Last Modified by:   Climax
# @Last Modified time: 2022-07-18 19:31:29


import sys 
import webbrowser

from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel, QLineEdit, QTextEdit, QDialog, QPushButton, QDialogButtonBox, QVBoxLayout)
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QFont, QRegExpValidator

from convert import SI_Calculator

# QRegExp is for the Regex Support. 
# QRegExpValidator is for the validator of the PyQt5 to be Regex Supported


calculuate = SI_Calculator()

app = QApplication(sys.argv)
regex = r'([\d]+)|(-[0-9]+)'
exception = QtCore.QRegExp(regex) # Regex syntax
validator = QtGui.QRegExpValidator(exception)



class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()	
		self.setWindowTitle("Temperature Converter")
		self.setFixedSize(600,800)
		self.setStyleSheet(open("design.css", "r").read())

		self.label_above()
		self.input_field()
		self.slot_connect()
		self.display_results()
		self.credits()

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
			size.setValidator(validator)


	def slot_connect(self):

		self.input_Celcius.textChanged.connect(self.celcius_evaluation)
		self.input_Fahrenheit.textChanged.connect(self.fahrenheit_evaluation)
		self.input_Kelvin.textChanged.connect(self.kelvin_evaluation)



	def celcius_evaluation(self, s):
		# disable if there is a value in a lineedit

		self.disable_TextFields(value=s, func1=self.input_Fahrenheit, func2=self.input_Kelvin)

		if s == "":
			self.ans_text_box.setText("")
			pass
		elif s == "-":
			self.ans_text_box.setText("")		
		else:
			self.ans_text_box.setText(f"Fahrenheit: {calculuate.celcius_to_fahrenheit(s)}\nKelvin: {calculuate.celcius_to_kelvin(s)}")


	def fahrenheit_evaluation(self, s):
		# disable if there is a value in a lineedit
		self.disable_TextFields(value=s, func1=self.input_Celcius, func2=self.input_Kelvin)

		if len(s) > 0:
			self.input_Celcius.setDisabled(True)
			self.input_Kelvin.setDisabled(True)
		else:
			self.input_Celcius.setDisabled(False)
			self.input_Kelvin.setDisabled(False)

		if s == "":
			self.ans_text_box.setText("")
			pass
		elif s == "-":
			self.ans_text_box.setText("")		
		else:
			self.ans_text_box.setText(f"Celcius: {calculuate.fahrenheit_to_celcius(s)}\nKelvin: {calculuate.fahrenheit_to_kelvin(s)}")


	def kelvin_evaluation(self, s):

		self.disable_TextFields(value=s, func1=self.input_Celcius, func2=self.input_Fahrenheit)

		if s == "":
			self.ans_text_box.setText("")
			pass
		elif s == "-":
			self.ans_text_box.setText("")		
		else:
			self.ans_text_box.setText(f"Celcius: {calculuate.kelvin_to_Celcius(s)}\nfFahrenheit: {calculuate.kelvin_to_Fahrenheit(s)}")


	def disable_TextFields(self, value, func1, func2):
		if len(value) > 0:
			func1.setDisabled(True)
			func2.setDisabled(True)
		else:
			func1.setDisabled(False)
			func2.setDisabled(False)


	def display_results(self):
		self.ans_text_box = QTextEdit(self)
		self.ans_text_box.setFixedSize(500,130) # width , height
		self.ans_text_box.move(20,630) # x , y
		
		self.ans_text_box.setPlaceholderText("The answers will be presented here.")


	def credits(self):
		self.author = QPushButton("Created by @Black_2_white for research and Open Sourced Development", self)
		self.author.move(110,770)
		self.author.resize(400,30)
		self.author.clicked.connect(self.author_response)




	def author_response(self):
		dlg = CustomDialog_forAuthor()
		if dlg.exec_():
			webbrowser.open("www.twitter.com/@Black_2_white")

	


class CustomDialog_forAuthor(QDialog):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Hello there!")
		self.setFixedSize(600,500)
		self.setStyleSheet("QDialog {background: black;}")

		QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

		self.buttonBox = QDialogButtonBox(QBtn)
		self.buttonBox.setStyleSheet("color: black")
		self.buttonBox.accepted.connect(self.accept)
		self.buttonBox.rejected.connect(self.reject)

		self.layout = QVBoxLayout()
		message = QLabel("Thank you for using this app.\n This is the second major solo app project I made in the library of the PyQt5. I hope that you can use this for your own research. If you wish, you can visit my Twitter Page!\nWill you go?")
		self.layout.addWidget(message)
		self.layout.addWidget(self.buttonBox)
		self.setLayout(self.layout)
		message.setWordWrap(True)
		message.setStyleSheet("color: white")
		message.setFont(QFont("Montserrat", 15))
		message.setAlignment(Qt.AlignCenter)




window = MainWindow()
window.show()
app.exec_()



