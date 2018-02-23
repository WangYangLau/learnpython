# -*- coding: utf-8 -*-
def sum(*args):
	ax = 0
	for n in args:
		ax = ax + n
	return ax

def lazy_sum():
	return sum

print('返回一个求和函数：')
print(u'lazy_sum():\n',lazy_sum())
print(u'lazy_sum()(1,2,3,4):\n',lazy_sum()(1,2,3,4))
print('>>>------------------------------------------------------------------------<<<')	
print(u'返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。')	
def count():
	fs = []
	for i in range(1,4):
		def fn():
			return i*i
		fs.append(fn)
	return fs

f1,f2,f3 = count()

print('f1:',f1())
print('f2:',f2())
print('f3:',f3())
print('>>>------------------------------------------------------------------------<<<')	
print(u'如果一定要引用循环变量，就再创建一个函数。')
def count():
	def fn(j):
		def f():
			return j*j
		return f
	fs = []
	for i in range(1,4):
		fs.append(fn(i))
	return fs

f1,f2,f3 = count()

print('f1:',f1())
print('f2:',f2())
print('f3:',f3())