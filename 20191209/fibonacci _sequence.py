"""

生成斐波那契数列的前二十个数

Version:1.0
Author:chaishuai

"""

num1 = 1
num2 = 1
cur_num = 0
sequence = '1 1'
count = 0
while True:
    if count == 18:
        break
    count += 1
    cur_num = num1 + num2
    num1 = num2
    num2 = cur_num
    sequence += ' ' + str(cur_num)
print(sequence)
