import numpy as np 
vector1 = np.array([1,2,3]) 
vector2 = np.array([4,5,6]) 
#np.sqrt计算平方根
eud_dist = np.sqrt(np.sum((vector1-vector2)**2)) 
print("欧式距离为",eud_dist) 
#欧式距离为 5.196152422706632
