'''
写一个程序，输出从 1 到 n 数字的字符串表示。

如果 n 是3的倍数，输出“Fizz”；

如果 n 是5的倍数，输出“Buzz”；

如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
'''
from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        #在此之间填写代码
        i = 1 
        a = [] 
        while i <= n:
            if i % 3==0 and i % 5==0:a.append('FizzBuzz')
            elif i % 3 == 0:a.append('Fizz') 
            elif i % 5 == 0:a.append('Buzz') 
            else:a.append(str(i)) 
            i += 1 
        return a 

print(Solution().fizzBuzz(15))
print(Solution().fizzBuzz(5))





























































