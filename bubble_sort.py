# -*- coding: utf-8 -*-
"""
created on Mon Aug 28
@author:quanqi.yue
filename:bubble_sort.py
"""

def Bubble_sort(number):
	for i in range(len(number)):
		for j in range(len(number) - 1):
			if number[j] > number[j+1]:
				number[j], number[j+1] = number[j+1], number[j]

	return number
