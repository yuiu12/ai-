'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
'''
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        #在此之间填写代码
        slow,fast = 0,0 
        a,b = len(nums),[] 
        while fast < a:
            if nums[fast] != 0:
                b.insert(slow,nums[fast]) 
                slow += 1 
            else:
                b.append(0) 
            fast += 1
        return b 

print(Solution().moveZeroes([0,1,0,3,12]))
print(Solution().moveZeroes([0]))










































