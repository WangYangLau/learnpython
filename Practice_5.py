# -*- coding: utf-8 -*-

L=['Bart','Lisa','Adam']
print('for_in')
for name in L:
	print('Hello,%s!'%name)

print('while')
n = 3
while n>0:
	print('Hello,%s!'%L[3-n])
	n=n-1
	