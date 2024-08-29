import numpy as np 
def minkowski_distance(x,y,p):
    return np.sum(np.abs(x - y) ** p) ** (1 / p)
vector1 = np.array([1,2,3]) 
vector2 = np.array([4,5,6]) 
yu = minkowski_distance(vector1,vector2,1)
iu = minkowski_distance(vector1,vector2,2) 
print("曼哈顿距离",yu)
print("欧式距离",iu)
'''
曼哈顿距离 9.0
欧式距离 5.196152422706632
'''