# -*- coding:utf-8 -*-
import functools

print(u'')
def now():
	print('2018-02-23')

f = now
print(f.__name__)
f()
print('>>>------------------------------------------------------------------------<<<')
print(u'两层嵌套返回函数名和调用函数：')
def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print('Call:%s()'%func.__name__)
		return func(*args,**kw)
	return wrapper
	
@log
def now2():
	print('2018-02-23')
now2()
print('>>>------------------------------------------------------------------------<<<')
print(u'三层嵌套返回函数名、自定义文本和调用函数：')
def log2(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper2(*args,**kw):
			print('%s,%s()'%(text,func.__name__))
			return func(*args,**kw)
		return wrapper2
	return decorator
	
@log2('execute')
def now3():
	print(u'2018-02-23')
now3()
print('>>>------------------------------------------------------------------------<<<')
print(now.__name__)
print(now2.__name__)
print(now3.__name__)