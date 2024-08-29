import numpy as np  

def gradient_descent(f,df,x0,epsilon=1e-6,max_iter=1000):
    x = x0 
    for k in range(max_iter):
        grad = df(x) 
        if np.linalg.norm(grad) <= epsilon:
            return x 
        alpha = 0.1 
        x = x - alpha * grad 
    return x 
