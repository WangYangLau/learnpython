# -*- coding: utf-8 -*-

print(u'创建一个generator:')
g = (x*x for x in range(6))
print(g)
print(u'迭代一个generator:')
for a in g:
	print(a)
	
print(u'斐波拉契数列-函数:')
def fib(max):
	a,b,n = 0,1,0
	while n<max:
		print(b)
		a,b=b,a+b
		n = n+1
	return 'done'

print(fib(6))

print(u'斐波拉契数列-generator:')
def fib_g(max):
	a,b,n = 0,1,0
	while n<max:
		yield b
		a,b=b,a+b
		n=n+1
	return 'done'
	
for g in fib_g(6):
	print(g)
print(fib_g(6))

print(u'可以输出return的斐波拉契数列-generator:')
g = fib_g(6)
while True:
	try:
		x = next(g)
		print('g:',x)
	except StopIteration as e:
		print('Generator return value :',e.value)
		break