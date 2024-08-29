from typing import List
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version,bad):
    if version<bad:return False
    else:return True

class Solution:
    def firstBadVersion(self, n,bad):
        #在此之间填写代码
        left,right = 1,n 
        while left < right:
            m = (left + right) // 2 
            if isBadVersion(m,bad):right=m 
            else:left=m+1 
        return left 

print(Solution().firstBadVersion(5,4))
print(Solution().firstBadVersion(1,1))
