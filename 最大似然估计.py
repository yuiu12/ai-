import numpy as np 
from scipy.stats import norm 

#生成模拟数据
np.random.seed(0) 
data = np.random.normal(loc=5,scale=2,size=100) 

#计算均值和标准差
mean_estimate = np.mean(data) 
std_estimate = np.std(data) 

#使用最大似然估计计算参数
max_likelihood_mean = np.sum((data - mean_estimate) ** 2) / (len(data) * std_estimate ** 2)
max_likelihood_std = np.sqrt(np.sum((data - mean_estimate) ** 2) / len(data)) 

print("最大似然估计的均值:",max_likelihood_mean) 
print("最大似然估计的标准差:",max_likelihood_std) 
