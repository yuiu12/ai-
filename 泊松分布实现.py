import math 
import numpy as np 
import matplotlib.pyplot as plt 

def poisson_distribution(lam, k):
    #计算泊松分布的概率密度函数值
    #lam  平均发生率
    #k   事件发胜次数
    return (math.exp(-lam) * lam ** k) / math.factorial(k)

#生成随机数
np.random.seed(0) 
lam = 5  #平均发生率
x = np.arange(0,11)  #生成0到10的整数序列
y = [poisson_distribution(lam,k) for k in x] 

#绘制泊松分布图
plt.bar(x,y,width=0.8,color='blue',alpha=0.5) 
plt.xlabel('k') 
plt.ylabel('P(X=k)') 
plt.title('Poisson Distribution') 
plt.show() 