'''
杨辉三角的性质：

每行首尾的数字都是1
每行中间的各数都是它肩上两个数的和
第n行的数字有n项
第n行的项数总比n-1行多1个
'''
'''
input函数使用户输入行数
创建两个列表，一个用于输出最后的结果，另一个输出每一行的数字，添加到第一个列表
每行首尾的数学都是1；每行中间的个数都是它肩上两个数的和
'''
n = int(input("输入需要打印的杨辉三角行数:")) 
assert n > 0,"请输入正整数!"
#完成整个序列的循环
list1 = [] 
for i in range(n):
    #存储每一行的数值
    list2 = [] 
    if i == 0:
        list2 = [1] 
    elif i == 1:
        list2 = [1,1] 
    else:
        for j in range(i+1):
            #每行首尾的数字都是1，输出每行首尾的数字 1，添加到列表list2
            if j == 0 or j == i:
                list2.append(1) 
            else:
                #每行中间的各数都是它肩上两个数的和，通过对双重列表的索引，获取中间这个数肩上的两个数，求和后将其添加到列表list2
                list2.append(list1[i - 1][j - 1] + list1[i - 1][j]) 
    list1.append(list2) 
#杨辉三角每一行的数值居中排列，设置每一行第一个数值前的空格数，len函数获取list1最后一行的长度
space = len(list1[-1]) 
#list1是二维列表，for循环遍历list1，循环变量i位一维列表
for i in list1:
    #每个数值之间间隔4个空格，每一行第一个元素的空格位space*4 //2 
    print(' ' * (space * 4 // 2),end='') 
    for j in i:
        #每个数值之间间隔4个空格
        print(f"{j:<4}",end='')
    print() 
    #由于第n行的数值比n-1行多1个，space在原有的基础上减1 
    space -= 1 