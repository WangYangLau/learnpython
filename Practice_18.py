# -*- coding:utf-8 -*-
#功能：使用匿名函数修改代码
print(u'功能：使用匿名函数修改代码：')
print('>>>------------------------------------------------------------------------<<<')	
print(u'源代码：')
print(u'def is_odd(n):\n	return n % 2 == 1')

def is_odd(n):
	return n % 2 == 1
	
L = list(filter(is_odd,range(1,20)))
print(L)
print('>>>------------------------------------------------------------------------<<<')	
print(u'修改后：')
print(u'lambda n:n%2==1')
L = list(filter(lambda n:n%2==1,range(1,20)))
print(L)