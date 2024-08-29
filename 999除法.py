'''
第一步： 首先输入一个数，input函数
第二步： 判断该数是否为奇数
第三步： 用无限循环，从一个九开始除以刚刚的奇数求余
第四步： 若余不为0则不能整除，增加九的数量
第五步： 注意：5的倍数无法被9的倍数整除，会陷入无限循环
'''
n = int(input('请输入一个奇数:')) 
def b():
    global n 
    if n % 2 == 0:
        n = int(input('你输入的不是奇数，请输入一个奇数:'))
        return b() 
    if n % 5 == 0:
        n = int(input('无解，请重新输入:')) 
        return b() 
    else:
        return c(n) 
def c(n):
    x = 10 
    while True:
        if (x - 1) % n == 0:
            print(f'至少{len(str(x-1))}个9除以{n}的结果为整数')
            break
        else:
            x *= 10 
b() 