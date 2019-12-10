"""

字符串的简单使用

Version:1.0
Author:chaishuai

"""

# 单引号双引号都可以
s1 = "Hello world!"
s2 = 'Hello world!'
print(s1)
print(s2)
# 多行字符串可以使用三个双引号
s3 = """
Line1
Line2
Line3
"""
print(s3)

# \可以用来转义,使用编码表示字符
s4 = '\142' # 八进制
s5 = '\61x' # 十六进制
s6 = '\u67f4' # Unicode编码
print(s4)
print(s5)
print(s6)

# 可以使用r来表示不需要转义
s7 = r'\142'
print(s7)

"""
字符串处理
1.字符串拼接
2.字符串重复
3.字符串包含
4.字符串切割
5.字符串常用函数
6.格式化字符串
"""
# 字符串使用 + 拼接
s8 = "Hello" + " World!"
print(s8)
# 字符串使用*重复
s9 = "Hello World!" * 5
print(s9)
# 字符串包含in,不包含not in
s10 = "我是一个字符串"
print("我" in s10)
print("你" not in s10)
# 字符串切片
s11 = "我是一个字符串too"
print(s11[2])# 取出指定位置的字符串 "一"
print(s11[2:8])# 根据开始索引和结束索引取出字符串,包前不包后, "一个字符串t"
print(s11[2:])# 根据开始索引一直切片到字符串结束，"一个字符串too"
print(s11[2::2])# 根据开始索引和步长来切片字符串, "一字串o"
print(s11[::2])# 根据步长从字符串开头切片字符串, "我一字串o"
print(s11[::-1])# 根据步长从字符串结尾切片字符串, "oot串符字个一是我"
print(s11[-3:-1])# 负数代表从结尾开始的索引(注意从结尾开始第一个索引是-1，不是0)
# 字符串常用函数
s12 = "我是一个字符串tootoo, hello,day"
print(len(s12)) # 获取字符串长度
print(s12.capitalize()) # 字符串首字母大写
print(s12.title()) # 字符串每个单词首字母大写
print(s12.upper()) # 字符串全部大写
print(s12.find("字符串")) # 查找字符串
print(s12.find("川建国")) # 查找字符串,如果查找不到返回-1
print(s12.index("字符串")) # 查找字符串,如果查找不到会引发异常
print(s12.startswith("我")) # 检查字符串是否以指定字符串开头
print(s12.endswith("y")) # 检查字符串是否以指定字符串结尾
print(s12.center(50, '*'))# 将字符串以指定的宽度居中并在两侧填充
print(s12.rjust(50, '*'))# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(s12.isdigit())# 检查字符串是否是只由数字构成
print(s12.isalpha()) # 检查字符串是否是只由字母构成
print(s12.isalnum()) # 检查字符串是否仅由字母和数字组成
print(s12.strip()) # 去除字符串左右两边的空格

# 格式化字符串
a, b = 5, 10
print('%d * %d = %d' % (a, b, a * b))
print('{0} * {1} = {2}'.format(a, b, a * b))
print(f'{a} * {b} = {a * b}') #Python3.6以后可以使用
