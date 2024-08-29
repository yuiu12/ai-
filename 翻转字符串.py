#方法1 for循环
a = input("请输入字符串")
b = '' 
for i in a:
    b = i + b 
print(b) 


#反向切片
a = input("请输入字符串:") 
b = a[::-1]
print(b) 

#方法3 反转列表
a = input("请输入字符串:") 
b = list(a) 
#reverse反转元素的排序顺序
b.reverse() 
c = ''.join(b) 
print(c) 


#方法四  递归
a = input("请输入字符串:") 
def f(x):
    if len(x) <= 1:
        return x 
    return f(x[1:]) + x[0] 
print(f(a)) 

#方法五 reduce函数
from functools import reduce 
a = input("请输入字符串:") 
b = reduce(lambda x,y:y + x,a) 
print(b) 
