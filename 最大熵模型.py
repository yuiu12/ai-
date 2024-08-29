import numpy as np
from scipy.optimize import minimize

# 定义目标函数（负对数似然）
def negative_log_likelihood(params, *args):
    p = params
    x = args[0]
    return -np.sum(x * np.log(p) + (1 - x) * np.log(1 - p))

# 定义约束条件（概率之和为1）
def constraint(params):
    return np.sum(params) - 1

# 初始化参数
initial_params = np.array([0.5, 0.5])

# 定义数据
x = np.array([0, 1, 0, 1, 1, 0, 1, 0, 0, 1])

# 设置优化问题
result = minimize(negative_log_likelihood, initial_params, args=(x,), constraints={'type': 'eq', 'fun': constraint})

# 输出结果
print("最优参数：", result.x)
