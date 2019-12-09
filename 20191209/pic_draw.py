"""

使用循环简单绘制一些图形
图形一:
*
**
***
****
*****
图形二
    *
   **
  ***
 ****
*****
图形三
    *
   ***
  *****
 *******
*********

Version:1.0
Author:chaishuai
"""

for row in range(1,6):
    line = ''
    for x in range(1,row + 1):
        line += '*'
    print(line)


for row in range(1, 6):
    line = ''
    for x in range(6, 0,-1):
        if x == 6 :
            line = ''
        elif x > row:
            line += ' '
        else:
            line += '*'
    print(line)

last_line_char = 5 * 2 - 1
center_index = 5
for row in range(1, 6):
    line = ''
    for x in range(1, 10):
        if x <= (center_index - row) or x >= (center_index + row):
            line += ' '
        else:
            line += '*'
    print(line)