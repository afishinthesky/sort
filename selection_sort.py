# -*- coding:utf-8 -*-
"""
created on Mon Aug 28
@author: quanqi.yue
filename: selection_sort.py
"""

def Selection_sort(number):
	for i in range(len(number)):
		min = i
		for j in range(i + 1, len(number)):
			if number[min] > number[j]:
				min = j
		number[min], number[i] = number[i], number[min]
	return number
