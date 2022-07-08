# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-07-08 21:28:31
# @Last Modified by:   Climax
# @Last Modified time: 2022-07-08 22:17:28


# Kelvin -> Frehenheit

value = input("Enter value -> ")

def kelvin_to_Frehenheit(value):
	frehenheit = (value*1.8) - 459.67
	return frehenheit


print(kelvin_to_Frehenheit(value))
