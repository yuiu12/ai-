from typing import List 
class Solution:
    def searchInsert(nums: List[int],target: int) -> int:
            left,right = 0,len(nums) - 1 
            while left <= right:
                 m = (left + right) // 2 
                 if nums[m] > target:right=m-1 
                 elif nums[m]<target:left=m+1 
                 else:
                      return m 
            return left 


if __name__ =='__main__':
    print(Solution.searchInsert([1,3,5,6],5))
    print(Solution.searchInsert([1,3,5,6],2))
    print(Solution.searchInsert([1,3,5,6],7))
    print(Solution.searchInsert([1,3,5,6],0))
    print(Solution.searchInsert([1],0))


































































































