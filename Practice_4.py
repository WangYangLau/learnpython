# -*- coding: utf-8 -*-

print('enter your height:')
height = float(input())
print('enter your weight:')
weight = float(input())

bmi = (weight / (height*height))
print('Your bmi is:')
print('%.2f'%bmi)

elif bmi < 18.5:
	print('too light')
elif bmi>=18.5 and bmi<25:
	print('normal')
elif bmi>=25 and bmi<28:
	print('heavy')
elif bmi>=28 and bmi<32:
	print('fat')
else:
	print('too fat')