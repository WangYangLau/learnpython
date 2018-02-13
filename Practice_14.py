# -*- coding: utf-8 -*-

from functools import reduce
#功能：把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
print(u'把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字:')

def normalize(name):
	return name.capitalize()
	
L = ['adam', 'LISA', 'barT']
L2 = list(map(normalize,L))
print(L2)
print(u'使用了capitalize()')
print('>>>------------------------------------------------------------------------<<<')

#功能：接受一个list并利用reduce()求积
print(u'接受一个list并利用reduce()求积:')

def prod(L):
	def mul(x,y):
		return x*y
	return reduce(mul,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print(u'测试成功!')
else:
    print(u'测试失败!')
print('>>>------------------------------------------------------------------------<<<')

#功能：用map和reduce把字符串'123.456'转换成浮点数123.456
print(u'把字符串\'123.456\'转换成浮点数123.456：')

d = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'.':'.'}

def str2num(s):
	return d[s]
	
L = list(map(str2num,'123.456'))

for index,item in enumerate(L):
	if item == '.':
		L1 = L[:index]
		L2 = L[index+1:]
	else:
		pass

def fn(x,y):
	return x*10+y
	
def str2float(s):
	return reduce(fn,L1) + reduce(fn,L2)/(10**len(L2))

if str2float('123.456') == 123.456:
	print(u'成功')
else:
	print(u'失败')
print('>>>------------------------------------------------------------------------<<<')
print(u'本次没用的技巧')
print(u'以某字符来分割字符串可以用str.split(\'字符串\')[第几段]')