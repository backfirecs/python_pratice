"""
简单使用ifelse

Version:1.0
Author:chaishuai

"""

score = float(input('请输入成绩:'))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'

print('评分为', grade)
   
