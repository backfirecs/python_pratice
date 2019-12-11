"""

字典的简单使用
1.创建字典
2.遍历字典
3.获取字典中的元素
4.更新字典中的元素
5.删除字典中的元素
6.清空字典

Version:1.0
Author:chaishuai

"""

# 创建字典
dict1 = {'uid':123, 'gender':'male'}# 字面量语法创建
print(dict1)
dict2 = dict(uid=123, gender='male') # 构造器语法创建
print(dict2)
dict3 = dict(zip(['a', 'b', 'c'], '123'))# 通过zip将两个序列压缩成字典
print(dict3)
dict4 = {x: x**2 for x in range(10)} # 通过推导式语法创建
print(dict4)

# 获取字典中的元素
print(dict1['uid'])
print(dict1.get('age', 26))

# 遍历字典中的元素
for key in dict1:
    print(key, dict1[key])

# 更新字典中的元素
dict1['gender'] = 'female'
dict1['department'] = 'engineer'
dict1.update(uid=1, nickname='backfirecs')
print(dict1)

# 删除字典中的元素
print(dict1.popitem())
print(dict1.popitem())
print(dict1)
print(dict1.pop('uid')) # 如果元素不存在会引发异常
print(dict1)

# 清空字典
dict1.clear()
print(dict1)