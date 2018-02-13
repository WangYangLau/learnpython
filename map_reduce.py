# -*- coding:utf-8 -*-

from functools import reduce
from collections import Iterable
from collections import Iterator

def maye(s):
	d = {'0':0,'1':1,'2':2,'3':3}
	return d[s]

print(list(map(maye,'123')))

def reye(x,y):
	return x*10+y
	
print(reduce(reye,map(maye,'123')))

print(isinstance('123',(Iterator)))
print(isinstance('123',(Iterable)))
