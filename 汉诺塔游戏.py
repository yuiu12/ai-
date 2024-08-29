num  = int(input('请输入A盘上的圆盘个数:')) 
n = 0 
def process(A,B,C,num):
    #global引入全局变量n
    global n 
    if num == 1:
        print(A,'到',C) 
        n += 1 
    else:
        #先num-1代表移动上面的num-1层
        num = num - 1 
        #将上面num从A移到B
        process(A,C,B,num) 
        print(A,'到',C) 
        n += 1 
        process(B,A,C,num) 
process('A','B','C',num) 
print(f'最小{n}步完成')
