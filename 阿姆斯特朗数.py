'''
input函数请用户输入查找的区间
for循环遍历这个区间的数值
判断位数，数值拆分，计算每个位数上数学的n次方和
计算出的值与该数值进行比较，相等，为阿姆斯特朗数
'''
#方法1
lower = int(input("请输入最小值:"))
upper = int(input("请输入最大值:")) 

assert lower > 0 and upper > 0 ,"请输入正整数"

for num in range(lower,upper+1):
    sum = 0 
    n = len(str(num)) 
    temp = num 

    while temp > 0:
        digit = temp % 10 
        sum += digit ** n 
        temp //= 10 
    
    if  num == sum: 
        print(num,end=' ')

#方法二
lower = int(input("请输入最小值:")) 
upper = int(input("请输入最大值:")) 

assert lower > 0 and upper > 0,"请输入正整数"

for num in range(lower,upper+1):
    sum = 0 
    n = len(str(num)) 

    for i in str(num):
        sum += int(i) ** n 
    
    if num == sum:
        print(num,end=' ')