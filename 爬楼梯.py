'''
从整体看，可能一时不知道该如何完成
当爬到n阶时，可以是从n-1爬上来，也可以是n-2爬上来
当只有一阶时，只有一种爬法
当n=2时，有两种爬法
其他情况下，n阶时，由于只有两者爬上来的可能性，所以只需计算n-1阶爬法以及n-2阶爬法即可，递归
'''
def Climb(n):
    if n == 1:
        return 1 
    elif n == 2:
        return 2 
    else:
        return Climb(n-1) + Climb(n-2) 
n = int(input('请输入楼层'))
print(f'一共有{Climb(n)}种爬法')