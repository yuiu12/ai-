'''
给你一个有序数组 nums ，请你原地删除重复出现的元素，使每个元素只出现一次 ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
'''
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #在此之间填写代码
        #快慢指针
        i,j = 1,1 
        n = len(nums) 
        while i < n:
            if nums[i] != nums[i-1]:
                nums[j] = nums[i] 
                j += 1 
            i += 1 
        print(nums[:j]) 
        return j 

print(Solution().removeDuplicates([1,1,2]))
print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

'''
双指针，指的是在遍历对象的过程中，不是普通的使用单个指针进行访问，而是使用两个相同方向（快慢指针）或者相反方向（对撞指针）的指针进行扫描，从而达到相应的目的。
对撞指针
对撞指针是指在有序数组中，将指向最左侧的索引定义为左指针(left)，最右侧的定义为右指针(right)，然后从两头向中间进行数组遍历。

对撞数组适用于有序数组，也就是说当你遇到题目给定有序数组时，应该第一时间想到用对撞指针解题。

快慢指针
快慢指针也是双指针，但是两个指针从同一侧开始遍历数组，将这两个指针分别定义为快指针（fast）和慢指针（slow），两个指针以不同的策略移动，直到两个指针的值相等（或其他特殊条件）为止，如fast每次增长两个，slow每次增长一个。
'''

















































































