"""

设计一个函数返回传入的列表中最大和第二大的元素的值

Version:1.0
Author:chaishuai

"""

def get_max2(list_value):
    max1, max2 = None, None
    if list_value is None or len(list_value) == 0:
        return False
    for value in list_value:
        if type(value) == int or type(value) == float:
            if max1 == None:
                max1 = value
            elif max1 < value:
                max2 = max1
                max1 = value
    return (max1, max2)

if __name__ == '__main__':
    test_list = [1,4,6,15,66,13,100,3,3, '1000', True]
    print(get_max2(test_list))