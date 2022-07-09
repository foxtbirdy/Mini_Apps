# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-07-08 21:28:31
# @Last Modified by:   Climax
# @Last Modified time: 2022-07-09 22:48:34


def kelvin_to_Fahrenheit(value):
	fahrenheit = (value*1.8) - 459.67
	return fahrenheit


kelvin_to_Fahrenheit(value=68)


def kelvin_to_Celcius(value):
	celcius = value - 273.15
	return celcius

kelvin_to_Celcius(value=68)


def celcius_to_fahrenheit(value):
	fahrenheit = (value*1.8)+32
	return fahrenheit

celcius_to_fahrenheit(value=68)


def celcius_to_kelvin(value):
	kelvin = value + 273.15
	return kelvin

celcius_to_kelvin(value=68)


def fahrenheit_to_celcius(value):
	celcius = (value - 32) * 0.56
	return celcius

fahrenheit_to_celcius(value=68)

def fahrenheit_to_kelvin(value):
	kelvin = (0.56 * (value-32)) + 273.15
	return kelvin

fahrenheit_to_kelvin(value=68)
