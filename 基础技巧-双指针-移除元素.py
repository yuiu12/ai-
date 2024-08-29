'''
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
'''
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #在此之间填写代码
        slow,fast = 0,0 
        a = len(nums) 
        while fast < a:
            if nums[fast] != val:
                nums[slow] = nums[fast] 
                slow += 1 
            fast += 1 
        print(nums[:slow]) 
        return slow 

print(Solution().removeElement([3,2,2,3],3))
print(Solution().removeElement([0,1,2,2,3,0,4,2],2))

'''
由于题目要求删除数组中等于 val 的元素，因此输出数组的长度一定小于等于输入数组的长度，我们可以把输出的数组直接写在输入数组上。
可以使用双指针：右指针 right 指向当前将要处理的元素，左指针 left 指向下一个将要赋值的位置。
如果右指针指向的元素不等于 val，它一定是输出数组的一个元素，我们就将右指针指向的元素复制到左指针位置，然后将左右指针同时右移；
如果右指针指向的元素等于 val，它不能在输出数组里，此时左指针不动，右指针右移一位
'''



















































