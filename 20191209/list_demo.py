"""

列表的简单实用

Version:1.0
Author:chaishuai

"""

list = [1, 3, 5, 7, '100'] # 列表可以设置不等同的数据类型
print(list)
# 列表可以通过*来重复
list2 = list * 3 
print(list2)
# 获取列表长度
print(len(list)) 
# 通过下标获取列表中的元素
print(list[1])
print(list[-1])

# 通过循环用下标遍历列表元素
for index in range(len(list)):
    print(list[index])
   
# 通过for循环用下表遍历列表元素
for element in list:
    print(element)
# 通过enumerate函数处理列表之后再遍历
for index,element in enumerate(list):
    print(index, element)

# 添加及移除元素
# 添加元素
list.append(200) # 在列表尾部添加一个元素
list.insert(1, 500) # 在指定位置插入一个元素 
print(list)
list += [799,900]
print(list)
# 判断元素存储不存在列表中
print(100 in list)
list.insert(1, 100)
list.insert(5,100)
# 移除元素
list.remove(100) # 删除第一个与给定值相同的元素， 不存在会引起异常
print(list)
list.pop(0) # 移除指定索引的元素
list.pop(-1)
print(list)
#遍历列表时可以改变元素长度
for index, element in enumerate(list):
    if index == 1:
        list.insert(2, 1000)
    print(index, element)
print(list)
# 清空列表
list.clear()
print(list)

# 列表分片
list3 = ["grape", "apple", "banana", "strawberry", "waxberry"]
print(list3[1:3]);
print(list3[:]);
print(list3[-3:-2]);
print(list3[::-1]);

# 列表排序
print(sorted(list3)) # 默认按照字母顺序排序，返回的是列表的拷贝，此方法排序不改变原有列表
print(sorted(list3, key = len, reverse = True)) # 默认按照长度排序，返回的是列表的拷贝，此方法排序不改变原有列表
list4 = [1,2,3,4,65,45,78,11, 2.56]
print(sorted(list4)) # 如果列表中都为数字(包括整型和浮点型)的话默认按照升序排序,如果由其他类型的数据会引起异常
list4.sort(reverse = True)
print(list4) # 这种通过列表对象调用sort方法来排序的方式会改变原有列表的顺序

# 生成式和生成器
f = [x for x in range(1, 10)] # 通过生成式生成列表
print(f)
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)
f = [x ** 2 for x in range(1, 1000)]
import sys
print(sys.getsizeof(f)) # 这种语法创建列表之后就已经把元素准备就绪所以比较耗内存
f= (x ** 2 for x in range(1, 1000)) # 注意这个式生成器,通过生成器可以获取到数据但是不占用额外的空间，每次获取数据的时候就通过内部运算得到数据（需要花费额外的时间）
print(sys.getsizeof(f))
print(f)

def fib(n):
    a,b = 0, 1
    for _ in range(n):
        a, b = b, a+b
        yield a

for val in fib(20):
    print(val)