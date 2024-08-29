'''
给定一个三角形 triangle ，找出自顶向下的最小路径和。

每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。
'''
from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #在此之间填写代码
        a =  len(triangle) 
        def backtrack(triangle,n):
            for i in range(n+1):
                if i == 0:
                    triangle[n][i] = triangle[n-1][i]+triangle[n][i] 
                elif i == n:
                    triangle[n][i] = triangle[n-1][i-1]+triangle[n][i]
                else:
                    triangle[n][i] = min(triangle[n-1][i-1],triangle[n-1][i]) + triangle[n][i] 
            if n == a - 1:return 
            backtrack(triangle,n+1) 
        if a >= 2:backtrack(triangle,1)
        return min(triangle[-1])         

print(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
print(Solution().minimumTotal( [[-10]]))

'''
我们用f[i][j]表示从三角形顶部走到位置(i, j)的最小路径和。这里的位置(i,j)指的是三角形中第i行第j列（均从0开始编号）的位置。
由于每一步只能移动到下一行「相邻的节点」上，因此要想走到位置 (i,j)，上一步就只能在位置 (i−1,j−1) 或者位置 (i - 1, j)(i−1,j)。我们在这两个位置中选择一个路径和较小的来进行转移，状态转移方程为：
f[i][j]=min(f[i−1][j−1],f[i−1][j])+c[i][j]
其中 c[i][j] 表示位置 (i,j) 对应的元素值。
注意三角形每一行两边的元素计算方法不同
'''




































































































