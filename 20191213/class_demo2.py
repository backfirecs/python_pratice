"""

类继承的简单使用

Version:1.0
Author:chaishuai

"""

class Person(object):
    __slots__ = ('_name', '_age')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @name.setter
    def name(self, name):
        self._name = name

    @age.setter
    def age(self, age):
        self._age = age


class Student(Person):

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print(f'{self.grade}的{self.name}正在学习{course}')

def main():
    stu1 = Student('James', 25, '一年级')
    stu1.name = 'jack'
    stu1.study('软件工程')
    stu1._age = 100
    print(stu1._age)
    stu1._grade = '二年级'
    print(stu1._grade)

if __name__ == '__main__':
    main()