# -*- coding: utf-8 -*-

def findMinAndMax(L):
	if L == []:
		return (None,None)
	else:
		Min = L[0]
		Max = L[0]
	for l in L:
		if not isinstance(l,(int,float)):
			raise TypeError(u"List中存在非int或float类型成员")
		if l > Max:
			Max = l
		elif l < Min:
			Min = l
		else:
			pass
	return (Min,Max)

if findMinAndMax([]) != (None,None):
	print(u'测试失败！')
elif findMinAndMax([7]) != (7,7):
	print(u'测试失败！')
elif findMinAndMax([7,1]) != (1,7):
	print(u'测试失败！')
elif findMinAndMax([7,1,3,9,5]) != (1,9):
	print(u'测试失败！')
else:
	print(u'测试成功！')
	