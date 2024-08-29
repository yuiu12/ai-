'''
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
'''
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #在此之间填写代码
        #宽度
        m = len(matrix) 
        #长度
        n = len(matrix[0]) 
        i,j = 0,0 
        #a 存放矩阵第一个元素
        a,p = [matrix[i][j]],0 
        matrix[i][j] = '' 
        while p <= 4:
            while j + 1<n and matrix[i][j+1]!='':
                j+=1 
                a.append(matrix[i][j]) 
                matrix[i][j] = '' 
                p = 0 
            p += 1 
            while i+1<m and matrix[i+1][j]!='':
                i += 1 
                a.append(matrix[i][j]) 
                matrix[i][j] = '' 
                p = 0 
            p += 1
            while j-1>=0 and matrix[i][j-1]!='':
                j -= 1 
                a.append(matrix[i][j])
                matrix[i][j] = '' 
                p = 0
            p += 1 
            while i - 1>=0 and matrix[i-1][j] !='':
                i -= 1 
                a.append(matrix[i][j]) 
                matrix[i][j] = '' 
                p = 0
            p += 1 
        return a  


print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))



























































