import numpy as np 

def sgd(f,df, x0,learning_rate=0.01,max_iter=1000,tol=1e-6):
    #f 目标函数， df目标函数的梯度   x0初始点    learning_rate 学习率 
    #max_iter  最大迭代次数    tol  容差，当梯度的摸长小于容差时，停止迭代
    x = x0 
    for _ in range(max_iter):
        grad = df(x) 
        if np.linalg.norm(grad) < tol:
            break 
        x = x - learning_rate * grad + np.random.normal(0,0.01,size=x.shape) 
    
    return x 
