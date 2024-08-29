'''
统计有序矩阵中的负数 给你一个 m * n 的矩阵 grid，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。
请你统计并返回 grid 中 负数 的数目。
'''
from typing import List
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        #在此之间填写代码
        def a(x):
            m,n = 0,len(x) - 1 
            while m <= n:
                t = (m+n) // 2 
                if x[t]>=0:m=t+1 
                else:n=t-1 
            return len(x) - m
        b = 0 
        for i in grid:
            b += a(i) 
        return b 

print(Solution().countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
print(Solution().countNegatives([[3,2],[1,0]]))
print(Solution().countNegatives([[1,-1],[-1,-1]]))
print(Solution().countNegatives([[-1]]))








































































