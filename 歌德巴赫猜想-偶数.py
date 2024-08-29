#将6-99之间的偶数都表示成两个素数之和，输出时每行输出5组。
'''
输出时每行输出5组，可以记录输出次数后换行输出
遍历6-99中的所有数，for循环
判断是否是素数的方法已经出现过很多次了
'''
a = [2] 
for i in range(3,100):
    b = 0 
    for j in range(2,i):
        if i % j != 0:
            b += 1 
            if b == i - 2:
                a.append(i) 
m = 0 
for i in range(6,99):
    if i % 2 == 0:
        for j in range(2,i):
            if j in a:
                if i - j in a:
                    m += 1 
                    if m == 5:
                        print(f'{i}={j}+{i - j}')
                        m = 0 
                    else:
                        print(f'{i}={j} + {i - j}',end=' ')
                    break 
                