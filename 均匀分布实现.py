import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import uniform 

#生成随机数
np.random.seed(0) 
a = -1  #区间左端点
b = 1 #区间右端点
x = np.linspace(a,b,1000) #生成-1到1之间的1000个点
y = uniform.pdf(x,a,b-a)  

#绘制均匀分布图
plt.plot(x,y,color='blue',alpha=0.5) 
plt.xlabel('X') 
plt.ylabel('P(X)') 
plt.title('Uniform Distribution') 
plt.show() 
