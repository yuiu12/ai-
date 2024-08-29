'''
每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
要求输入值返回加密值
'''
def encrypt(n):
    digitsSingle = n % 10
    digitsTen = n // 10 % 10
    digitsHundred = n // 100 % 10
    digitsThousands = n // 1000 % 10
    redigitsSingle = (digitsSingle + 5) % 10
    redigitsTen = (digitsTen + 5) % 10
    redigitsHundred = (digitsHundred + 5) % 10
    redigitsThousands = (digitsThousands + 5) % 10
    redigitsThousands, redigitsSingle = redigitsSingle, redigitsThousands
    redigitsHundred, redigitsTen = redigitsTen, redigitsHundred
    return redigitsSingle + redigitsTen * 10 + redigitsHundred * 100 + redigitsThousands * 1000


n = int(input("请输入数字:"))
print(encrypt(n))
