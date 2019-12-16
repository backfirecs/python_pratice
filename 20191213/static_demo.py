"""

静态方法的使用

Version:1.0
Author:chaishuai

"""

import math

class Triangle(object):

    __slots__ = ('_a', '_b', '_c')

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return math.sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))

def main():
    a, b, c = 3, 4, 5
    if Triangle.is_valid(a, b, c):
        triangle = Triangle(a, b, c)
        print(f'周长:{triangle.perimeter()}, 面积:{triangle.area()}')
    else:
        print('无法构成三角形')

if __name__ == '__main__':
    main()