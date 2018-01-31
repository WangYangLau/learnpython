# -*- coding:utf-8 -*-

s1 = set([1,1,2,2,3,3,4])
s2 = set([1,3,5,6])
print("origion set 1:\n",s1)
print("origion set 2:\n",s2)
s1.add(5)
print("after set 1 add:\n",s1)
s1.remove(5)
print("after set 1 remove:\n",s2)

print("after set 1&2:\n",s1 & s2)
print("after set 1|2:\n",s1 | s2)

L=[11,13,12]
print("origion List:\n",L)
s = set(L)
print("after set:\n",s)
L.sort()
print("after sort:\n",s)
s = set('abc')
print("after set str:\n",s)

T1 = (3,2,1)
T2 = (4,3,[2,1])
s1 = set(T1)
s2 = set(T2)
print("origion Tuple1:\n",T1)
print("origion Tuple2:\n",T2)
print("after set tuple 1:\n",s1)
print("after set tuple 2:\n",s2)