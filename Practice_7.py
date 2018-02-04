# -*- coding:utf-8 -*-

#功能：求一元二次方程的解
print(u"功能：求一元二次方程的解")
import math

def quadratic(a,b,c):

	d = (b*b-4*a*c)
	if d > 0:
		e1 = (-b + math.sqrt(b*b-4*a*c))
		e2 = (-b - math.sqrt(b*b-4*a*c))
		
	else:
		pass		
	if not isinstance(a,(int,float)):
		raise TypeError(u"参数a只能为整数型和浮点型") 
	if not isinstance(b,(int,float)):
		raise TypeError(u"参数b只能为整数型和浮点型") 
	if not isinstance(c,(int,float)):
		raise TypeError(u"参数c只能为整数型和浮点型") 
	if a == 0:
		raise TypeError(u"参数a不能为0")
	else:
		if d >0:
			return e1/(2*a),e2/(2*a)
		elif d ==0:
			return -(b/2*a),-(b/2*a)
		else:
			return None,None

x1,x2=quadratic(2,3,1)
print(x1,x2)	
x1,x2=quadratic(1,2,1)
print(x1,x2)		

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print(u'测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print(u'测试失败')
else:
    print(u'测试成功')