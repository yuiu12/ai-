import numpy as np 
vector1 = np.array([1,2,3]) 
vector2 = np.array([4,5,6]) 
cb_dist = np.max(np.abs(vector1-vector2)) 
print("切比雪夫距离为",cb_dist)
#切比雪夫距离为 3