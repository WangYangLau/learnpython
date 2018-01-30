# -*- coding: utf-8 -*-

#List

print('List')
classmates = ['Amy','Kit','John']
print(classmates[0])
print(classmates[1])
print(classmates[2])
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])

print('origion :\n',classmates)
classmates.append('Adam')
print('After append :\n',classmates)
classmates.insert(2,'Jack')
print('After insert 2 :\n',classmates)
classmates.pop()
print('After pop :\n',classmates)
classmates.pop(2)
print('After pop 2 :\n',classmates)

#List in list
print('List in list')
mates = ['Amy','Kit',['John','Jack']]
print('origion :\n',mates)
print('List in list :\n',mates[2])
print('one of the list in list :\n',mates[2][1])