# -*- conding:utf-8 -*-

print(u'用filter筛选出奇数：')
def is_odd(n):
	return n%2 == 1

print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9,0])))
print('>>>------------------------------------------------------------------------<<<')
print(u'筛选出非空字符串：')	
def not_empty(s):
	return s and s.strip()	

print(list(filter(not_empty,['A',' ','B','  ','   ','','C'])))
print(u's.strip(‘字符’)去除字符串头尾的‘字符’（默认空格）')
print('>>>------------------------------------------------------------------------<<<')
print(u'用埃氏筛法筛选出素数：')

#生成奇数序列
def _odd_iter():
	n=1
	while n<30:
		n = n+2
		yield n
	
#筛选条件
def _not_divisible(n):
	return lambda x:x%n>0
	
#执行函数
def primes():
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n),it)
		#_not_divisible(n)相当于def func(x):
		#							return x%n>0
	
b = _not_divisible(3)(2)
print(b)
L = primes()
print(list(L))
print(u'_not_divisible(n)相当于def func(x): return x%n>0')	