max = int(input("请输入行数:")) 
x = [' '] * (2*max-1) 
for i in range(max):
    x[max-1-i] = str(i + 1) 
    x[max-1+i] = str(i + 1) 
    print(''.join(x)) 
    






























































