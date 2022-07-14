# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-07-08 21:28:31
# @Last Modified by:   Climax
# @Last Modified time: 2022-07-14 16:48:08

class SI_Calculator():

	def celcius_to_fahrenheit(self, value):
		fahrenheit = (float(value)*1.8)+32
		return round(fahrenheit, 2)


	def celcius_to_kelvin(self, value):
		kelvin = float(value) + 273.15
		return kelvin


	def fahrenheit_to_celcius(self, value):
		celcius = (value - 32) * 0.56
		return celcius


	def fahrenheit_to_kelvin(self, value):
		kelvin = (0.56 * (value-32)) + 273.15
		return kelvin

	
	def kelvin_to_Fahrenheit(self, value):
		fahrenheit = (value*1.8) - 459.67
		return fahrenheit


	def kelvin_to_Celcius(self, value):
		celcius = value - 273.15
		return celcius
