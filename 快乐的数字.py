'''
从一个正整数开始，用其每位数的平方之和取代该数，并重复这个过程，
直到最后数字要么收敛等于1且一直等于1，要么将无休止地循环下去且最终不会收敛等于1。
能够最终收敛等于1的数就是快乐的数字。
'''
x = input('请输入这个数:') 
a,m = [x],0 
while True:
    y = 0 
    for i in range(len(str(a[m]))):
        y += (int(a[m]) // (10 ** i) % 10) ** 2 
    if y == 1:
        print(True)
        break 
    if y in a:
        print(False) 
        break 
    a.append(y) 
    m += 1 