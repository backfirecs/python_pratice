"""

奥特曼小游戏

Version:1.0
Author:chaishuai

"""

import abc
import random
import time

class Fighter(object, metaclass=abc.ABCMeta):
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp

    @abc.abstractmethod
    def attack(self, other):
        pass

    def is_alive(self):
        return True if self._hp > 0 else False

class Ultraman(Fighter):
    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

    @property
    def mp(self):
        return self._mp

    @mp.setter
    def mp(self, mp):
        self._mp = mp
    
    def attack(self, num, other):
        if num < 7:
            self.normal_attack(other)
        elif num < 10:
            self.magic_attack(other)
        else:
            self.unique_skill_attack(other)

    def normal_attack(self, other):
        other.hp -= 10
        other.hp = 0 if other.hp < 0 else other.hp
        print(f'{self.name} 攻击了 {other.name} 造成了10点伤害')

    def magic_attack(self, other):
        if self._mp < 5:
            print(f'{self.name} 想使用 魔法 攻击，但是没有足够的魔法，只能使用普通攻击了')
            self.normal_attack(other)
            return False
        print(f'{self.name} 使用 魔法 攻击了 {other.name} 造成了25点伤害, 花费了5点魔法')
        self._mp -= 5
        other.hp -= 25
        other.hp = 0 if other.hp < 0 else other.hp
        return True

    def unique_skill_attack(self, other):
        if self._mp < 25:
            self.normal_attack(other)
            print(f'{self.name} 想使用 必杀技 攻击，但是没有足够的魔法，只能使用普通攻击了')
            return False
        print(f'{self.name} 使用 必杀技 攻击了 {other.name} 造成了50点伤害, 花费了2点魔法')
        self._mp -= 30
        other.hp -= 50
        other.hp = 0 if other.hp < 0 else other.hp
        return True

class Monster(Fighter):
    __slots__ = ('_name', '_hp')

    def __intit__(self, name, hp):
        super().__init__(name, hp)

    def attack(self, other, num):
        other.hp -= num
        other.hp = 0 if other.hp < 0 else other.hp
        print(f'{self.name} 攻击了 {other.name} 造成了10点伤害')
        return True

def find_alive_monsters(monsters):
    alive_monster_list = []
    for monster in monsters:
        if monster.is_alive():
            alive_monster_list.append(monster)
    return alive_monster_list

def show_status(ultraman, monsters):
    print('当前状态')
    print(f'{ultraman.name} hp:{ultraman.hp} mp:{ultraman.mp}')
    for monster in monsters:
        print(f'{monster.name} hp:{monster.hp}')

def main():
    ultraman = Ultraman('Chace', 100, 100)
    monster1 = Monster('哥斯拉', 100)
    monster2 = Monster('小丑', 100)
    monster3 = Monster('灭霸', 100)
    monsters = [monster1, monster2, monster3]
    round = 0
    isGameGoOn = True
    while isGameGoOn:
        round +=1
        print(f'=================第{round}回合==================')
        show_status(ultraman, monsters)
        alive_monsters = find_alive_monsters(monsters)
        for alive_monster in alive_monsters:
            num = random.randint(1, 10)
            print(f'{ultraman.name} 摇出了 {num}')
            ultraman.attack(num, alive_monster)
            if alive_monster.is_alive():
                alive_monster.attack(ultraman, num + 1)
                if ultraman.is_alive() == False:
                    print(f'{ultraman.name} 死了，英雄陨落，世间再无光明')
                    isGameGoOn = False
                    break
            else:
                print(f'{alive_monster.name} 被当场击毙')
        show_status(ultraman, monsters)
        if len(find_alive_monsters(monsters)) == 0:
            print(f'怪兽全部死亡，圣光重新照亮人间')
            isGameGoOn = False
        else:
            time.sleep(2)


if __name__ == '__main__':
    main()