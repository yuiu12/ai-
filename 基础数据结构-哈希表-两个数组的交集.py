from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #在此之间填写代码
        a,b = {},[] 
        for i in nums1:
            a[i] = a.get(i,0) + 1 
        for i in nums2:
            if a.get(i,0)>0:
                b.append(i) 
                a[i] = a.get(i) - 1 
        return b 

print(Solution().intersect([1,2,2,1],[2,2]))
print(Solution().intersect([4,9,5],[9,4,9,8,4]))
print(Solution().intersect([1,2],[1,1]))
print(Solution().intersect([1,3,8,9,3],[1,0]))















































