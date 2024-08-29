'''
有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，
问最后留下的是原来第几号的那位。
要求：输入围成一圈的人数n
输出最后一个人的编号
'''
n = int(input('请输入围成一圈的人数：'))
a = []
for i in range(n):
    a.append(i + 1)


def count(a):
    i = 2
    while True:
        if len(a) == 2:
            if i == 1:
                return a[0]
            else:
                return a[1]
        a[i] = 0
        i += 3
        if i >= len(a):
            i -= len(a)
            while True:
                try:
                    a.remove(0)
                except:
                    break


print(count(a))
