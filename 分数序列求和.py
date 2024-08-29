#2/1  3/2  5/3   8/5  13/8   21/13
#方法1 递归法
def f(x):
    if x == 1 or x == 2:
        return x 
    return f(x - 1) + f(x - 2) 
sum1 = 0 
for i in range(1,21):
    sum1 += f(i + 1) / f(i) 
print(round(sum1,2))

#方法二 for循环
a = 2 
b = 1 
sum1 = 0 
for i in range(20):
    sum1 += a / b 
    b, a = a, a+b 
print(round(sum1,2)) 

