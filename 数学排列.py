#嵌套for循环使填在百位、十位、个位的数学都是1，2，3，4
#组成所有的排列后再去掉不满足条件的排列

#方法1 
total = 0 
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i != j and j != k and i != k:
                print(str(i)+str(j)+str(k),end=' ') 
                total += 1 
print(f"\n共有{total}个数")

#方法2
from itertools import permutations 
'''
permutations(item [,r])
item为排序的对象
r为长度参数，用于指定长度的排列中​

'''
total = 0 
for i in permutations('1234',3):
    print(''.join(i),end=' ')
    total += 1 
print(f"\n共有{total}个数")
