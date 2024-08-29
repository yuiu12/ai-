'''
给定一个已按照 非递减顺序排列 的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。 函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。
'''
from typing import List
'''
可以首先固定第一个数，然后寻找第二个数，第二个数等于目标值减去第一个数的差。
利用数组的有序性质，可以通过二分查找的方法寻找第二个数。为了避免重复寻找，在寻找第二个数时，只在第一个数的右侧寻找。
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #在此之间填写代码
        n = len(numbers) 
        for i in range(n):
            x,y = i+1,n-1 
            while x <= y:
                m = (x+y) // 2 
                if numbers[i] + numbers[m] > target:
                    y=m-1
                elif numbers[i]+numbers[m]<target:x=m+1 
                else:return [i+1,m+1] 
print(Solution().twoSum([2,7,11,15],9))
print(Solution().twoSum([2,3,4],6))
print(Solution().twoSum([-1,0],-1))
