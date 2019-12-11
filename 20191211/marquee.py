"""

屏幕显示文字跑马灯效果

Version:1.0
Author:chaishuai

"""

import os
import time
content = '我是一个跑马灯......'
start_index = 0
if os.name == 'nt':
    clear_command = 'cls'
else:
    clear_command = 'clear'
while True:
    time.sleep(0.2)
    os.system(clear_command)
    print(content[start_index:])
    start_index += 1
    if start_index == len(content):
        start_index = 0