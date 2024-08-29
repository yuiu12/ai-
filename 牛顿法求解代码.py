#求解非线性方程 x**3 - x**2 + 2 = 0
import numpy as np   
def f(x):
    return x**3 - x ** 2 + 2 

def df(x):
    return 3 * x ** 2 - 2 * x 

def newton_method(f,df,x0,tol=1e-6,max_iter=100):
    x = x0 
    for i in range(max_iter):
        grad = df(x) 
        if abs(grad) < tol:
            break 
        x = x - grad / df(x) 
    return x 
root = newton_method(f,df,x0=0.5) 
print("Root of equation:",root)
