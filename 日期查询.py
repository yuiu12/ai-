'''
输入某年某月某日，判断这个日期是这一年的低多少天
'''
#方法1
print("请输入年月日，判断这个日期是这一年的第多少天")
year = int(input("请输入年份:"))
month = int(input("请输入月份:")) 
day = int(input("请输入日期:")) 
months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
if 1 <= month <= 12:
    sum = months[month - 1] 
    sum += day 

    leap = 0 
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        leap = 1 
    days = [31, 28 + leap, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day > days[month - 1]:
        print("输入的日期错误")
    
    else:
        if month > 2 and leap == 1:
            sum += 1 
        
        print(f"这是这一年的第{sum}天")
else:
    print("输入的月份错误")

#方法二
print("请输入年月日,判断这个日期是这一年的第多少天")
year = int(input("请输入年份:")) 
month = int(input("请输入月份"))
day = int(input("请输入日期:")) 

import datetime 

date1 = datetime.date(year,month,day) 
date2 = datetime.date(year-1,12,31) 
timedelta = (date1 - date2).days 

print(f"这是这一年的第{timedelta}天")
