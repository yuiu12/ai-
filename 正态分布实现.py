import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import norm 

#生成随机数
np.random.seed(0) 
mu = 0 #均值
sigma = 1 #标准差
x = np.linspace(-5,5,1000) #生成-5到5之间的1000个点
#计算正态分布的概率密度函数值
y = norm.pdf(x,mu,sigma)  

#绘制正态分布图
plt.plot(x,y,color='blue',alpha=0.5) 
plt.xlabel('X') 
plt.ylabel('P(X)') 
plt.title('Normal Distribution') 
plt.show() 
