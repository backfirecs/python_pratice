"""

正整数反转

Version:1.0
Author:chaishuai

"""

num = int(input("请输入一个正整数:"))
reversed_num = ''
while True:
   if (num < 10):
       reversed_num += str(num)
       break
   a = num % 10
   reversed_num += str(a)
   num = num // 10
print(reversed_num)


