import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import expon   

#生成随机数
np.random.seed(0) 
lam = 1 #指数分布的参数 入
x = np.linspace(0,5,1000) 
y = expon.pdf(x,scale=1/lam) 

#绘制指数分布图
plt.plot(x,y,color='blue',alpha=0.5) 
plt.xlabel('X') 
plt.ylabel('P(X)') 
plt.title("Exponential Distribution") 
plt.show() 