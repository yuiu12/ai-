from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        #在此之间填写代码
        a = len(nums) 
        i = 2 
        if a == 1:return nums[0] 
        nums[1]=max(nums[0],nums[1]) 
        while i < a:
            nums[i] = max(nums[i-1],nums[i-2]+nums[i]) 
            i += 1 
        return max(nums[-1],nums[-2]) 

'''
首先考虑最简单的情况。如果只有一间房屋，则偷窃该房屋，可以偷窃到最高总金额。
如果只有两间房屋，则由于两间房屋相邻，只能偷窃其中的一间房屋，因此选择其中金额较高的房屋进行偷窃，可以偷窃到最高总金额。
如果房屋数量大于两间，应该如何计算能够偷窃到的最高总金额呢？对于第k(k>2)间房屋，有两个选项：
1、偷窃第k间房屋，那么就不能偷窃第k−1间房屋，偷窃总金额为前k−2间房屋的最高总金额与第k间房屋的金额之和。
2、不偷窃第 k 间房屋，偷窃总金额为前 k-1 间房屋的最高总金额。
'''
print(Solution().rob([1,2,3,1]))
print(Solution().rob([2,7,9,3,1]))
print(Solution().rob([2,1,1,2]))








































































































