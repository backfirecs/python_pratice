"""

判断一个数是不是回文数

Version:1.0
Author:chaishuai

"""



def is_palindrome(num):
    resversed_num = reverse_num(num)
    return num == resversed_num



def reverse_num(num):
    rnum = 0;
    while True:
       if rnum != 0:
           rnum = rnum * 10
       rnum += num % 10
       num = num //10
       if num < 10:
           rnum = rnum * 10 + num
           break
    return rnum

def is_prime(num):
    for x in range(2, num+1):
        if x != num and num % x ==0 and num != 1:
            return False
    return True
            
num = int(input("请输入一个正整数:"))
print('是回文素数') if is_palindrome(num) and is_prime(num) else print("不是回文素数")        