# -*- coding: utf-8 -*-
#功能：利用闭包返回一个计数器函数，每次调用它返回递增整数：
print(u'功能：利用闭包返回一个计数器函数，每次调用它返回递增整数：')
print('>>>------------------------------------------------------------------------<<<')
print(u'方法一，使用全局变量：')
def createCounter():
	global n 
	n = 0
	def counter():
		global n
		n = n+1
		return n
	return counter
	
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
print('>>>------------------------------------------------------------------------<<<')	
print(u'方法二，使用生成器：')
def createCounter2():
	def g():
		n = 0
		while True:
			n = n+1
			yield n
	it = g()
	def counter2():	
		return next(it)
	return counter2
	
counterC = createCounter2()
print(counterC(), counterC(), counterC(), counterC(), counterC()) # 1 2 3 4 5
counterD = createCounter2()
if [counterD(), counterD(), counterD(), counterD()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')