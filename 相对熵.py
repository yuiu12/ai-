import numpy as np 
def relative_entropy(p,q):
    return np.sum(p * np.log2(p / q)) 

p = np.array([0.5,0.5]) 
q = np.array([0.3,0.7]) 
print("相对熵为:",relative_entropy(p,q)) 