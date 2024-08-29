import numpy as np 

def cross_entropy(p,q):
    return -np.sum(p * np.log2(q)) 

p = np.array([0.5,0.5]) 
q = np.array([0.3,0.7]) 
print("交叉熵为:",cross_entropy(p,q)) 
