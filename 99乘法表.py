'''
因数从1到9逐个循环，使用循环结构
分行与列考虑，共9行9列，嵌套循环
变量1-9的数学序列，使用range函数
使用format将字符串格式化，数据按照几成几等于几的固定格式显示
'''
for i in range(1,10):
    for j in range(1,i+1):
        print('{}x{}={}\t'.format(j,i,i*j),end=' ')
    print()
'''
for循环遍历1-9整数，i赋值
第一个for语句嵌套一个for语句，i只加一就是1*1，1*(1+1),1*(1+2)
print打印结果，format方法格式化字符串;\t是tab键
print函数换行输出，继续下一次循环，输出九九乘法表
'''
'''
range创建一个整数列表
range(start,stop,[step]) 
format格式化字符串的一种方法

'''
