
"""

打印三角形

Version:1.0
Author:chaishuai

"""
row = int(input("请输入行数:"))
for x in range(row):
    str = ''
    for j in range(x+1):
        str = str + '*'
    print(str)
print()
for x in range(row):
    str = ''
    for j in range(x+1):
        str = str + '*'
    print(str)