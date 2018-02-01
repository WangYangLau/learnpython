# -*- coding: utf-8 -*-

print("define my function named my_abs")
def my_abs(x):
	if not isinstance(x,(int,float)): #表示x应为int或者float
		raise TypeError('bad operand type') #报错提示
	if x>0:
		return x
	else:
		return -x
		
a = my_abs(100)
b = my_abs(-100)
print("enter 100,output %d"%a)
print("enter -100,output %d"%b)

import math #导入math包

print("return more value")
def move(x,y,step,angle):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx,ny

x,y=move(100,100,60,math.pi/6)
print("output a tuple :")
print(x,y)
	
