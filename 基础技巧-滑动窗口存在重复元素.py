'''
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。
'''
from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #在此之间填写代码
        a = [] 
        i,j,b = 0,0,len(nums) 
        while i < b:
            if nums[i] in a:return True 
            a.append(nums[i]) 
            i += 1 
            if j == k:
                a.pop(0) 
            else:j += 1 
        return False 

print(Solution().containsNearbyDuplicate([1,2,3,1],3))
print(Solution().containsNearbyDuplicate([1,0,1,1],1))
print(Solution().containsNearbyDuplicate([1,2,3,1,2,3],2))




















































