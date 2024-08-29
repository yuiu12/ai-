'''
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案
'''
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #在此之间填写代码
        #回溯函数，内部变量first用于固定一个值
        def backstack(first=0):
            #则本次列表遍历完成，将该结果加入总列表中
            if first==n:
                a.append(nums[:])
            #first值到列表长度的值
            for i in range(first,n):
                nums[first],nums[i] = nums[i],nums[first]
                backstack(first+1) 
                nums[first],nums[i] = nums[i],nums[first] 
        a = []
        n = len(nums) 
        backstack() 
        return a 

print(Solution().permute([1,2,3]))
print(Solution().permute([0,1]))
print(Solution().permute([1]))









































































