import numpy as np 

def conditional_entropy(p,q):
    return -np.sum(p * np.log2(q / p)) 

p = np.array([0.5,0.5]) 
q = np.array([0.3,0.7]) 
print("条件熵为:",conditional_entropy(p,q)) 
