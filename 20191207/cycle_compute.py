"""
输入半径计算圆的周长和面积

Version:1.0
Author:chaishuai

"""
import math

radius  = float(input("请输入圆的半径:"))
perimeter = radius * 2 * math.pi
area = radius * radius *math.pi
print("周长:%.1f" % perimeter);
print("面积:%.1f" % area);