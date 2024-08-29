'''
input函数使用用户输入头的个数和脚的个数
判断鸡和兔子的数量，需要把握住关键条件"鸡+兔=头数；2鸡+4兔=脚数"
'''
head  = int(input("请输入头数:")) 
foot = int(input("请输入脚数:")) 

x = 0 #鸡
y = 0 #兔子
answer = False 

for x in range(head + 1):
    for y in range(head+1):
        if x + y == head and 2*x+4*y==foot:
            answer=True 
            break 
    if answer:
        break 

if answer:
    print("鸡有",x,"只;兔子有",y,"只")
else:
    print("此题无解，请重新输入")
    