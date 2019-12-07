"""

while简单使用

Version:1.0
Author:chaishuai

"""
import random

number = random.randint(1, 100)
count = 0
while True:
    count += 1
    a = int(input("请输入一个整数:"))
    if a > number:
       print("大了，请小一点")
    elif a < number:
       print("小了，请大一点")
    else :
       print("恭喜你猜了%d次后答对了" % count)
       break