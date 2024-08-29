import numpy as np 
from scipy.optimize import minimize 

#定义一个凸函数
def f(x):
    return x ** 2 

#随机生成一组点
points = np.random.rand(100,1) 

#计算每个点的函数值
values = f(points)

#使用scipy库中的minimize函数来最小化函数
result = minimize(f,x0=0) 

#如果最小化后的函数值与原函数值相等，该函数为凸函数
if result.fun == f(result.x):
    print("该函数为凸函数")
else:
    print("该函数不是凸函数")



