# -*- coding:utf-8 -*-

def calc(*number):
	sum = 0
	for n in number:
		sum = sum + n*n
	return sum

L = [1,2,3]	
s = calc(1,2,3)
print("changeable_para calc(*number) 1 2 3:\n%d"%s)
s = calc(4,5)
print("changeable_para calc(*number) 4 5:\n%d"%s)
s = calc(*L)
print("L =",L)
print("changeable_para calc(*number) *L:\n%d"%s)


print("key_para,a para which can expand **kw")
def person(name,age,**kw):
	print("name :",name,"\nage :",age,"\nothers :",kw)
	
print("person(\"Kit\",18,city=\"Beijing\",sex=\"F\")")
person("Kit",18,city="Beijing",sex="F")
print("a dict d:")
d={"city":"Beijing","sex":"F"}
print(d)
print("person(\"Kit\",18,**d)")
person("Kit",18,**d)
	

