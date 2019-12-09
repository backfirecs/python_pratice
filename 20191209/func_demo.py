"""

函数的简单使用

Version:1.0
Author:chaishuai

"""

def add(a = 10, b = 100):
    return a + b


print(add())
print(add(5, 20))


def add2(*args):
    return args[0] + args[1]

print(add2(5, 20, 30, 50))