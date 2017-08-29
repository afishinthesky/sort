# -*- coding:utf-8 -*-
"""
@author: quanqi.yue
created in Aug 29 2017
filename:insertion_sort.py
"""

def Insert_sort(number):
	num = []
	for i in range(len(number)):
		if i == 0:
			num.insert(0,number[i])
		
		else:
			for j in range(len(num)-1,-1,-1):
				if num[j]<= number[i]:
					num.insert(j+1, number[i])
					break
				elif j == 0:
					num.insert(j,number[i])
				else:
					continue
	return num
