# -*- coding: utf-8 -*-

def fact(n):
	if n == 1:
		return 1
	else:
		return n*fact(n-1)
		
		
print("尾递归:")
def fact_back(n,p):
	if n == 1:
		return p
	else:
		return fact_back(n-1,n*p)
	
def fact_back_use(n):
	return fact_back(n,1)

a = fact_back_use(5)
print(a)