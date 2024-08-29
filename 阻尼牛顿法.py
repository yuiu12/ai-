import numpy as np

def damped_newton_method(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if np.linalg.norm(dfx) < tol:
            print("梯度接近为零，提前终止")
            return x

        dx = -fx / dfx
        x = x + dx
        print("第{}次迭代，解为：{}".format(i + 1, x))
    print("达到最大迭代次数，未收敛")
    return x

# 示例：求解方程组 x^2 - 4x + 4 = 0 和 x^2 - 2x + 1 = 0
def f1(x):
    return x ** 2 - 4 * x + 4

def df1(x):
    return 2 * x - 4

def f2(x):
    return x ** 2 - 2 * x + 1

def df2(x):
    return 2 * x - 2

x0 = np.array([1, 1])
tol = 1e-6
max_iter = 100
x1 = damped_newton_method(f1, df1, x0, tol, max_iter)
x2 = damped_newton_method(f2, df2, x0, tol, max_iter)
print("方程组的解为：", x1, x2)
