'''
请用户输入带运算的两个数字
请用户选择运算方法
运算结果展示
'''
#方法1.
print("简易计算器")
def add(x,y):
    return x + y 
def subtract(x,y):
    return x - y 
def multiply(x,y):
    return x * y 
def divide(x,y):
    return x / y 
num1 = int(input("请输入第一个数字:"))
num2 = int(input("请输入第二个数字:")) 

print("输入运算:1、相加;2、相减;3、相乘;4、相除")
choice = input("请输入你的选择(1/2/3/4):")
if choice == '1':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "×", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "÷", num2, "=", divide(num1, num2))
else:
    print("非法输入")


#方法二
print("简易计算器")
num1 = int(input("请输入第一个数学:")) 
num2 = int(input("请输入第二个数学:")) 
print("输入运算:1、相加;2、相减;3、相乘;4、相除")
choice = input("请输入你的选择(1/2/3/4)") 

if choice == '1':
    print(num1,"+",num2,"=",num1+num2) 
elif choice == '2':
   print(num1, "-", num2, "=", num1 - num2)
elif choice == '3':
   print(num1, "×", num2, "=", num1 * num2)
elif choice == '4':
    print(num1, "÷", num2, "=", num1 / num2)
else:
   print("非法输入")