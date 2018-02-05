# -*- coding: utf-8 -*-
#功能：使含有整数的List中的字符变小写
print(u"功能：使含有整数的List中的字符变小写")

L = ['Hello','World',18,'Apple',None]
L2 = [l.lower() for l in L if isinstance(l,str)]

print(L2)
if L2 == ['hello','world','apple']:
	print(u'测试通过！')
else:
	print(u'测试失败！')
	
#注意：列表生成式中，如果，有if判断，列表中不符合判断内容的都不会生成在列表当中
print(u'列表生成式中，如果，有if判断，列表中不符合判断内容的都不会生成在列表当中')