"""

输入三条边长，如果能构成三角形就计算周长和面积

Version:1.0
Author:chaishuai

"""

a = int(input("请输入第一条边的长"))
b = int(input("请输入第二条边的长"))
c = int(input("请输入第三条边的长"))

if (a + b > c) or (a +c >b) or (b + c >a):
    permimeter = a + b + c
    p = (a + b +c) /2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print("周长:%.2f, 面积:%.2f" % (permimeter, area))
else:
    print("不是三角形");