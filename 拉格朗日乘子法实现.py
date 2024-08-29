import numpy as np 

def primal_dual_method(A,b,c):
    m, n = A.shape 
    x = np.zeros(n) 
    y = np.zeros(m) 
    z = c - A.T @ y 
    L = np.eye(m) 
    u = np.zeros(m) 
    while True:
        i = np.argmin(z) 
        if z[i] >= 0:
            break 
        x_bar = np.linalg.solve(A[i],b[i]) 
        alpha = (b[i] - A[i] @ x_bar) / (A[i] @ x_bar - A[i] @ x + c)
        x += alpha * x_bar 
        z += alpha * (c - A.T @ y) 
        y += alpha * (A @ x - b) 
        L[i] = np.eye(m) - alpha * A[i] 
        u += alpha * (A[i] @ x - b[i]) 
    return x,u,L 
#测试数据
A = np.array([[1,2],[3,4]]) 
b = np.array([5,6]) 
c = np.array([7,8]) 
x, u, L = primal_dual_method(A, b, c) 
print("最优解:",x) 
print("对偶变量:", u) 
print("拉格朗日乘子矩阵:",L) 