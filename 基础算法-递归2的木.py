'''
给
你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。
如果存在一个整数 x 使得 n == 2x ，则认为 n 是 2 的幂次方
'''
from typing import List
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #在此之间填写代码
        if n==0:return False
        if n==1:return True
        return n%2==0 and self.isPowerOfTwo(n/2)

print(Solution().isPowerOfTwo(1))
print(Solution().isPowerOfTwo(16))
print(Solution().isPowerOfTwo(3))
print(Solution().isPowerOfTwo(4))
print(Solution().isPowerOfTwo(5))





















































