'''
计算机随机生成一个100以内的正整数
用户通过键盘输入数字，猜测计算机所生成的随机数
限定用户的输入次数
'''
'''
随机生成整数，引入生成随机数的模块random
定义函数，设置计算机生成数的范围及用户输入数学的次数
input获取用户输入的数学，if语句判断大小
'''
print("这是一个猜数字游戏，你可以输入1到100之间的数字，但只有5次机会")
from random import randint 
def guess(start,end,maxTime):
    value = randint(start,end) 

    for i in range(maxTime):
        prompt = '开始猜吧,请输入一个整数:' if i == 0 else '再猜一次:'

        try:
            guessNum = int(input(prompt)) 
            if guessNum == value:
                print("恭喜你,猜对啦!") 
                break 
            elif guessNum > value:
                print("你猜的太大了!")
            else:
                print("你猜的太小了!") 
        except:
            print("请输入整数")
    else:
        print("很遗憾，游戏结束") 
        print("正确答案是:",value,"继续努力吧~") 
guess(1,100,5) 