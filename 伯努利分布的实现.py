import numpy as np 
def bernoulli_distribution(p):
    #用于生成二项分布的随机数。
    #1  试验次数；p是每次实验成功的概率
    return np.random.binomial(1,p) 

p = 0.5 
result = bernoulli_distribution(p) 
print("伯努利分布的结果:",result) 