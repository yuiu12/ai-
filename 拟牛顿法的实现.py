import numpy as np    
def f(x):
    return x**2-4*x+4 
def df(x):
    return 2*x-4 
def newton_method(x0,tol=1e-6,max_iter=100):
    x = x0 
    for i in range(max_iter):
        fx = f(x) 
        dfx = df(x)
        if np.abs(dfx) < tol:
            dfx += tol 
        x_new = x - fx / dfx 
        if np.abs(x_new - x) < tol:
            return x_new 
        x = x_new 
    return None 
x0=2.0 
result = newton_method(x0) 
print("牛顿法求解结果:",result)