from typing import List
class Solution:
    def myPow(self, x: float, n: int) -> float:
        #在此之间填写代码
        def quickMul(N):
            if N == 0:
                return 1.0 
            #变量y为N除以二的整数部分的递归结果
            y = quickMul(N // 2) 
            #N整除2，返回yy，否则返回yy*x
            return y * y if N % 2 == 0 else y * y * x 
        #n>=0 
        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n) 

print(Solution().myPow(2.0,10))
print(Solution().myPow(2.1,3))
print(Solution().myPow(2.0,-2))






















































