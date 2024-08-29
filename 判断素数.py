'''
素数又称质数，只有1和它本身两个因数的自然数
质数与合数相对立 两个概念  比1大但不是素数的数称为合数   
1和0即非素数也非合数
'''
#方法1  
num = int(input("请输入一个大于1的整数:"))
if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print(f"{num}不是素数")
            break 
    else:
        print(f"{num}是素数")
else:
    print("输入错误，输入大于1的整数")

#方法二
num = int(input("请输入一个大于1的整数:"))
if num > 1:
    for i in range(2,int(num ** 0.5 + 1)):
        if num % i == 0:
            print(f"{num}不是素数")
            break 
    else:
        print(f"{num}是素数")
else:
    print("输入错误，输入大于1的整数")


#方法三
num = int(input("请输入一个大于1的整数:")) 
if num > 1:
    if num == 2:
        print(f"{num}是素数") 
    elif num % 2 == 0:
        print(f"{num}不是素数")
    else:
        for i in range(3,int(num ** 0.5) + 1, 2):
            if num % i == 0:
                print(f"{num}不是素数")
                break 
        else:
            print(f"{num}是素数")
else:
    print("输入错误，输入大于1的整数")