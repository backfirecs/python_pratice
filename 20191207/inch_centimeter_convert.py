"""

英寸和厘米转换

Version:1.0
Author:chaishuai

"""

length = float(input('请输入长度:'))
unit = input('请输入单位:')

if unit == '英寸':
    print("%.1f 英寸等于 %.1f厘米" % (length, (length * 2.54)))
else:
    print("%f 厘米等于 %.1f英寸" % (length, (length * 0.39)))
    