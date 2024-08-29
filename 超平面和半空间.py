import numpy as np 

#定义超平面的法向量和截距
normal_vector = np.array([1,2,3]) 
intercept = -5 

#定义半空间的法向量和截距
halfspace_normal_vector = np.array([1,-1,0]) 
halfspace_intercept = 0 

#计算超平面和半空间的方程
hyperplane_equation = f"{normal_vector[0]}x + {normal_vector[1]}y + {normal_vector[2]}z + {intercept} = 0"
halfspace_equation = f"{halfspace_normal_vector[0]}x + {halfspace_normal_vector[1]}y + {halfspace_normal_vector[2]}z + {halfspace_intercept} >= 0" 

print("超平面方程:",hyperplane_equation) 
print("半空间方程:",halfspace_equation) 
