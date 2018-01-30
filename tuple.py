# -*- coding：utf-8 -*-

#tuple
print('Tuple is unchangeable')
classmates = ('Amy','Kit','John')
print('origion :\n',classmates)

#List in tuple
print('List in tuple is changeable')
print('origin :')
mates = ('Amy','Kit',['John','Jack'])
print('List in tuple :\n',mates)
mates[2].append('Adam')
print('After append :\n',mates)
mates[2].insert(2,'Marry')
print('After insert 2 :\n',mates)
mates[2].pop()
print('After pop :\n',mates)
mates[2].pop(2)
print('After pop 2 :\n',mates)