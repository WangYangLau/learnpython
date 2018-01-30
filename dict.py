# -*- coding:utf-8 -*-

#dict
index = False
print('dict')
d = {'Michael':80,'Lisa':95,'Jack':72,'Bart':0}
d['Bart'] = 98
while index==False:
	print('enter the name you find:')
	name = input()
	index = name in d
	if index==False:
		print('Without this guy,Do you want to insert one?(yes/no)')
		a = input()
		if a=='yes':
			d.setdefault(name,0)
			print(d)
		else:
			pass
	else:
		pass
print('Have this guy,enter his score:')
score = input()
d[name] = score
print(d)
print('Lisa' in d) #返回True or False

