# -*- coding: utf-8 -*-

#功能：汉诺塔
def move(n,a,b,c):
	if n == 1:
		print(a,'-->',c)
	else:
		move(n-1,a,c,b)
		move(1,a,b,c)
		move(n-1,b,a,c)
		
#理解 n = 1,a放一个到c；n = 2，a放2个到c		
print(u"功能：汉诺塔")		
move(3,'A','B','C')
		
	