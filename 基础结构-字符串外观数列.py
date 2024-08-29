from typing import List
class Solution:
    def countAndSay(self, n: int) -> str:
        #在此之间填写代码
        if n==1:return '1' 
        x,y = 0,''
        a = self.countAndSay(n-1) 
        while x < len(a):
            m = 1 
            while x + 1 < len(a) and a[x] == a[x+1]:
                m += 1 
                x += 1 
            y = y+str(m*10+int(a[x])) 
            x += 1 
        return y 

print(Solution().countAndSay(1))
print(Solution().countAndSay(4))
print(Solution().countAndSay(8))










































































