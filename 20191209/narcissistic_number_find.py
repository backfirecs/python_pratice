
"""

找出所有水仙花数

Version:1.0
Author:chaishuai

"""

for x in range(100, 1000):
    a = x % 10 # 个位数
    b = x // 10 % 10 # 十位数
    c = x // 100 # 百位数
    if a * a * a + b * b * b + c * c * c == x:
        print(x)
