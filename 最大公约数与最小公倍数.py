'''
最大公约数  存在数x，满足a和b均可以整除x  x为a和b的公约数，x最大时，为最大公约数
最小公倍数   存在数y，满足a和b均可以被y整除，y为a和b的公倍数，y最小是，为最小公倍数
'''
'''
能同时被两个数整除的最大整数，同时被两个数整除，这个数必然小于等于两个数中的较小者
找出两个数中的较小数
较小数开始遍历到1 
遍历过程中最先能同时被两个数整除的就是最大公约数

能同时将两个数整除的最小整数，必然大于等于两个数中的较大者
找出两个数中的较大者
较大数开始递增遍历
遍历过程中最先能同时将两个数整除的就是最小公倍数
'''
num1 = int(input("请输入一个整数:")) 
num2 = int(input("请输入另一个整数:")) 

assert num1 > 0 and num2 > 0,"请输入正整数!"

min_num = min(num1,num2)  #最大公因数
max_num = max(num1,num2) #最小公倍数

for i in range(min_num, 0, -1):
    if num1 % i == 0 and num2 % i == 0:
        break 
print(f"{num1}和{num2}的最大公约数是{i}") 

while True:
    if max_num % num1 == 0 and max_num % num2 == 0:
        break 

    max_num += 1 
print(f"{num1}和{num2}的最小公倍数是{max_num}")