'''
特殊a串数列求和 给定两个均不超过9的正整数a和n，要求编写程序求a+aa+aaa++⋯+aa⋯a（n个a）之和。
输入说明：输入在一行中给出不超过9的正整数a和n。
输出格式：在一行中按照“s = 对应的和”的格式输出。
输入样例：2 3
输出样例：s = 246
'''

a, n = map(int, input().split())
b = a
x = []
s = 0
for i in range(1, n + 1):
    x.append(a)
    a = a * 10 + b
for i in x:
    s += i

print(f's = {s}')
