# -*- coding: utf-8 -*-

def person(name,age,*,city,sex):
	print(name,age,city,sex)
	
print("key_name_para,after '*',need to enter key,but can change the position")	
person("Amy",18,sex="F",city="Beijing")

print(u"参数定义顺序：必选参数，默认参数，可变参数，命名关键字参数，关键字参数")

def person_mix(name,city="Beijing",*pet,age,sex,**kw):
	print("name :",name,"\ncity :",city,"\npet :",pet,"\nage :",age,"\nsex :",sex,"\nothers :",kw)

person_mix("Bart","Beijing","dog","cat",sex="M",age="18",Dad="Bob",Mon="Kit")
print(u"默认参数和可变参数不可连用，默认参数会没用")