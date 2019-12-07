"""
内置函数变量类型转换

Version:1.0
Author:chaishuai
"""

# 将一个数值或者字符串转换成整数，不能转换成整数的将会报错（浮点数类型，浮点数字符串，不是数字的字符串，None，空串，空格），False=>0，true=>1
a = '123'
print(int(a))
# b = '123.00'
# print(int(b))
# c = 123.00
# print(int(c))
# d = None
# print(int(d))
e = True
print(int(e))
f = False
print(int(f))
# g = ''
# print(int(g))
# h = ' '
# print(int(h))

# 将一个字符串转换成浮点数，不能转换成浮点数的将会报错（不是数字的字符串，None，空串，空格），False=>0.0，true=>1.0
a1 = '123'
print(float(a1))
b1 = '123.00'
print(float(b1))
c1 = 123
print(float(c1))
# d1 = None
# print(float(d1))
e1 = True
print(float(e1))
f1= False
print(float(f1))
# g = ''
# print(int(g))
# h1 = ' '
# print(float(h1))

# 将指定的对象转换成字符串形式，可以指定编码，False=>'False'，True=>'True'，None=>'None' 
a3 = 123
print(str(a3));
b3 = 123.00
print(str(b3));
c3 = None
print(str(c3));
d3 = True
print(str(d3));
f3 = False
print(str(f3));

# 将整数转换成该编码对应的字符串（一个字符）
a4 = 97
print(chr(a4));

# 将字符串（一个字符）转换成对应的编码（整数）
a5 = 'a'
print(ord(a5));