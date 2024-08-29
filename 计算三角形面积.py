'''
任意两边之和大于第三边
假设三角形的三边长度分布是a,b,c,构成三角形的条件是:
a+b>c  a+c>b b+c>a 
'''
'''
input函数请用户输入三条边的长度
验证三角形是否成立
海伦公式计算面积
输出结果
'''
a = float(input("输入三角形的第一条边长:")) 
b = float(input("输入三角形的第二条边长:")) 
c = float(input("输入三角形的第三条边长:")) 
if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2 
    s = pow(p * (p - a) * (p - b) * (p - c),0.5) 
    print(f"三角形的面积是{s:0.2f}")
else:
    print("不能构成三角形，请重新输入!")
    