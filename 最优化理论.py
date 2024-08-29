import numpy as np 
from scipy.optimize import minimize 

#定义目标函数
def objective_function(params,*args):
    x = args[0] 
    return np.sum((x - params) ** 2) 

#初始化参数
initial_params = np.array([0]) 

#定义数据
x = np.array([1,2,3,4,5]) 

#设置优化问题
result = minimize(objective_function,initial_params,args=(x,)) 

#输出结果
print("最优参数:",result.x)