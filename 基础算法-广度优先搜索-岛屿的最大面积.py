from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #在此之间填写代码
        #岛屿面积的最大值
        t = 0
        #整个海面的横竖长度和宽度
        m,n = len(grid),len(grid[0]) 
        #接下来需要遍历的坐标
        queue = [] 
        #存放四个方向
        dir = [(1,0),(0,1),(-1,0),(0,-1)] 
        for i in range(m):
            for j in range(n):
                #该点是否是岛屿，进行之后的操作
                if grid[i][j] == 1:
                    #该岛屿数值赋值为0，避免之后再次遍历
                    grid[i][j] = 0 
                    #定义变量t1记录当前岛屿的面积
                    t1 = 1
                    #存放当前岛屿的坐标
                    queue.append((i,j))
                    #不为空时执行接下来的循环 
                    while queue:
                        #删除第一个元素并将赋值给cur
                        cur = queue.pop(0) 
                        for k in dir:
                            #定义变量x，y存放该方向的横竖坐标
                            x,y = cur[0]+k[0],cur[1]+k[1] 
                            #该点横竖坐标是否在矩阵内且该店是否为岛屿
                            if 0<=x<m and 0<=y<n and  grid[x][y] == 1:
                                grid[x][y] = 0
                                t1 += 1 
                                #加如带点坐标，该点扩散
                                queue.append((x,y)) 
                                
                    if t1>t:t=t1 
        return t

print(Solution().maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
print(Solution().maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))


















































