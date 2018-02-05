# -*- coding: utf-8 -*-
#列表生成
print(u"列表生成，for_in的进阶")
import os

print(u"生成List，1-10:")
L = list(range(1,11))
print(L)

print(u"生成List，1*1-10*10")
L = [x*x for x in range(1,11)]
print(L)
#注意添加[]

print(u"生成List，1-10偶数平方")
L = [x*x for x in range(1,11) if x%2==0]
print(L)
#注意，条件用if

print(u"生成List,两层循环，全排列")
L = [n+m for n in 'abc' for m in 'xyz']
print(L)

print(u"生成List,列出当前目录下所有文件和文件夹")
print(u"使用os模块")
L = [d for d in os.listdir('D:\learngit\\')]
print(L)

print(u"使用两个变量来生成List")
d ={'x':'A','y':'B','z':'C'}
L = [k+'='+v for k,v in d.items()]
print(L)

print(u"把List中字符串大写变小写")
print(u"使用了函数lower")
L = ['HELLO','WORLD','IBM','Apple']
print('origin : \n%s'%L)
L = [l.lower() for l in L]
print('After lower :\n%s'%L)