"""

面向对象的一些简单联系

Version:1.0
Author:chaishuai

"""

class Person(object):

    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @name.setter # 如果没有这个注解的方法，那么这个属性就只读的
    def name(self, name):
        self._name = name

    @age.setter
    def age(self, age):
        self._age = age

def main():
    uzi = Person('uzi', 23)
    print(uzi.name, uzi.age)
    uzi.name = '简自豪'
    uzi._age = 100
    uzi.age = 105
    uzi._gender = 'male'
    # uzi._phone = '13333333333'
    print(uzi.name, uzi.age, uzi._gender, uzi._age)

if __name__ == '__main__':
    main()