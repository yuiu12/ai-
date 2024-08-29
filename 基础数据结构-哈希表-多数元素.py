from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #在此之间填写代码
        a = {} 
        for i in nums:
            a[i] = a.get(i,0) + 1 
            if a[i] > len(nums) // 2:
                return i 

print(Solution().majorityElement([3,2,3]))
print(Solution().majorityElement([2,2,1,1,1,2,2]))






















































































