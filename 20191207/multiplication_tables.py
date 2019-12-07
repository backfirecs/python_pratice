"""

打印一个九九乘法表

Version:1.0
Author:chaishuai

"""

for i in range(1,10):
    line = ""
    for j in range(1,10):
        if (line == ''):
            line = str(i) + "*" + str(j) + " = " + str(i * j)
        else:
            sprator = "     ";
            if i * j  >= 10:
                sprator = "    "
            line = line + sprator + str(i) + "*" + str(j) + " = " + str(i * j)
    print(line)
