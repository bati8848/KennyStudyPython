import random

resultList = [0,0,0]


def checkQuit(input):
    if str(input) == 'Q':
        return True
    else:
        return False

def tryThrow():
    a = random.randrange(1,7)
    b = random.randrange(1,7)
    c = random.randrange(1,7)

    resultList[0] = a
    resultList[1] = b
    resultList[2] = c

    result = a+b+c

    if result <= 10:
        return 'SMALL'
    else:
        return 'BIG'



Cash_Left = int(10000)


while (Cash_Left >= 1):
    print('\n\n新一局游戏开始！你现在拥有人民币 '+str(Cash_Left)+' 元')

    # 输入猜的大小，并判断玩家是否想退出
    bigOrSmall = input('请输入 BIG 或者 SMALL。 你也可以输入 \'Q\' 来结束游戏！\n')
    if checkQuit(bigOrSmall) == True:
        print("游戏结束，下次再见啦！")
        break

    # 输入猜的金额，并判断玩家是否想退出
    betAmount = input('请输入你想押注多少钱？ 你也可以输入 \'Q\' 来结束游戏！\n')
    if checkQuit(betAmount) == True:
        print("游戏结束，下次再见啦！")
        break

    # 输入猜的倍数，并判断玩家是否想退出
    times = input('你想赌几倍？你也可以输入 \'Q\' 来结束游戏！\n')
    if checkQuit(times) == True:
        print("游戏结束，下次再见啦！")
        break

    #检查余额合法性
    if float(Cash_Left) < float(betAmount) * float(times):
        print("\n***** 你的余额不足，请重新输入金额和倍率，以开始游戏。 *****")
        continue


    if tryThrow() == bigOrSmall:
        changeAmount = float(betAmount) * float(times)
        print('本次三个骰子的结果是：  ', end='')
        print(resultList)
        print("恭喜你！你赢了！你本次总共赢了 "+str(changeAmount)+' 元')
        Cash_Left = Cash_Left + changeAmount

    else:
        changeAmount = -(float(betAmount) * float(times))
        print('本次三个骰子的结果是：  ', end='')
        print(resultList)
        print("很遗憾！你输了！你本次总共输了 "+str(abs(changeAmount))+' 元')
        Cash_Left = Cash_Left + changeAmount

    print(2*'\n')

if (Cash_Left == 0):
    print('你的钱输光了，游戏结束！')



