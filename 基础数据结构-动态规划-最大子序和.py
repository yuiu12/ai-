from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #在此之间填写代码
        a,i = nums[0],1 
        while i < len(nums):
            nums[i] = max(nums[i-1] + nums[i], nums[i]) 
            if nums[i]>a:
                a = nums[i] 
            i += 1 
        return a 


print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(Solution().maxSubArray([1]))
print(Solution().maxSubArray([0,2,3,-3,4,-5,6,-2,8,-4,5,-3,3,3,2,-5,4,-3,3]))
print(Solution().maxSubArray([-1]))
print(Solution().maxSubArray([-100000]))













































































