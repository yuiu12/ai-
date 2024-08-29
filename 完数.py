'''
求某一范围内的所有完数。
或者输入一个数，判断其是不是完数。
如果一个数等于它的因子之和，则称该数为“完数”（或“完全数”)。例如，6的因子为1、2、3，而 6=1+2+3，因此6是“完数”。
'''
#判断完数
pnum = int(input("请输入一个数:")) 
cum = 0 
for i in range(1,pnum):
    if pnum % i == 0:
        cum += i 
if pnum == cum:
    print(f"{pnum}是完数")
else:
    print(f"{pnum}不是完数")

#输出完数
pnum = [] 
for i in range(1,1001):
    cum = 0 
    for j in range(1,i):
        if i % j == 0:
            cum += j 
    if i == cum:
        pnum.append(str(i))
print('1000以内的完数有这些:',','.join(pnum))














