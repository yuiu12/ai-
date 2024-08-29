import numpy as np 
vector1 = np.array([1,2,3]) 
vector2 = np.array([4,5,6])
#np.dot点积
'''
点积，又被称为内积或数量积，是向量运算中的一种重要操作。
通俗来说，它是两个向量进行"相乘"后得到的标量值。
这个过程实际上是将两个向量的对应分量相乘，并将乘积累加得到。
'''
#np.linalg.norm向量或矩阵的范数。
#元素平方和然后开根号。
cos_sim = np.dot(vector1,vector2) / (np.linalg.norm(vector1)*np.linalg.norm(vector2)) 
print("余炫相似度为",cos_sim)
#余炫相似度为 0.9746318461970762