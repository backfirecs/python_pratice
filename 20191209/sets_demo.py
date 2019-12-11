"""

集合的简单使用

Version:1.0
Author:chaishuai

"""
#创建集合
set1 = {1, 2, 3, '4'} # 使用字面量语法创建
print(set1)
set2 = set(range(10)) # 使用构造器创建
set3 = set((1, 3, 5))
print(set2)
print(set3)
set4 = {x ** 2 for x in range(10) if x % 2 != 0} # 使用推到是语法
print(set4)

#添加和删除集合元素
set5 = {1, 2, 3, 4, '5'}
set5.add('6'); #添加的元素顺序不固定
print(set5)
set5.update([2, 3, 8, '6', '10']) # 如果集合中没有元素则添加
print(set5)
set5.discard(2)# 如果集合中有这个元素删除，没有这个元素不做任何事
print(set5)
set5.remove(3)# 如果集合中有这个元素则删除，没有这个元素则会引发异常
print(set5)
set5.pop()
print(set5) # 删除集合中的第一个元素,如果集合为空，那么会引发异常

# 求集相关操作
set6 = {1, 2, 3, '4'}
set7 = {3, '4', '5', 6}
# 交集
print(set6 & set7) 
print(set6.intersection(set7))
# 并集
print(set6 | set7)
print(set6.union(set7))
# 差集
print(set6 - set7)
print(set6.difference(set7))
# 对称差集
print(set6 ^ set7)
print(set6.symmetric_difference(set7))
# 判断子集和超集
print(set6 <= set7)
print(set6.issubset(set7))
print(set6 >= set7)
print(set6.issuperset(set7))