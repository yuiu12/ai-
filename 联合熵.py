import numpy as np 

def joint_entropy(p):
    return -np.sum(p * np.log2(p)) 

p = np.array([[0.5,0.5],[0.5,0.5]]) 
print("联合熵为:",joint_entropy(p)) 
