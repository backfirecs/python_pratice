"""

某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成

Version:1.0
Author:chaishuai

"""

import abc
class Employee(object, metaclass=abc.ABCMeta):
    __slots__ = ('_salary', '_name')

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @abc.abstractmethod
    def settlement():
        pass

class Manager(Employee):
    __slots__ = ('_salary', '_name')

    def __init__(self, name):
        super().__init__(name)
        self._salary = 15000

    def settlement(self):
        return self._salary

class Developer(Employee):
    __slots__ = ('_salary', '_name', '_man_hour')

    def __init__(self, name, man_hour):
        super().__init__(name)
        self._man_hour = man_hour

    def settlement(self):
        return self._man_hour * 150

class Saleman(Employee):
    __slots__ = ('_salary', '_name', '_sales')

    def __init__(self, name, sales):
        super().__init__(name)
        self._sales = sales

    def settlement(self):
        return 1200 + 0.05 * self._sales

def main():
    manager = Manager('jack')
    print(f'经理 {manager.name} 本月的工资为 {manager.settlement()}')
    developer = Developer('gates', 180)
    print(f'程序员 {developer.name} 本月的工资为 {developer.settlement()}')
    saleman = Saleman('james', 2000000)
    print(f'程序员 {saleman.name} 本月的工资为 {saleman.settlement()}')

if __name__ == '__main__':
    main()