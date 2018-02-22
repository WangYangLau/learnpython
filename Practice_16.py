# -*- coding:utf-8 -*-
#功能：对tuple表示的学生名字和成绩，按名字排序：

L = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]

print(u'对tuple表示的学生名字和成绩，按名字排序：')

def by_name(t):
	return t[0]

L2 = sorted(L, key=by_name)
print(L2)

print('>>>------------------------------------------------------------------------<<<')
print(u'对tuple表示的学生名字和成绩，按成绩排序：')

def by_score(t):
	return t[1]
	
L2 = sorted(L, key=by_score)
print(L2)