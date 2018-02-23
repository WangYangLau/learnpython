# -*- coding: utf-8 -*-

print(u'使用匿名函数：')
print('list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9]:')
print('[1, 2, 3,  4,  5,  6,  7,  8,  9]')
print(list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9])))

print('>>>------------------------------------------------------------------------<<<')	
print(u'把匿名函数作为返回值：')
def build(x,y):
	return lambda:x*x+y*y
a = build(2,3)
print(u'a = build(2,3), a =',build(2,3))
print(u'a() = ',a())
