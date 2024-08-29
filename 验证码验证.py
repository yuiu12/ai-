'''
用户登录网站经常需要输入验证码，验证码包含大小写字母和数字，随机出现。用户输入验证码时不区分大小写，只要各字符出现顺序正确即可通过验证。 　　
请写一个程序完成验证码的匹配验证，随机生成四位数的验证码如Qs2X（生成数字概率为1/5，大写字母和小写字母概率各为2/5）　
如果用户输入验证码正确，输出“验证码正确”，输入错误时输出“验证码错误，请重新输入”，再重新生成验证码让用户输入，输入五次错误时输出“您已用光了验证机会”。
'''
import random 
n = 0 
def verify2():
    a = [] 
    for _ in range(4):
        x = random.random() 
        if x <= 0.4:
           a.append(random.choice(
                ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'L', 'K', 'J', 'H', 'G', 'F', 'D', 'S', 'A', 'Z',
                 'X', 'C', 'V', 'B', 'N', 'M']))
        elif x <= 0.8:
             a.append(random.choice(
                ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'l', 'k', 'j', 'h', 'g', 'f', 'd', 's', 'a', 'z',
                 'x', 'c', 'v', 'b', 'n', 'm']))
        else:
            a.append(random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']))
    return str(''.join(a)) 
def code():
    global n 
    a = verify2() 
    verify = input(f'请输入验证码{a}')
    if verify.lower() == a.lower():
        print('验证码正确') 
    else:
        n += 1 
        if n == 5:
            print('你一用光了验明证机会')
        else:
            print('验证码错误，请重新输入')
            code() 
code()