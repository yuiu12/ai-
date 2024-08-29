'''
由于因子只能是2，3，5这三个特殊数字，所以可以把这三个数字做成列表进行判断
遍历小于该数的除了1以外的最小因子，判断其是否在2，3，5之间
若不在内部可以直接输出其不是丑数
若是2，3，5之一，则可以使用剩下的数，再次判断其最小因子，直至数变成2，3，5后，可确定其是丑数，循环
'''
a = [2,3,5] 
def UglyNumber(m):
    n = m 
    while True:
        if n == 1:
            return f'{m}是丑数'
            break 
        elif n in a:
            return f'{m}是丑数'
            break
        else:
            b = 0 
            for i in a:
                if n % i != 0:
                    b += 1 
                else:
                    n /= i 
                    continue
            if b == 3:
                return f'{m}不是丑数'
                break 
m = int(input('请输入整数:'))
print(UglyNumber(m))



























