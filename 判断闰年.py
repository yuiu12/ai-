#闰年共有366天
'''
普通闰年和世纪闰年
普通闰年  公历年份是4的倍数，不是100的倍数，为闰年
世纪闰年 公历年份是整百数的，必须是400的倍数才是闰年
'''
#方法1 
year = int(input("请输入一个年份:"))
if year % 4 == 0:
    if year % 100 == 0:
        #这一段是单独的就是被400整除的就是世纪闰年
        if year % 400 == 0:
            print(f"{year}年是世纪闰年")
        else:
            print(f"{year}年不是闰年")
    #能被4整除不是100的倍数的普通闰年
    else:
        print(f"{year}年是普通闰年")
else:
    print(f"{year}年不是闰年") 

#方法2
year = int(input("请输入一个年份"))
if year % 4 == 0 and year % 100 != 0:
    print(f"{year}年是普通闰年")
elif year % 400 == 0:
    print(f"{year}年是世纪闰年")
else:
    print(f"{year}年不是闰年")

#方法3 
year = int(input("请输入一个年份"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year}年是闰年")
else:
    print(f"{year}年不是闰年")

