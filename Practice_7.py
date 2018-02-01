# -*- coding:utf-8 -*-

import math

def quadratic(a,b,c):

	d = (b*b-4*a*c)
	if d > 0:
		e1 = (-b + math.sqrt(b*b-4*a*c))
		e2 = (-b - math.sqrt(b*b-4*a*c))
	else:
		pass
		
	#if not isinstance(a,b,c(int,float))
	if a == 0:
		return None,None
	else:
		if d >0:
			return e1/2*a,e2/2*a
		elif d ==0:
			return -(b/2*a),-(b/2*a)
		else:
			return None,None

x1,x2=quadratic(1,3,-4)
print(x1,x2)	
x1,x2=quadratic(1,2,1)
print(x1,x2)
x1,x2=quadratic(0,0,0)
print(x1,x2)		