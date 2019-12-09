"""
CRAPS赌博游戏
CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
玩家第一次如果摇出2点、3点或12点，庄家胜；
其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；
其他点数，玩家继续摇骰子，直到分出胜负
假设赌注1000美金

Version:1.0
Author:chaishuai

"""
import random

money = 1000
while True:
    round = 0
    first_num = 0
    if money == 0:
        print('你没有赌注了，已经是彻底的输家，再见')
        break
    else:
        pot = int(input("手中赌注%d,请下注:" % money))
    while True:
        if pot > money:
            print('你没有那么多赌注')
            break
        else:
            round += 1
            num = random.randint(2, 12)
            if round == 1:
                first_num = num
                if num == 7 or num == 11:
                    money += pot
                    print('这轮摇出的骰子为%d，你赢了，老铁，下一轮走起' % num)
                    break
                elif num == 2 or num == 3 or num == 12: 
                    money -= pot
                    print('这轮摇出的骰子为%d，你输了，老铁，下一轮走起' % num)
                    break
                else:
                   print('这轮摇出的骰子为%d，未分胜负，下一轮走起' % num)
            elif num == 7:
                money -= pot
                print('这轮摇出的骰子为%d，你输了，老铁，按回车开始下一轮' % num)
                break
            elif num == first_num:
                money += pot
                print('这轮摇出的骰子为%d，你赢了，老铁，下一轮走起' % num)  
                break
            else:
                print('这轮摇出的骰子为%d，未分胜负，下一轮走起' % num)
