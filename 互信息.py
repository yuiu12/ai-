import numpy as np 
from scipy.stats import entropy 

def mutual_information(p,q):
    return entropy(p) + entropy(q) - entropy(np.outer(p,q)) 

p = np.array([0.5,0.5]) 
q = np.array([0.3,0.7]) 

print("互信息为:",mutual_information(p,q)) 
