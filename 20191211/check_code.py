"""

设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成

Version:1.0
Author:chaishuai

"""
import random

def genCode(length = 6):
    list1 = [chr(x) for x in range (65, 91)] # Unicode编码'A' - 'Z' => 65 - 90
    list2 = [chr(x) for x in range (97, 123)] # Unicode编码'a' - 'z' => 97 - 123
    list3 = list(range(0, 10))
    list_total = list1 + list2 + list3
    code = ''
    for _ in range(length):
        char = list_total[random.randint(0, len(list_total))]
        if  type(char) == int:
            char = str(char)
        code += char 
    return code


if __name__ == '__main__':
    length = int(input("请输入需要的验证码位数:"))
    code = genCode(length)
    print(code)