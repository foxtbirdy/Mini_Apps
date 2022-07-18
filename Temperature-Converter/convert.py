# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-07-08 21:28:31
# @Last Modified by:   Climax
# @Last Modified time: 2022-07-18 11:34:12

set_number_decimal = 2

class SI_Calculator():

	def celcius_to_fahrenheit(self, value):
		if value == "-":
			pass
		else:
			fahrenheit = (float(value)*1.8)+32
			return round(fahrenheit, set_number_decimal)


	def celcius_to_kelvin(self, value):
		if value == "-":
			pass
		else:
			kelvin = float(value) + 273.15
			return round(kelvin , set_number_decimal)


	def fahrenheit_to_celcius(self, value):
		if value == "-":
			pass
		else:
			celcius = (float(value) - 32) * 0.56
			return round(celcius, set_number_decimal)


	def fahrenheit_to_kelvin(self, value):
		if value == "-":
			pass
		else:
			kelvin = (0.56 * (float(value)-32)) + 273.15
			return round(kelvin, set_number_decimal)

	
	def kelvin_to_Fahrenheit(self, value):
		if value == "-" or "":
			pass
		else:		
			fahrenheit = (float(value)*1.8) - 459.67
			return round(fahrenheit , set_number_decimal)


	def kelvin_to_Celcius(self, value):
		if value == "-":
			pass
		else:
			celcius = float(value) - 273.15
			return round(celcius , set_number_decimal)
