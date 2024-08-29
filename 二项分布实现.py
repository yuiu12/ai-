import math 
import matplotlib.pyplot as plt 
import numpy as np 
def binomial_distribution(n,p,k):
    #n 试验次数   p  每次试验成功的概率    
    #k 成功次数 
    return math.comb(n, k) *(p ** k) *((1-p)**(n-k)) 

#生成随机数
np.random.seed(0) 
n = 10  #试验次数
p = 0.5  #每次试验成功的概率
x = np.arange(0,n + 1) #生成0到n的整数序列
y = [binomial_distribution(n,p,k) for k in x]

#绘制二项分布图
plt.bar(x,y,width=0.8,color='blue',alpha=0.5)
plt.xlabel('k') 
plt.ylabel('P(X=K)') 
plt.title('Binomial Distribution') 
plt.show()