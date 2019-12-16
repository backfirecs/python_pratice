"""

类方法的简单实用

Version:1.0
Author:chaishuai

"""

import time
import os

class Clock(object):
    __slots__ = ('_hour', '_minute', '_second')

    def __init__(self, hour, minute, second):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = time.localtime(time.time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    @property
    def hour(self):
        return self._hour

    @property
    def minute(self):
        return self._minute

    @property
    def second(self):
        return self._minute

    @hour.setter
    def hour(self, hour):
        self._hour - hour

    @minute.setter
    def minute(minute):
        self._minute = minute

    @second.setter
    def second(second):
        self._second = second

    def hour_move(self):
        if (self._hour == 23):
            self._hour = 0
        else:
            self._hour += 1

    def minute_move(self):
        if (self._minute == 59):
            self._minute = 0
            self.hour_move()
        else:
            self._minute += 1

    def second_move(self):
        if (self._second == 59):
            self._second = 0
            self.minute_move()
        else:
            self._second += 1

    def run(self):
        while True:
            time.sleep(1)
            self.second_move()
            self.show()

    def show(self):
        show_hour = str(self._hour) if self._hour >= 10 else '0' + str(self._hour)
        show_minute = str(self._minute) if self._minute >= 10 else '0' + str(self._minute)
        show_second = str(self._second) if self._second >= 10 else '0' + str(self._second)
        os.system('cls')
        print(f'{show_hour}:{show_minute}:{show_second}')

def main():
    clock = Clock.now()
    clock.run()

if __name__ == '__main__':
    main()