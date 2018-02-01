# -*- coding: utf-8 -*-


def power(x):
	return x*x

t = power(5)
print("power 5 :\n%d"%t)

def double_power(x,n):
	s = 1
	while n>0:
		n = n-1
		s = s*x
	return s

dt = double_power(5,2)
print("double_power 5 2:\n%d"%dt)

def default_power(x,n=2):
	s = 1
	while n>0:
		n = n-1
		s = s*x
	return s

vt = default_power(5)
print("default_power 5 :\n%d"%vt)
vt = default_power(5,2)
print("default_power 5 2:\n%d"%vt)

def add_end(L=[]):
	L.append("end")
	return L

add_end()
L = add_end()
print("add_end() use for twice:\n",L)

def add_end_one(L=None):
	if L is None:
		L=[]
	L.append("end")
	return L

add_end_one()
L = add_end_one()
print("add_end_one() use for twice:\n",L)
		