# -*- coding: utf-8 -*-

#功能：去除字符串首尾的空格
print(u"功能：去除字符串首尾的空格")
def trim(s):
	n = 0
	if len(s) == 0:
		return ""
	while s[n] == " " and n < len(s) - 1:
		n=n+1
		if n == len(s)-1:
			return ""
	a = n
	while a < len(s)-1 and s[a] != " ":
		if a < len(s)-1:
			a=a+1	
	if a == len(s)-1:
		a = a+1
	return s[n:a]
			
if trim("Hello  ") != "Hello" :
	print(u"测试失败1")
elif trim("  Hello  ") != "Hello" :
	print(u"测试失败2")
elif trim("Hello") != "Hello" :
	print(u"测试失败3")
elif trim("    ") != "" :
	print(u"测试失败4")
elif trim("") != "" :
	print(u"测试失败5")
else:
	print(u"测试成功")