'''
range函数遍历100以内的奇数，sum函数求和
for循环嵌套if语句，100以内的奇数相加求和
while循环将100以内的奇数相加，打印求和
递归方法求和
'''
#解法1.sum函数
print(sum(range(1,100,2)))

#解法2 for循环
count = 0 
#for循环遍历1-99的整数
for number in range(100):
    #判断是否是奇数，偶数继续运行
    if number % 2 == 0:
        continue 
    #直到这边有奇数在相加
    count += number 
print(count) 

#方法三 while循环
count = 0 
number = 1 
#这里就是number在1-99范围内
while number < 100:
    #count每次加一
    count += number 
    #然后count变成1，number+2=3  count=3  
    number += 2 
print(count) 

#方法四 递归求和
def sum(x):
    if x > 99:
        return 0 
    else:
        count = sum(x + 2) 
        return x + count 
print(sum(1))


