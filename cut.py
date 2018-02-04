# -*- coding: utf-8 -*-

L = ["Amy","Kit","Bart","John","Jack"]

print('The origin :\n%s'%L)
print('The 1st to the 3th :\n%s'%L[0:3]) 
print('The 2nd to the 3th :\n%s'%L[2:3])
print('The last one to the 2nd to the last :\n%s'%L[-2:])
print('The 2nd to the last :\n%s'%L[1:len(L)])

print(u"创建一个有序数列：\n%s"%range(10))
print(u"前8个数，每两个取一个：\n%s"%range(10)[:8:2])
print(u"所有数里，每5个取一个：\n%s"%range(10)[::5])
print(u"Tuple和str都可以用切片")