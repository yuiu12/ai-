import numpy as np 
import matplotlib.pyplot as plt 


#定义几何分布函数
def geometric_distribution(p,k):
    return (1-p) ** (k-1) * p 

#生成随机数
np.random.seed(0) 
n = 10000  #生成随机数的数量
p = 0.3  #成功的概率
x = np.arange(1,11) #生成1到10的整数数列
y = geometric_distribution(p,x)  

#绘制几何分布图
plt.bar(x,y,width=0.8,color="blue",alpha=0.5)
plt.xlabel('k') 
plt.ylabel('p(X=k)') 
plt.title('Geometric Distribution') 
plt.show()