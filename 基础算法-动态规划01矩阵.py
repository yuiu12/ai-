from typing import List
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #在此之间填写代码
        queue = [] 
        a,b = len(mat),len(mat[0]) 
        for i in range(a):
            for j in range(b):
                if mat[i][j]==1:mat[i][j]=-1 
                if mat[i][j]==0:queue.append((i,j)) 
        x = 0 
        while x < len(queue):
            cur = queue[x] 
            for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
                if 0 <= cur[0]+i<a and 0 <= cur[1]+j<b and mat[cur[0]+i][cur[1]+j]==-1:
                    mat[cur[0]+i][cur[1]+j]=mat[cur[0]][cur[1]]+1
                    queue.append((cur[0]+i,cur[1]+j))
            x += 1 
        return mat 
print(Solution().updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))
print(Solution().updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))




















































