'''
第一步： 可以将两者转化为列表类型，通过列表的翻转来判断
第二步： 也可以直接使用字符串的翻转来判断
'''
#方法1 
def Type(num):
    if num > 0:
        num = str(num) 
        list1 = list(num) 
        list2 = list1[:] 
        list2.reverse() 
        if list1 == list2:
            return f'{num}是回文数'
        else:
            return f'{num}不是回文数'
num = int(input('输入一个数:')) 
print(Type(num)) 



#方法二
x = input('请输入任意位数的数字:')
if x == x[::-1]:
    print('%s是个回文数'%x)
else:
    print('%s不是回文数'%x)