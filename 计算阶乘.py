'''
一个正整数的阶乘是所有小于及等于该数的正整数的积
'''
#方法1 for循环
a = int(input("请输入一个自然数:")) 
result = 1 
if a < 0:
    print("复述没有阶乘")
elif a == 0:
    print("0的阶乘为1")
else:
    for i in range(1,a+1):
        result *= i 
    print(f"{a}的阶乘为{result}")

#方法二 递归法
def factorial(n):
    assert n >= 0,"请输入自然数"
    if n == 0:
        return 1 
    return n * factorial(n-1) 
a = int(input("请输入一个自然数:")) 
print(factorial(a))

#方法三  reduce函数
from functools import reduce 

def factorial(n):
    assert n >= 0,"请输入自然数"
    if n == 0:
        return 1 
    return reduce(lambda x,y:x *y,range(1,n+1))
a = int(input("请输入一个自然数:"))
print(factorial(a)) 

#方法四 factorial函数
import math  
a = int(input("请输入一个自然数:")) 
result = math.factorial(a) 
print(f"{a}的阶乘为{result}") 