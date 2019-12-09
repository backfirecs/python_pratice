"""

输入两个正整数,计算它们的最大公约数和最小公倍数

Versoin:1.0
Author:chaishuai

"""

a = int(input("请输入第一个数:"))
b = int(input("请输入第二个数:"))
end = a if a < b else b
for x in range(end+1,0,-1):
    if a % x == 0 and b % x == 0:
        print("%d和%d的最大公约数是%d" % (a, b, x))
        print("%d和%d的最小公倍数是%d" % (a, b, a * b // x))
        break