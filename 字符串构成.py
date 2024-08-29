#一行字符，统计其中英文字母、空格、数学和其他字符的个数
'''
统计数量，需要使用累加
if或while函数 
'''
#方法1 
begin = input("请输入字符串:") 
engnum = spanum = dignum = elnum = 0 
for i in begin:
    if i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z':
        engnum += 1 
    elif i == " ":
        spanum += 1 
    elif i in '0123456789':
        dignum += 1 
    else:
        elnum += 1 
print('在您输入的字符串中，英文字母的个数为{}，空格的个数为{}，数字的个数为{}，其他字符的个数为{}'.format(engnum,spanum,dignum,elnum))

#方法二
begin = input("请输入字符串:") 
engnum = spanum = dignum = elnum = 0 
for i in begin:
    #检测字符串是否由字母组成
    if i.isalpha():
        engnum += 1 
    #检测字符串是否由数字组成
    elif i.isspace():
        spanum += 1 
    #检测字符串是否由空格组成
    elif i.isnumeric():
        dignum += 1 
    else:
        elnum += 1 
print(f'在您输入的字符串中，英文字母的个数为{engnum}，空格的个数为{spanum}，数字的个数为{dignum}，其他字符的个数为{elnum}')
