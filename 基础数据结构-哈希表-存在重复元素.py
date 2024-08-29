from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #在此之间填写代码
        a = {} 
        for i in nums: 
            a[i] = a.get(i,0) + 1 
            if a[i] == 2:
                return True 
        return False 

print(Solution().containsDuplicate([1,2,3,1]))
print(Solution().containsDuplicate([1,2,3,4]))
print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]))




























































































