# -*- coding: utf-8 -*-

def product(*number):
	s = 1
	if number is ():
		return ("No number enter!")
	else:
		for n in number:
			s = s*n
		return s
	
sum = product(1,2,3)
print("sum = %s"%sum)