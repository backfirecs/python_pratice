"""

找出10000以内的完美数

Version:1.0
Author:chaishuai

"""

for x in range(1, 10001):
    sum = 0
    for y in range(1, x + 1):
        if x % y == 0 and x != y:
            sum += y
    if sum == x:
        print(x)

