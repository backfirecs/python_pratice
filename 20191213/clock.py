"""

一个简单的描述时间的类

Version:1.0
Author:chaishuai

"""
import time
import os
class Clock(object):
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def second_move(self):
        if self.second == 59:
            self.second = 0
            self.minute_move()
        else:
            self.second += 1
    def minute_move(self):
        if self.minute == 59:
            self.minute = 0
            self.hour_move()
        else:
            self.minute += 1
    def hour_move(self):
        if self.hour == 23:
            self.hour = 0
        else:
            self.hour += 1
    def move(self):
        self.second_move()
    def show(self):
        os.system('cls')
        show_hour = str(self.hour)
        show_minute = str(self.minute) if self.minute >= 10 else '0' + str(self.minute)
        show_second = str(self.second) if self.second >= 10 else '0' + str(self.second)
        print(f'时钟时间 {show_hour}:{show_minute}:{show_second}')

def main():
    clock = Clock(23, 59, 50)
    while True:
        time.sleep(1)
        clock.move()
        clock.show()

if __name__ == '__main__':
    main()
