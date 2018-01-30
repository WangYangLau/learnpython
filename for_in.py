# -*- coding: utf-8 -*-

print('Your roommates:')
Names = ['Amy','Kit','John']
for name in Names:
	print(name)
	
print('How much num do you want to add?')
sum = 0
Numbers = int(input())+1
for num in range(Numbers):
	sum = sum + num
print('total is:')
print(sum)

#PS:变量记得初始化
#while

print(u'乱入的while：')
sum = 0
n = 100
while n>0:
	sum = sum+n
	n = n-1
print(sum)