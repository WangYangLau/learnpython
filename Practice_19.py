# -*- coding:utf-8 -*-
#功能：设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import functools,time

print(u'功能：设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：')
def log():
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('begin call')
			start = time.time()
			f = func(*args,**kw)
			end = time.time()
			t = end - start	
			print('%s executed in %s ms'%(func.__name__,t))
			print('end call')
			return f
		return wrapper
	return decorator
	
@log()
def fast(x, y):
	time.sleep(0.0012)
	return x + y

@log()
def slow(x, y, z):
	time.sleep(0.1234)
	return x * y * z
print('>>>------------------------------------------------------------------------<<<')	
f = fast(11, 22)
print('>>>------------------------------------------------------------------------<<<')	
s = slow(11, 22, 33)
print('>>>------------------------------------------------------------------------<<<')	
if f != 33:
    print(u'测试失败!')
elif s != 7986:
    print(u'测试失败!')
else:
	print(u'测试成功!')
