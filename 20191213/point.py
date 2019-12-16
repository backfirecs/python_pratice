"""

描述两点之间距离

Version:1.0
Author:柴帅

"""
import math
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def distance(self, point):
        return print(math.sqrt((self.x - point.get_x()) ** 2 + (self.y - point.get_y()) ** 2))

def main():
    point1 = Point(10, 10)
    point2 = Point(15, 15)
    print(point1.distance(point2))

if __name__ == '__main__':
    main()