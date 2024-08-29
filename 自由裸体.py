'''
计算单次往返运动距离为落地高度乘以3/2
第十次落地，所以只往返九次加上最后单次落地一次
'''
height = 100 
i = 0 
for _ in range(10):
    i += height * (3 / 2) 
    #每次落地后反跳回原高度的一半
    height /= 2 
print(f'第十次落地时，共经过{i - height}米')
print(f'第十次反弹{height}米高')
