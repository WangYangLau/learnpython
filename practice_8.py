# -*- coding: utf-8 -*-

#功能：可接收一个或多个数并计算乘积
print(u"功能：可接收一个或多个数并计算乘积")
def product(*number):
	s = 1
	if number is ():
		raise TypeError("参数不能为空")
	else:
		for n in number:
			if not isinstance(n,(int,float)):
				raise TypeError("参数只能为整数型或浮点型")
			s = s*n
		return s
	
sum = product(1,2,3)
print("sum = %s"%sum)

print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print(u'测试失败!')
elif product(5, 6) != 30:
    print(u'测试失败!')
elif product(5, 6, 7) != 210:
    print(u'测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print(u'测试失败!')
else:
    try:
        product()
        print(u'测试失败!')
    except TypeError:
        print(u'测试成功!')