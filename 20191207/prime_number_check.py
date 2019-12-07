"""

判断一个数是不是素数

Version:1.0
Author:chaishuai
"""

import math

number = int(input("请输入一个数字:"))
end = int(math.sqrt(number))
is_prime = True
for x in range(2, end +1):
    if number % x == 0:
        is_prime = False
    break;
if number !=1 and is_prime == True:
    print("%d 是素数" % number)
else:
    print("%d 不是素数" % number)