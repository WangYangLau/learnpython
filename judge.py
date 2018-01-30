# -*- coding: utf-8 -*-

input_str = input()
if input_str != '':
	age = int(input_str)
	if age<18:
		print('Under age')
	elif age>=18 and age<=30:
		print('Youth')
	elif age>30:
		print('old age')
else:
	print('enter nothing, Bye!')