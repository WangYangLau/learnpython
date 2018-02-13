# -*- coding: utf-8 -*-
#高阶函数

print(u'一个简单的高阶函数：')
print('add(-5,6,abs)')
def add(x,y,f):
	return f(x)+f(y)
	
print(add((-5),6,abs))