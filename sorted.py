# -*- coding: utf-8 -*-
print(u'排序算法：')
L = [36,5,-12,9,-21]
print(u'origin:\n',L)
print(u'after sorted:\n',sorted(L))
print(u'after add key=abs:\n',sorted(L,key=abs))
print(u'反序Reverse：')
print(u'after sorted with key=abs and reverse=True:\n',sorted(L,key=abs,reverse=True))
print('>>>------------------------------------------------------------------------<<<')
print(u'字母排序‘A’ - ‘Z’ - ‘a’ - ‘z’:')
name = ['bob','about','Zoo','Credit']
print(u'origin:\n',name)
print(u'after sorted:\n',sorted(name))
print(u'after add key=str.lower:\n',sorted(name,key=str.lower))
print(u'反序Reverse：')
print(u'after sorted with key=str.lower and reverse=True:\n',sorted(name,key=str.lower,reverse=True))
print('>>>------------------------------------------------------------------------<<<')