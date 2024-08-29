import numpy as np 

def entropy(p):
    return -np.sum(p * np.log2(p)) 

p = np.array([0.5,0.5]) 
print("熵为:",entropy(p))