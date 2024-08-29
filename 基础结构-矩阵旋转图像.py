'''
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。 你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
'''
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #在此之间填写代码
        def a(m,n):
            i,x=0,n-m-1 
            if x < 0:return 
            while i <= x:
                matrix[m][m+i],matrix[m+i][n],matrix[n][n-i],matrix[n-i][m]=matrix[n-i][m],matrix[m][m+i],matrix[m+i][n],matrix[n][n-i]
                i+=1
            a(m+1,n-1) 
        a(0,len(matrix)-1) 
        return matrix 

print(Solution().rotate([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
print(Solution().rotate([[1]]))
print(Solution().rotate([[1,2],[3,4]]))






















































