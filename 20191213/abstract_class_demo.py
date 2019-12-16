"""

抽象类的简单使用

Version:1.0
Author:chaishuai

"""

import abc 

class Pet(object, metaclass=abc.ABCMeta):
    def __init__(self, nickname):
        self._nickname = nickname
    
    @abc.abstractmethod
    def make_voice(self):
        pass

class Dog(Pet):
    def make_voice(self):
        print(f'{self._nickname}:汪..汪..')

def main():
    dog = Dog('宝马')
    dog.make_voice()

if __name__ == '__main__':
    main()