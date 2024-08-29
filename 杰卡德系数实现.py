import numpy as np
def jaccard_distance(A,B):
    #用于计算两个布尔数组的逻辑与操作。
    intersection = np.logical_and(A,B) 
    #用于计算两个布尔数组的逻辑或操作。
    union = np.logical_or(A,B) 
    return 1 - np.sum(intersection) / np.sum(union) 
a=np.array([1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0])
b=np.array([1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1])
result = jaccard_distance(a,b) 
print("Jacard距离:",result)
#Jacard距离: 0.4117647058823529