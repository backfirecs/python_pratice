"""

类与对象的简单使用

Version:1.0
Author:chaishuai

"""

class Student(object):
    # 相当于构造方法
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}')
    def __get_name(self):
        return self.name
def main():
    stu1 = Student('chaishuai', 26)
    stu1.study('程序设计')
    print(stu1._Student__age)
    print(stu1._Student__get_name())


if __name__ == '__main__':
    main()