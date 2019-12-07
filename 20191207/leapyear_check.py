"""

检查输入的年份是否是闰年

Version:1.0
Author:chaishuai

"""


year =  int(input("请输入年份:"))
isLeapYear = (year % 4 == 0  and year % 100 != 0) or (year % 400 == 0) or (year % 3200 == 0 and year % 172800 == 0)
print(isLeapYear)
