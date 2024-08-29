'''
黄金分割数列
1 1 2 3 5 8 13 21 34 55....
第三项开始，每一项都等于前两项之和
'''
#方法1 递归
def fib1(n):
    if n == 1 or n == 2:
        return 1 
    return fib1(n-1) + fib1(n - 2) 

for i in range(1,21):
    print(fib1(i),end=' ')


#方法二  for循环
def fib2(n):
    a,b = 0,1 
    for i in range(n+1):
        a,b = b,a+b 
    return a 
for i in range(20):
    print(fib2(i),end=' ')