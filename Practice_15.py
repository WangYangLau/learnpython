# -*- coding: utf-8 -*-
#功能：利用filter()筛选出回数（从左开始读和从右开始读，一样的数）：
print(u'功能：利用filter()筛选出回数（从左开始读和从右开始读，一样的数）：')
	
def is_palindrome(n):
	return str(n) == str(n)[-1::-1]

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
#使用了切片技巧
print(u'使用了切片技巧')