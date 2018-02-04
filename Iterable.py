# -*- coding: utf-8 -*-

# 迭代
#判断是否可以迭代
from collections import Iterable

L=["Amy","Bart","Jack","John","Kit"]
D={"Amy":85,"Bart":98,"Jack":75,"John":70,"Kit":90}
str="iampeter"



print(u"迭代List:")
if isinstance(L,Iterable):
	for l in L:
		print(l)
	
print(u"\n迭代dict.key:")
if isinstance(D,Iterable):
	for d in D:
		print(d)

print(u"\n迭代dict.value:")
if isinstance(D,Iterable):
	for dv in D.values():
		print(dv)
	
print(u"\n同时迭代dict.key&value:")
if isinstance(D,Iterable):
	for k,v in D.items():
		print(k,v)
	
print(u"\n迭代字符串：")
if isinstance(str,Iterable):
	for s in str:
		print(s)
#enumerate
print(u"\n把List变成索引-元素对")
for i,v in enumerate(L):
	print(i,v)