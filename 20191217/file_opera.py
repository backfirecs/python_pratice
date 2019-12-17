"""

文件操作

Version:1.0
Author:chaishuai

"""
import os
import random
# 文件操作
def main():
    f =None
    # 一次全部读取
    try:
        f = open('./20191217/侠客行.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()

    # 逐行读取
    with open('./20191217/侠客行.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line)
    with open('./20191217/侠客行.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        print(lines)
   
    # 写文件
    filenames = ['./20191217/a.txt', './20191217/b.txt', './20191217/c.txt']
    files = []
    for filename in filenames:
        files.append(open(filename, 'a', encoding='utf-8'))
        
    for file in files:
        file.write(str(random.randint(1, 100)))
        file.close()

    # 读写二进制文件
    with open('./20191217/test.png', 'rb') as fs1:
        data = fs1.read()
    with open('./20191217/test2.png', 'wb') as fs2:
        fs2.write(data)


if __name__ == '__main__':
    main()